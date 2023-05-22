from gui import Window

def on_close():
    window.destroy()
    window.quit()


if __name__ == "__main__":
    window = Window()

    window.protocol('WM_DELETE_WINDOW', on_close)
    
    window.mainloop()
