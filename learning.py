import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from datetime import datetime

url = 'https://market.isagha.com/prices'
sales = []
buy = []
status = []
karat = []

def main():
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    golds_karat = soup.find_all('div', {'class': 'gauge text-center'})
    prices = soup.find_all('div', {'class': 'col-xs-4'})

    for i in range(len(prices)):
        price = prices[i].text
        clean_price = price.replace('\n', '').replace('\t', '').strip()
        if 'بيع' in clean_price:
            sales.append(clean_price)
        elif 'شراء' in clean_price:
            buy.append(clean_price)
        else:
            status.append(clean_price)
        if len(golds_karat) > i:
            gold_karat = golds_karat[i].text
            clean_karat = gold_karat.replace('\n', '').replace('\t', '').strip()
            karat.append(clean_karat)

        # Get the current date and time in a formatted string
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Create a PrettyTable with a custom title including the current date and time, and without headers
    table = PrettyTable()
    table.field_names = ["Status", "Buy", "Sale", "Karat"]
    table.title = f"Gold price for {current_datetime}"

    # Add data to the table
    for st, b, s, k in zip(status, buy, sales, karat):
        table.add_row([st, b, s, k])

    # Print the table without headers
    print(table.get_string(header=False))


main()
