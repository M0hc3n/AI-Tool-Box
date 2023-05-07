from tkinter import Canvas, Scrollbar, VERTICAL, RIGHT, Y
from time import sleep


class Visualizer(Canvas):
    def __init__(self, master, problem, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.problem = problem

        self.current_x = 200
        self.current_y = 100

        vertical_scrollbar = Scrollbar(master, orient=VERTICAL)
        vertical_scrollbar.pack(side=RIGHT, fill=Y)
        vertical_scrollbar.config(command=self.yview)

        self.configure(yscrollcommand=vertical_scrollbar.set)

    def call_dfs(self, event):

        if self.depth_first_search(self.problem, "A", "", self.current_x, self.current_y):
            print("Goal Found")
        else:
            print("Goal could not be reached")

    def depth_first_search(self, problem, start, end, x, y, visited=set()):
        sleep(.5)

        visited.add(start)

        self.drawCircle(start, x, y)
        self.update()

        if (start == end):
            return True

        for i, neighbour in enumerate(list(set(problem[start]) - visited)):
            new_x, new_y = x+i*100, y+100

            sleep(.5)
            self.create_line(x+25, y+50, new_x+25, new_y)
            self.update()

            sleep(.5)

            if neighbour == end:
                self.drawCircle(neighbour, new_x, new_y, color="green")
                self.update()
                return True

            self.drawCircle(neighbour, new_x, new_y)
            self.update()

            result = self.depth_first_search(
                problem, neighbour, end, new_x, new_y, visited)

            if result:
                return result

        return False

    def drawCircle(self, label, x, y, radius=50, color="gray"):
        self.create_oval(x, y, x + radius, y + radius, fill=color)
        self.create_text(x + radius//2, y + radius//2, text=label,
                         fill="black", font=('Helvetica 15 bold'))
