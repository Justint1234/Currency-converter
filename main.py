from optparse import Values
import tkinter as tk
from forex_python.converter import CurrencyRates

common_CurrencyRates = ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'CHF', 'NZD']

class CurrencyConverter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Currency Converter')
        self.root.geometry('200x180')

        self.from_var = tk.StringVar(self.root)
        self.from_var.set('USD')
        self.from_menu = tk.OptionMenu(self.root, self.from_var, *common_currencies)
        self.from_menu.pack(pady=1)

        self.to_var = tk.StringVar(self.root)
        self.to_var.set('EUR')
        self.to_menu = tk.OptionMenu(self.root, self.to_var, *common_currencies)
        self.to_menu.pack(pady=1)

        self.amount_label = tk.Label(self.root, text='Amount:')
        self.amount_label.pack(pady=1)

        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack(pady=1)

        self.convert_button = tk.Button(self.root, text='Convert', command=self.convert_currency)


