import requests
import json
import tkinter as tk
import time

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
    'X-CMC_PRO_API_KEY': '37ec0d2d-88b3-4bd0-830c-e30f173b3706'
}
def update_data():

    response = requests.get(url, headers=headers)
    response_json = json.loads(response.text)

    data.delete("1.0",tk.END)
    for currency in response_json['data']:
        name = currency['name']
        symbol = currency['symbol']
        price = currency['quote']['USD']['price']
        data.insert(tk.END, f"{name} ({symbol}): ${price}\n\n")
    root.after(3000,update_data)
update_data()
root.mainloop()
