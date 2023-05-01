import requests
import json

import tkinter as tk

root = tk.Tk()
root.title("Canlı Kripto Para Verileri")
root.configure(bg="black")

label = tk.Label(root, text="Kripto Para Verileri",fg="green", font=("Terminal", 34))
label.pack(pady=10)
label.configure(bg="black", fg="green")

data = tk.Text(root, height=20, width=80,background="black",fg="green",font=("Terminal",12))
data.pack(padx=20, pady=20)


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'MY_API_KEY'
}
response = requests.get(url, headers=headers)
response_json = json.loads(response.text)

for currency in response_json['data']:
    name = currency['name']
    symbol = currency['symbol']
    price = currency['quote']['USD']['price']
    data.insert(tk.END, f"{name} ({symbol}): ${price}\n\n")

root.mainloop()
