from bs4 import BeautifulSoup as bs4
import requests

def get_item(marketWatch_url):
    source = requests.get(marketWatch_url).text
    soup = bs4(source, 'lxml')
    intraData = soup.find("div", {"class":"intraday__data"})
    currency = intraData.find("sup", {"class":"character"}).get_text()
    intraDayValue = intraData.find("span",{"class":"value"}).get_text()
    stockValue = currency + intraDayValue
    return stockValue


def get_exchange_rates():
    source = requests.get("https://www.exchangerates.org.uk/").text
    soup = bs4(source, 'lxml')
    data = soup.findAll(class_='colthree')
    euro, dollar, *_ = val = [x.strong.text for x in data]
    return [euro, dollar]


def currency_check(stock_value):
    if 'p' in stock_value:
        stock_value = stock_value.replace('p', '')
        return 'p', float(stock_value)
    if '$' in stock_value:
        stock_value = stock_value.replace('$', '')
        return '$', float(stock_value)
    if '€' in stock_value:
        stock_value = stock_value.replace('€', '')
        return '€', float(stock_value)


def euro_to_gbp(value, exchange_rate):
    gbp_val = value / float(exchange_rate)
    gbp_3sf = "%.2f" % round(gbp_val, 3)
    return f"£{gbp_3sf}"


def pence_to_gbp(value):
    gbp_numeric = value / 100
    return f"£{gbp_numeric}"


def dollar_to_gbp(value, exchange_rate):
    gbp_val = value / float(exchange_rate)
    gbp_3sf = "%.2f" % round(gbp_val, 3)
    return f"£{gbp_3sf}"


def gbp_standardise(argument, value, exchange_rate):
    switcher = {
        'p': pence_to_gbp(value),
        '€': euro_to_gbp(value, exchange_rate[0]),
        '$': dollar_to_gbp(value, exchange_rate[1])
    }
    return switcher.get(argument, "invalid currency")


