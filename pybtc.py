#!/usr/bin/python

from datetime import datetime
import json
from urllib.request import urlopen



cryptoall = 'BTC,ETH,LTC'


def Get_Price(crypto=cryptoall,full=0,currency='USD'):
    ''' Provide the PRICE,OPEN24HOUR,HIGH24HOUR,CHANGE24HOUR, LASTUPDATE,CHANGEPCT24HOUR
    of one crypto currency '''

    url = ('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=%s&tsyms=%s'
    % (crypto, currency))
    data = urlopen(url)
    data = data.read().decode('utf8')
    rawdata = json.loads(data)['RAW']
    cur = rawdata[crypto][currency]
    price = cur['PRICE']
    open24hr = cur['OPEN24HOUR']
    high24hr = cur['HIGH24HOUR']
    change24hr = cur['CHANGE24HOUR']
    lastupdate =datetime.fromtimestamp(cur['LASTUPDATE']).strftime('%c')
    changepct = cur['CHANGEPCT24HOUR']
    if full == 1:
        return price, open24hr, high24hr,change24hr,lastupdate,changepct
    else:
        return price

def HistoryPriceDays(crypto,days=60):
    '''Get the historical data of a currency default 60 days'''
    url=('https://min-api.cryptocompare.com/data/histoday?fsym=%s&tsym=USD&limit=%d'%(crypto,days))
    data = urlopen(url)
    data = data.read().decode('utf8')
    raw_data = json.loads(data)['Data']
    return raw_data

def HistoryPriceHrs(crypto,hrs=12):
    ''' get the price for the last 12 hrs'''
    url=('https://min-api.cryptocompare.com/data/histohour?fsym=%s&tsym=USD&limit=%d'%(crypto,hrs))
    data = urlopen(url)
    data = data.read().decode('utf8')
    raw_data = json.loads(data)['Data']
    return raw_data

def main():
    pass


if __name__ == '__main__':
    main()

