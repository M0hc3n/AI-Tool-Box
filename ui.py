from tkinter import Tk, TOP, LEFT, RIGHT
from visualizer import Visualizer
from sidebar import SideBar


class UI(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(" AI ToolBox ")

        self.configure(
            background="white",
            borderwidth=2,
        )

        simple_graph = {
            "A": {
                "B": 2,
                "C": 3,
            },
            "B": {
                "A": 2,
                "B": 4,
                "D": 5,
            },
            "C": {
                "A": 3,
                "B": 4,
                "D": 3,
                "F": 6
            },
            "D": {
                "B": 5,
                "C": 3,
                "E": 2,
            },
            "E": {
                "D": 2,
                "F": 3,
                "G": 5,
            },
            "F": {
                "C": 6,
                "E": 3
            },
            "G": {
                "E": 5
            },
        }

        self.geometry("800x600")
        self.resizable(width=False, height=False)

        self.visualizer = Visualizer(self, simple_graph, bg="white")
        self.visualizer.pack(fill="both", expand=True)

        self.sidebar = SideBar(self, self.visualizer, border=2)
        self.sidebar.pack(side=LEFT, fill="y")
