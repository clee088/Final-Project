import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
#============================PFP_COMMANDS============================
def help():
    print('''
Press t for a summary of a ticker symbol
Press y for a graph of the current yield Curve
Press h for a list of commands
Press q to quit
''')
def quit():
    check = input('Are you sure you want to quit? y/n ')
    if check == 'y':
        print('Quitting...')
    elif check == 'n':
        pfp()
    else:
        print('Did not understand. Please try again')
        quit()
#=======================================================================
def yield_curve():
    onemonth = 2.37
    twomonth = 2.42
    threemonth = 2.42
    sixmonth = 2.58
    one = 2.71
    two = 2.80
    three = 2.81
    five = 2.79
    seven = 2.84
    ten = 2.91
    twenty = 3.05
    thirty = 3.16
    plt.plot([2, 3, 5, 7, 10, 20, 30], [two, three, five, seven, ten, twenty, thirty])
    plt.plot([2, 3, 5, 7, 10, 20, 30], [two, three, five, seven, ten, twenty, thirty], 'ro')
    plt.axis([0, 32, 2.6, 3.25])
    plt.ylabel("U.S. Treasury Bond's Yields to Maturity")
    plt.xlabel("U.S. Treasury Bonds' Times to Maturity (years)")
    plt.show()

def summary():
    current = dt.datetime.now()

    ticker = input('Ticker symbol:  ')
    ticker = ticker.upper()

    style.use = 'ggplot'
    start = dt.datetime(current.year, current.month - 1, current.day)
    end = dt.datetime(current.year, current.month, current.day)

    df = web.DataReader(ticker, 'yahoo', start, end)
    print('')
    print('Getting data for ticker symbol "' + ticker + '"...')
    print(ticker)
    print(df)

def pfp():
    run = input('''Enter command: ''')
    for i in run:
        if i == 't':
            summary()
            print('')
            pfp()
        elif i == 'y':
            yield_curve()
            pfp()
        elif i == 'q':
            quit()
        elif i == 'd':
            print('Debugging')
        elif i == 'h':
            help()
            pfp()
        else:
            print('Did not understand. Please try again.')
            pfp()
help()
pfp()
