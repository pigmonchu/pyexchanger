from tkinter import *
from tkinter import ttk

class CurrencyConverter(ttk.Frame):
    
    def __init__(self, parent, **args):
        ttk.Frame.__init__(self, parent, height=args['height'], width=args['width'])

        self.inQuantityEntry = ttk.Entry(self, font=('Helvetica', 24, 'bold'), width=10).place(x=38, y=23)
        self.inCurrencyCombo = ttk.Combobox(self, width=10, height=5).place(x=38, y=71)
        ttk.Label(self, text='⥮').place(x=102, y=98)
        self.outCurrencyCombo = ttk.Combobox(self, width=10, height=5).place(x=38, y=120)
        self.outQuantityLabel = ttk.Label(self, width=10, font=('Helvetica', 24), text='0000000000').place(x=38, y=166)




class MainApp(Tk):
    __currencyConverter = None

    def __init__(self):
        Tk.__init__(self)
        self.title("Convertidor de divisas")
        self.geometry("378x229")
        self.__currencyConverter = CurrencyConverter(self, width=378, height=229).place(x=0, y=0)

    def start(self):
        self.mainloop()


if __name__ == '__main__':
    app = MainApp()
    app.start()