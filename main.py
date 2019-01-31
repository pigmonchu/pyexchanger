from tkinter import *
from tkinter import ttk


currencies = {
    'EUR': 1,
    'USD': 0.9,
    'CAD': 0.75
}

class CurrencyConverter(ttk.Frame):
    __oldValueInQuantity = None
    
    def __init__(self, parent, **args):
        ttk.Frame.__init__(self, parent, height=args['height'], width=args['width'])

        #Variables de control
        self.inQuantity = DoubleVar(value=0)
        self.__strInQuantity = StringVar(value="")
        self.__oldValueInQuantity = ""
        self.__strInQuantity.trace('w', self.validateQuantity)
        self.outQuantity = 0.0
        self.inCurrency = StringVar()
        self.outCurrency = StringVar()

        currency_keys = []
        for key in currencies.keys():
            currency_keys.append(key)

        self.inQuantityEntry = ttk.Entry(self, font=('Helvetica', 24, 'bold'), width=10, textvariable=self.__strInQuantity).place(x=38, y=23)
        self.inCurrencyCombo = ttk.Combobox(self, width=10, height=5, values=currency_keys, textvariable=self.inCurrency)
        self.inCurrencyCombo.place(x=38, y=71)
        self.inCurrencyCombo.bind("<<ComboboxSelected>>", self.convertirDivisas)
        ttk.Label(self, text='⥮').place(x=102, y=98)
        self.outCurrencyCombo = ttk.Combobox(self, width=10, height=5, values=currency_keys, textvariable=self.outCurrency)
        self.outCurrencyCombo.place(x=38, y=120)
        self.outCurrencyCombo.bind("<<ComboboxSelected>>", self.convertirDivisas)
        self.outQuantityLabel = ttk.Label(self, width=10, font=('Helvetica', 24), text='0000000000')
        self.outQuantityLabel.place(x=38, y=166)

    def convertirDivisas(self, *args):
        _amount = self.__strInQuantity.get()
        _from = self.inCurrency.get()
        _to = self.outCurrency.get()

        resultado = 0

        if _amount != "" and _from != "" and _to != "":
            if _to == 'EUR':
                resultado = float(_amount) * currencies[_from]
            elif _from == 'EUR':
                resultado = float(_amount) / currencies[_to]
            else: 
                resultado = float(_amount) * currencies[_from] / currencies[_to]

            self.outQuantityLabel.config(text=str(resultado))


    def validateQuantity(self, *args):
        try:
            if self.__strInQuantity.get() != "":
                v = self.__strInQuantity.get()
                valorParaOld = v
                v = v.replace('.', '@')
                v = v.replace(',', '.')
                float(v)
                self.__oldValueInQuantity = valorParaOld
                self.convertirDivisas()
        except:
            self.__strInQuantity.set(self.__oldValueInQuantity)

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