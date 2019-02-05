from tkinter import *
from tkinter import ttk
import requests
import json

class CurrencyConverter(ttk.Frame):
    __APICURRENCYLIST_EP = 'https://free.currencyconverterapi.com/api/v6/currencies'
    __APICURRENCYCONVERSION_EP = 'https://free.currencyconverterapi.com/api/v6/convert?q={}_{}&compact=ultra'

    __oldValueInQuantity = None
    
    def __init__(self, parent, **args):
        ttk.Frame.__init__(self, parent, height=args['height'], width=args['width'])

        #Variables de control
        self.inQuantity = DoubleVar(value=0)
        self.__strInQuantity = StringVar(value="")
        self.__oldValueInQuantity = ""
        self.__strInQuantity.trace('w', self.validateQuantity)
        self.outQuantity = 0.0
        self.outCurrency = StringVar()
        self.inCurrency = StringVar()

        currency_keys = self.__getCurrencies()

        self.inQuantityEntry = ttk.Entry(self, font=('Helvetica', 24, 'bold'), width=10, textvariable=self.__strInQuantity).place(x=38, y=23)
        self.inCurrencyCombo = ttk.Combobox(self, width=25, height=5, values=currency_keys, textvariable=self.inCurrency)
        self.inCurrencyCombo.place(x=38, y=71)
        self.inCurrencyCombo.bind("<<ComboboxSelected>>", self.convertirDivisas)
        ttk.Label(self, text='⥮').place(x=102, y=98)
        self.outCurrencyCombo = ttk.Combobox(self, width=25, height=5, values=currency_keys, textvariable=self.outCurrency)
        self.outCurrencyCombo.place(x=38, y=120)
        self.outCurrencyCombo.bind("<<ComboboxSelected>>", self.convertirDivisas)
        self.outQuantityLabel = ttk.Label(self, width=10, font=('Helvetica', 24), text='0000000000')
        self.outQuantityLabel.place(x=38, y=166)

    def convertirDivisas(self, *args):
        _amount = self.__strInQuantity.get()
        _from = self.inCurrency.get()
        _to = self.outCurrency.get()

        if _amount != "" and _from != "" and _to != "":
            _to = _to[:3]
            _from = _from[:3]
            url = self.__APICURRENCYCONVERSION_EP.format(_from, _to)
            response = requests.get(url)

            if response.status_code == 200:
                value = json.loads(response.text)
                tasa = value["{}_{}".format(_from, _to)]
                resultado = float(tasa) * float(_amount)

                self.outQuantityLabel.config(text=str(resultado))
            else:
                print("Se ha producido un error", response.status_code)

    def validateQuantity(self, *args):
        try:
            if self.__strInQuantity.get() != "":
                v = self.__strInQuantity.get()
                valorParaOld = v
                v = v.replace('.', '@')
                v = v.replace(',', '.')
                float(v)
                if v[0] == '-':
                    self.__strInQuantity.set(self.__oldValueInQuantity)
                else:
                    self.__oldValueInQuantity = valorParaOld
                    self.convertirDivisas()
        except:
            self.__strInQuantity.set(self.__oldValueInQuantity)

    def __getCurrencies(self):
        response = requests.get(self.__APICURRENCYLIST_EP)

        if response.status_code == 200:
            currencies = json.loads(response.text)['results']
            result = []
            for key in currencies.keys():
                value = "{} - {}".format(key, currencies[key]['currencyName'])
                result.append(value)
            result.sort()
            return result
        else:
            print("Se ha producido un error", response.status_code)

        

class MainApp(Tk):
    __currencyConverter = None


    def __init__(self):
        Tk.__init__(self)
        self.title("Convertidor de divisas")
        self.geometry("378x229")
        self.__currencyConverter = CurrencyConverter(self, width=378, height=229)
        self.__currencyConverter.place(x=0, y=0)

    def start(self):
        self.mainloop()


if __name__ == '__main__':
    app = MainApp()
    app.start()