import Scraper
import Printer
import csv
import os
import requests
import time
import Companies


def scrapeLoop(schema):
    while True:
        currentValues = [Scraper.getCurrentValue(company['url']) for company in schema]
        exchangeRates = Scraper.getExchangeRates()
        currencies = [Scraper.currencyChecker(x) for x in currentValues]
        adjustedValues = [Scraper.standardiseToSterling(company[0], company[1], exchangeRates) for company in currencies]
        counter = 0
        for company in schema:
            company["value"] = adjustedValues[counter]
            counter = counter + 1
        Printer.writeToCSV(schema)
        time.sleep(60)


if __name__ == "__main__":
    scrapeLoop(Companies.COMPANY_SCHEMAS)














