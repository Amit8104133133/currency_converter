import tkinter as tk
import requests

def convert_currency():
    amount = float(entry_amount.get())
    from_currency = from_var.get()
    to_currency = to_var.get()

    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    
    rate = data["rates"].get(to_currency)
    if rate:
        converted = amount * rate
        result_label.config(text=f"{amount} {from_currency} = {converted:.2f} {to_currency}")
    else:
        result_label.config(text="Conversion failed.")

# GUI setup
root = tk.Tk()
root.title("Currency Converter")
root.geometry("300x250")

tk.Label(root, text="Amount:").pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

tk.Label(root, text="From Currency (e.g. USD):").pack()
from_var = tk.StringVar()
entry_from = tk.Entry(root, textvariable=from_var)
entry_from.pack()

tk.Label(root, text="To Currency (e.g. INR):").pack()
to_var = tk.StringVar()
entry_to = tk.Entry(root, textvariable=to_var)
entry_to.pack()

tk.Button(root, text="Convert", command=convert_currency).pack(pady=10)
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()