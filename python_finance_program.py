import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from bs4 import BeautifulSoup
import requests
from math import floor

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))
#============================PFP_COMMANDS============================
def help():
    print('''
Press 't' for a summary of a ticker symbol
Press 'l' for a list of popular stocks
Press 'y' for a graph of the current yield curve
Press 'f' for US Treasury Data
Press 'h' for a list of commands
Press 'q' to quit
''')
#-------------------------------------------------------------------
def quit():
    check = input('Are you sure you want to quit? y/n ')
    for r in check:
        if check == 'y':
            print('Quitting...')
        elif check == 'n':
            pfp()
        else:
            print('Did not understand. Please try again')
            quit()
#=======================================================================
def yield_curve():
    onemonth = 2.42
    twomonth = 2.42
    threemonth = 2.45
    sixmonth = 2.54
    one = 2.58
    two = 2.53
    three = 2.51
    five = 2.53
    seven = 2.60
    ten = 2.70
    twenty = 2.86
    thirty = 2.99
    plt.plot([2, 3, 5, 7, 10, 20, 30], [two, three, five, seven, ten, twenty, thirty])
    plt.plot([2, 3, 5, 7, 10, 20, 30], [two, three, five, seven, ten, twenty, thirty], 'ro')
    plt.axis([0, 32, floor(three), 3.25])
    plt.ylabel("U.S. Treasury Bond's Yields to Maturity")
    plt.xlabel("U.S. Treasury Bonds' Times to Maturity (years)")
    plt.show()
#=======================================================================
def fred():
    data = requests.get('https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yield')

    soup = BeautifulSoup(data.text, 'html.parser')

    d = soup.find(class_='t-chart')

    #print(d)
    print(d.prettify())
#=======================================================================
def los():
    print('''
List of Popular Stocks:
AAPL - Apple
GOOGL - Google
TSLA - Tesla
SBUX - Starbucks
AMZN - Amazon
DIS - The Walt Disney Company
T - AT&T
VZ - Verizon
TMUS - T-Mobile
NFLX - Netflix
MSFT - Microsoft
    ''')
#=====================================================
def summary():
    current = dt.datetime.now()

    ticker = input('Ticker symbol:  ')
    ticker = ticker.upper()

    style.use = 'ggplot'
    if current.month == 1:
        start = dt.datetime(current.year - 1, current.month, current.day)
        end = dt.datetime(current.year, current.month, current.day)
    else:
        start = dt.datetime(current.year, current.month - 6, current.day)
        end = dt.datetime(current.year, current.month, current.day)
    t = web.DataReader(ticker, 'yahoo', start, end)
    print('')
    print('Getting data for ticker symbol "' + ticker + '"...')
    print(ticker)
    print(t)
    graph = input("Press 'g' to graph / Press 'c' to compare with another stock / Press any key to continue")
    for i in graph:
        if i == 'g':
            t['Adj Close'].plot(label = str(ticker), figsize=(16, 8), title = str(ticker))
            #plt.finance.candlestick2_ochl(ax, t['Open'], t['Close'], t['High'], t['Low'], width=4, colorup='k', colordown='r', alpha=0.75)
            plt.ylabel("Price ($)")
            plt.legend();
            plt.show()
        elif i == 'c':
            current = dt.datetime.now()

            cticker = input('Ticker symbol:  ')
            cticker = cticker.upper()

            style.use = 'ggplot'
            if current.month == 1:
                start = dt.datetime(current.year - 1, current.month, current.day)
                end = dt.datetime(current.year, current.month, current.day)
            else:
                start = dt.datetime(current.year, current.month - 6, current.day)
                end = dt.datetime(current.year, current.month, current.day)
            compare = web.DataReader(cticker, 'yahoo', start, end)

            t['Adj Close'].plot(label = str(ticker), figsize=(16, 8), title = str(ticker + " / " + cticker))
            compare['Adj Close'].plot(label = str(cticker))
            plt.ylabel("Price ($)")
            plt.legend();
            plt.show()

#=====================================================
def debug():
    current = dt.datetime.now()

    currentdate = "{}/{}/{}".format(current.year, current.month, current.day)

    print(currentdate)
#=========================PFP==========================
def pfp():
    run = input('''Enter command: ''')
    for i in run:
        if i == 't':
            summary()
            print('')
            pfp()
        elif i == 'l':
            los()
            pfp()
        elif i == 'f':
            fred()
            pfp()
        elif i == 'y':
            yield_curve()
            pfp()
        elif i == 'q':
            quit()
        elif i == 'd':
            print('Debugging...')
            debug()
            pfp()
        elif i == 'h'or i == 'help':
            help()
            pfp()
        else:
            print('Did not understand. Please try again.')
            pfp()
help()
pfp()
