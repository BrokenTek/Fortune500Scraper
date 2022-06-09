'''

Authoer: Carson Pribble
This is a module that contains two functions.
stockScrapePagePrint : Prints data from all 500 S&P Companies
stockScrapePageWrite : Writes data from all 500 S&P Companies to a CSV

'''

from bs4 import BeautifulSoup as bs
import requests
import csv

# This is the printer function
def scrapeStockPagePrint(url):

	url_page_list = []
	names_list = []
	price_list = []
	low_high_list = []
	plusminus_percent_list = []
	time_date_list = []

	for i in range(1,12):
		url_page = url + "?p=" + str(i)
		url_page_list.append(url_page)	

	for url in url_page_list:
		page = requests.get(url)
		soup = bs(page.content, 'html.parser')

		body = soup.find(class_="table__tbody")

		t_body_list = (soup.find(class_="table__tbody"))

		tr = t_body_list.select("tr")

		for i in tr:
			td = i.select("td")
			name = td[0].get_text().strip()
			prices = td[1].get_text().strip()
			low_high = td[2].get_text().strip()
			plusminus_percent = td[3].get_text().strip()
			time_date = td[4].get_text().strip()

			names_list.append(name)
			price_list.append(prices.replace("\n"," "))
			low_high_list.append(low_high.replace("\n"," "))
			plusminus_percent_list.append(plusminus_percent.replace("\n"," "))
			time_date_list.append(time_date.replace("\n"," "))

	for i in range(len(names_list)):
		print("Stock Name:",names_list[i])
		print("Latest Price:", price_list[i].split()[0], "| Previous Close:", price_list[i].split()[1])
		print("Low:", low_high_list[i].split()[0], "| High:", low_high_list[i].split()[1])
		print("Change:", plusminus_percent_list[i].split()[0], "| Percent:", plusminus_percent_list[i].split()[1])
		print("Time:", time_date_list[i].split()[0], "| Date:", time_date_list[i].split()[5])
		print()

# This is the writer function
def scrapeStockPageWrite(url):
	# Set to append or write, current append
	f = open('sp_stock_date.csv', 'a')
	writer = csv.writer(f)
	writer.writerow(["Name","Latest Price","Previous Close","Low","High","Change","Percent Change","Time","Date"])

	url_page_list = []
	names_list = []
	price_list = []
	low_high_list = []
	plusminus_percent_list = []
	time_date_list = []

	for i in range(1,12):
		url_page = url + "?p=" + str(i)
		url_page_list.append(url_page)

	for url in url_page_list:
		page = requests.get(url)
		soup = bs(page.content, 'html.parser')

		body = soup.find(class_="table__tbody")

		t_body_list = (soup.find(class_="table__tbody"))

		tr = t_body_list.select("tr")

		names_list = []
		price_list = []
		low_high_list = []
		plusminus_percent_list = []
		time_date_list = []


		for i in tr:
			td = i.select("td")
			name = td[0].get_text().strip()
			prices = td[1].get_text().strip()
			low_high = td[2].get_text().strip()
			plusminus_percent = td[3].get_text().strip()
			time_date = td[4].get_text().strip()

			names_list.append(name)
			price_list.append(prices.replace("\n"," "))
			low_high_list.append(low_high.replace("\n"," "))
			plusminus_percent_list.append(plusminus_percent.replace("\n"," "))
			time_date_list.append(time_date.replace("\n"," "))

	for i in range(len(names_list)):
		row = [names_list[i], price_list[i].split()[0], price_list[i].split()[1], low_high_list[i].split()[0],
		low_high_list[i].split()[1], plusminus_percent_list[i].split()[0], plusminus_percent_list[i].split()[1],
		time_date_list[i].split()[0], time_date_list[i].split()[5]]
		writer.writerow(row)