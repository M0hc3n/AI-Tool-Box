from tkinter import ttk, TOP


class SideBar(ttk.Frame):
    def __init__(self, master, visualizer, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.visualize_dfs = ttk.Button(
            self,
            text="Visualize DFS",
            command=lambda: visualizer.call_dfs(0)
        )
        self.visualize_dfs.pack(side=TOP)

        self.clear = ttk.Button(
            self,
            text="clear",
            command=lambda: visualizer.delete("all")
        )
        self.clear.pack(side=TOP)
