from bs4 import BeautifulSoup as bs4
import requests
import re

def getCurrentValue(marketWatch_url):
    source = requests.get(marketWatch_url).text
    soup = bs4(source, 'lxml')
    intraData = soup.find("div", {"class":"intraday__data"})
    currency = intraData.find("sup", {"class":"character"}).get_text()
    intraDayValue = intraData.find("span",{"class":"value"}).get_text()
    stockValue = currency + intraDayValue
    return stockValue


def getExchangeRates():
    source = requests.get("https://www.exchangerates.org.uk/").text
    soup = bs4(source, 'lxml')
    data = soup.findAll(class_='colthree')
    euro, dollar, *_ = val = [x.strong.text for x in data]
    exchangeRates = {"euro" : euro, "dollar": dollar}
    return exchangeRates


def currencyChecker(stock_value):
    if 'p' in stock_value:
        parsedVal = re.sub('p|,', '', stock_value)
        return 'p', float(parsedVal)
    if '$' in stock_value:
        parsedVal = re.sub('$|,', '', stock_value)
        return '$', float(parsedVal)
    if '€' in stock_value:
        parsedVal = re.sub('€|,', '', stock_value)
        return '€', float(parsedVal)


def euroToGBP(value, exchange_rate):
    gbp_val = value / float(exchange_rate['euro'])
    gbp_3sf = "%.2f" % round(gbp_val, 3)
    return f"£{gbp_3sf}"


def penceToGBP(value, exchange_rate):
    gbp_numeric = value / 100
    return f"£{gbp_numeric}"


def dollarToGBP(value, exchange_rate):
    gbp_val = value / float(exchange_rate['dollar'])
    gbp_3sf = "%.2f" % round(gbp_val, 3)
    return f"£{gbp_3sf}"


def standardiseToSterling(argument, value, exchange_rate):
    converterSwitch = {'p': penceToGBP,'€': euroToGBP,'$': dollarToGBP}
    return converterSwitch.get(argument, "invalid currency")(value, exchange_rate)

