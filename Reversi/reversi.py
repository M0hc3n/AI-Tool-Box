import ai


class Game_error(Exception):
    """Errors related to the game in general"""
    pass


class Illegal_move(Game_error):
    """Errors from illegal moves"""
    pass


class Game_rule_error(Game_error):
    """Errors that arise from rule issues"""
    pass


class Reversi():
    """
    0 = Empty
    1 = White (player 1)
    2 = Black (player 2)
    """

    def __init__(self):

        self.turn = 1
        self.player = 1
        self.victory = 0

        self.board = [[0 for x in range(8)] for x in range(8)]

        self.board[3][3] = 1
        self.board[3][4] = 2
        self.board[4][3] = 2
        self.board[4][4] = 1

        self.use_ai = True
        self.ai = ai.GameAI(self)

        self.has_changed = True
        self.ai_is_ready = False

    def player_move(self, x, y):
        if self.victory != 0:
            return

        if self.use_ai and self.player != 1:
            return

        self.perform_move(x, y)

        if self.use_ai:
            self.ai_is_ready = True

    def __get_all_tiles(self):
        return [tile for row in self.board for tile in row]

    def __count_tiles_of_type(self, all_tiles, tile_type=0):
        return sum(1 for tile in all_tiles if tile == tile_type)

    def perform_move(self, x, y):

        if(x== -1 and y == -1):
            self.player = 3 - self.player
            self.has_changed = True 
            return

        if self.board[x][y] != 0:
            raise Illegal_move(
                f"Player {self.player} tried to place a tile at {x},{y} but it is already occupied by {self.board[x][y]}")

        self.place_piece(x, y)

        all_tiles = self.__get_all_tiles()

        empty_tiles = self.__count_tiles_of_type(all_tiles, 0)
        white_tiles = self.__count_tiles_of_type(all_tiles, 1)
        black_tiles = self.__count_tiles_of_type(all_tiles, 2)

        if white_tiles < 1 or black_tiles < 1 or empty_tiles < 1:
            self.end_game()
            return

        legal_move_exists = self.legal_move_exists()

        if not legal_move_exists:
            print('game ended')
            self.end_game()
            return

        # alternate between player 1 and 2
        self.player = 3 - self.player
        self.has_changed = True

    def legal_move_exists(self):
        move_found = False

        for x in range(0, 8):
            for y in range(0, 8):
                if move_found:
                    break
                if self.board[x][y] == 0:
                    number_of_changes = self.place_piece(x, y, live_mode=False)
                    if number_of_changes > 0:
                        move_found = True

        return move_found

    def ai_move(self):
        self.ai.make_move()
        self.ai_is_ready = False

    def __set_victory_status(self, white_tiles_count, black_tiles_count):
        if white_tiles_count > black_tiles_count:
            self.victory = 1
        elif white_tiles_count < black_tiles_count:
            self.victory = 2
        else:
            self.victory = -1

    def end_game(self):
        all_tiles = self.__get_all_tiles()

        white_tiles = self.__count_tiles_of_type(all_tiles, 1)
        black_tiles = self.__count_tiles_of_type(all_tiles, 2)

        self.__set_victory_status(white_tiles, black_tiles)
        self.has_changed = True

    def __get_cross_diagonal(self, x, y):
        i, j = x-7, y+7
        bottom_left_top_right_diagonal = []

        for q in range(0, 16):
            if 0 <= i < 8 and 0 <= j < 8:
                bottom_left_top_right_diagonal.append(self.board[i][j])

            i += 1
            j -= 1

        return bottom_left_top_right_diagonal

    def __get_main_diagonal(self, x, y):
        i, j = x-7, y-7
        bottom_right_top_left_diagonal = []

        for q in range(0, 16):
            if 0 <= i < 8 and 0 <= j < 8:
                bottom_right_top_left_diagonal.append(self.board[i][j])
            i += 1
            j += 1

        return bottom_right_top_left_diagonal

    def __move_up(self, x, y, column, live_mode):
        if not self.player in column[:y]:
            return 0

        changes = []
        search_complete = False

        for i in range(y-1, -1, -1):
            if search_complete:
                break

            counter = column[i]

            if counter == 0:
                changes = []
                search_complete = True
            elif counter == self.player:
                search_complete = True
            else:
                changes.append(i)

        if search_complete:
            if live_mode:
                for i in changes:
                    self.board[x][i] = self.player

            return len(changes)

        return 0

    def __move_down(self, x, y, column, live_mode):
        if not self.player in column[y:]:
            return 0

        changes = []
        search_complete = False

        for i in range(y+1, 8, 1):
            if search_complete:
                break

            counter = column[i]

            if counter == 0:
                changes = []
                search_complete = True
            elif counter == self.player:
                search_complete = True
            else:
                changes.append(i)

        if search_complete:
            if live_mode:
                for i in changes:
                    self.board[x][i] = self.player

            return len(changes)

        return 0

    def __move_left(self, x, y, row, live_mode):
        if not self.player in row[:x]:
            return 0

        changes = []
        search_complete = False

        for i in range(x-1, -1, -1):
            if search_complete:
                break

            counter = row[i]

            if counter == 0:
                changes = []
                search_complete = True
            elif counter == self.player:
                search_complete = True
            else:
                changes.append(i)

        # Perform changes
        if search_complete:
            if live_mode:
                for i in changes:
                    self.board[i][y] = self.player

            return len(changes)

        return 0

    def __move_right(self, x, y, row, live_mode):
        if not self.player in row[x:]:
            return 0

        changes = []
        search_complete = False

        for i in range(x+1, 8, 1):
            if search_complete:
                break

            counter = row[i]

            if counter == 0:
                changes = []
                search_complete = True
            elif counter == self.player:
                search_complete = True
            else:
                changes.append(i)

        if search_complete:
            if live_mode:
                for i in changes:
                    self.board[i][y] = self.player

            return len(changes)

        return 0

    def __move_up_right(self, x, y, cross_diagonal, live_mode):
        if not self.player in cross_diagonal:
            return 0

        changes = []
        search_complete = False
        i = 0
        lx, ly = x, y

        while 0 <= lx < 8 and 0 <= ly < 8:
            lx += 1
            ly -= 1

            if search_complete or lx > 7 or ly < 0:
                break

            counter = self.board[lx][ly]

            if counter == 0:
                changes = []
                search_complete = True
            elif counter == self.player:
                search_complete = True
            else:
                changes.append((lx, ly))

        # Perform changes
        if search_complete:
            if live_mode:
                for i, j in changes:
                    self.board[i][j] = self.player

            return len(changes)

        return 0

    def __move_down_left(self, x, y, cross_diagonal, live_mode):
        if not self.player in cross_diagonal:
            return 0

        changes = []
        search_complete = False
        i = 0
        lx, ly = x, y

        while 0 <= lx < 8 and 0 <= ly < 8:
            lx -= 1
            ly += 1

            if search_complete or lx < 0 or ly > 7:
                break

            counter = self.board[lx][ly]

            if counter == 0:
                changes = []
                search_complete = True
                break
            elif counter == self.player:
                search_complete = True
                break
            else:
                changes.append((lx, ly))

        # Perform changes
        if search_complete:
            if live_mode:
                for i, j in changes:
                    self.board[i][j] = self.player

            return len(changes)

        return 0

    def __move_up_left(self, x, y, main_diagonal, live_mode):
        if not self.player in main_diagonal:
            return 0
        changes = []
        search_complete = False
        i = 0
        lx, ly = x, y

        while 0 <= lx < 8 and 0 <= ly < 8:
            lx -= 1
            ly -= 1

            if lx < 0 or ly < 0:
                break
            if search_complete:
                continue

            counter = self.board[lx][ly]

            if counter == 0:
                changes = []
                search_complete = True
            elif counter == self.player:
                search_complete = True
            else:
                changes.append((lx, ly))

        # Perform changes
        if search_complete:
            if live_mode:
                for i, j in changes:
                    self.board[i][j] = self.player
            return len(changes)

        return 0

    def __move_down_right(self, x, y, main_diagonal, live_mode):
        if not self.player in main_diagonal:
            return 0
        changes = []
        search_complete = False
        i = 0
        lx, ly = x, y

        while 0 <= lx < 8 and 0 <= ly < 8:
            lx += 1
            ly += 1

            if lx > 7 or ly > 7:
                break
            if search_complete:
                continue

            counter = self.board[lx][ly]

            if counter == 0:
                changes = []
                search_complete = True
            elif counter == self.player:
                search_complete = True
            else:
                changes.append((lx, ly))

        # Perform changes
        if search_complete:
            if live_mode:
                for i, j in changes:
                    self.board[i][j] = self.player
            return len(changes)

        return 0

    def place_piece(self, x, y, live_mode=True):
        if live_mode:
            self.board[x][y] = self.player
        change_count = 0

        column = self.board[x]
        row = [self.board[i][y] for i in range(0, 8)]
        main_diagonal = self.__get_main_diagonal(x, y)
        cross_diagonal = self.__get_cross_diagonal(x, y)

        # First can we travel up?
        change_count += self.__move_up(x, y, column, live_mode)

        # Down?
        change_count += self.__move_down(x, y, column, live_mode)

        # Left?
        change_count += self.__move_left(x, y, row, live_mode)

        # Right?
        change_count += self.__move_right(x, y, row, live_mode)

        # Up Right
        change_count += self.__move_up_right(x, y, cross_diagonal, live_mode)

        # Down Left
        change_count += self.__move_down_left(x, y, cross_diagonal, live_mode)

        # Up Left
        change_count += self.__move_up_left(x, y, main_diagonal, live_mode)

        # Down Right
        change_count += self.__move_down_right(x, y, main_diagonal, live_mode)

        if change_count == 0 and live_mode:
            self.board[x][y] = 0
            raise Illegal_move("Player {0} tried to place a tile at {1},{2} but that will result in 0 flips".format(
                self.player,
                x, y,
            ))

        return change_count

    def get_copy(self):
        game_copy = Reversi()

        game_copy.turn = self.turn
        game_copy.player = self.player
        game_copy.victory = self.victory

        # game_copy.board = self.board

        game_copy.board = [row[:] for row in self.board]

        game_copy.use_ai = self.use_ai
        game_copy.ai = self.ai

        game_copy.has_changed = self.has_changed
        game_copy.ai_is_ready = self.ai_is_ready

        return game_copy
