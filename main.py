import Scraper
import Printer
from datetime import datetime
import csv
import os
import requests
import time


def loopz(rsda, ajb, un_utilities):
    while True:
        date = datetime.now()
        Company_list = [Scraper.get_item(hgl), Scraper.get_item(ajb),
                        Scraper.get_item(un_utilities)]
        dem_rates = Scraper.get_exchange_rates()
        currency_checks = [Scraper.currency_check(x) for x in Company_list]
        stock_final = [Scraper.gbp_standardise(x[0], x[1], dem_rates) for x in currency_checks]
        stock_final.insert(4, date)
        Printer.write_val(stock_final)
        time.sleep(60)


if __name__ == "__main__":
    hgl = "https://www.marketwatch.com/investing/stock/hl?countrycode=uk"
    ajb = "https://www.marketwatch.com/investing/stock/ajb?countrycode=uk"
    Un_utilities = "https://www.marketwatch.com/investing/stock/uu?countrycode=uk"
    loopz(hgl, ajb, Un_utilities)














