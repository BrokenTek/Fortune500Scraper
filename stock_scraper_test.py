'''
Author: Carson Pribble
Purpose: This is a simple test for StockScraper. Allows for printing
    and writing the data.
'''

from StockScraper import StockScraper

def main():
    scraper = StockScraper()
    print("\nA 'StockScraper' instance has been created. Please choose a testing option below\n")
    try:
        input1 = int(input("Enter 1 to print stock data, 2 to write stock data to csv: "))
    except:
        print("Input Must Be An Integer 1 or 2. Option 1 Chosen By Default")
        input1 = 1
    if input1 == 1:
        scraper.printData()
    elif input1 == 2:
        scraper.writeData()
    else:
        print("Invalid Input")

if __name__ == "__main__":
    main()


