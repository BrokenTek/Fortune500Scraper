from Fortune500Scraper import *

url = "https://markets.businessinsider.com/index/components/s&p_500"

choice = int(input("Enter 1 to print S&P stock data or 2 to write S&P stock data: "))

if choice == 1:
	scrapeStockPagePrint(url)
elif choice == 2:
	scrapeStockPageWrite(url)
else:
	print("Invalid Input")