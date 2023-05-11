class GameAI():

    def __init__(self, game):
        self.game = game

    def make_move(self):
        (x, y), _ = self.minimax(self.game)
        self.game.perform_move(x, y)

    def legal_moves(self, game):
        legal_moves_ = []
        for x in range(0, 8):
            for y in range(0, 8):
                if game.board[x][y] == 0:
                    c = game.place_piece(x, y, live_mode=False)
                    if c > 0:
                        legal_moves_.append((x, y))
        return legal_moves_

    def count_tiles(self, game, tile_type=0):
        count = 0

        for row in game.board:
            for tile in row:
                count += tile if tile == tile_type else 0

        return count

    def heuristic(self, game):
        white_count = self.count_tiles(game, 1)
        black_count = self.count_tiles(game, 2)

        return white_count - black_count

    def min_value(self, game, depth, cutoff):
        if depth >= cutoff:
            return None, self.heuristic(game)

        minimum = float('inf')
        min_move = (-1, -1)

        for move in self.legal_moves(game):
            state = game.get_copy()
            state.perform_move(move[0], move[1])
            result = self.minimax(state, depth=depth+1, cutoff=cutoff)

            evaluation = result[1]

            if evaluation <= minimum:
                minimum = evaluation
                min_move = move

        return min_move, minimum

    def max_value(self, game, depth, cutoff):

        if (depth >= cutoff):
            return None, self.heuristic(game)

        maximum = float('-inf')
        max_move = (-1, -1)

        for move in self.legal_moves(game):
            state = game.get_copy()
            state.perform_move(move[0], move[1])
            result = self.minimax(state, depth=depth+1, cutoff=cutoff)

            evaluation = result[1]

            if evaluation > maximum:
                maximum = evaluation
                max_move = move

        return max_move, maximum

    def minimax(self, game, depth=0, cutoff=8):
        if game.player == 1:
            max_value = self.max_value(game, depth=depth+1, cutoff=cutoff)
            return max_value

        elif game.player == 2:
            min_value = self.min_value(game, depth=depth+1, cutoff=cutoff)
            return min_value
