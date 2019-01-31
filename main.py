from tkinter import *
from tkinter import ttk

class MainApp(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title("Convertidor de divisas")
        self.geometry("378x229")

    def start(self):
        self.mainloop()


if __name__ == '__main__':
    app = MainApp()
    app.start()