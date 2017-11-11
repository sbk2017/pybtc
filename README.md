# pybtc

This a simple script where you can get the price of most crypto currencies like BTC, ETH, LTC ..etc

## How to use :

```python

import pybtc
price = pybtc.Get_Price('BTC') # to get Bitcoin current price in USD
print(price)
```
for EURO 
```python

price = pybtc.Get_Price('BTC',currency='EUR')
```
additional option if you want full detail of the current price

```python

price = pybtcGet_Price('BTC',full=1)

```
This will give you (PRICE,OPEN24HOUR,HIGH24HOUR,CHANGE24HOUR, LASTUPDATE,CHANGEPCT24HOUR)

## History of Currency

if you want the history of a curreny price ( hours or days)

```python

hprice_days = pybtc.HistoryPriceDays('BTC',60) # this will give the price details for the last 60 days 
print(hprice_days) 

>>> [{'time': 1505174400, 'low': 4074.97, 'volumeto': 453402207.42, 'volumefrom': 107041.94, 'high': 4387.76, 'close': 4158.92, 'open': 4217.9} .....
```
This will give you data for the last 60 days

to get the every hour 
```python

hprice_hrs = pybtc.HistoryPriceHrs('BTC',12) # this will give the price details for the last 12 hrs 
print(hprice_hrs) 

>>> [{'time': 1505174400, 'low': 4074.97, 'volumeto': 453402207.42, 'volumefrom': 107041.94, 'high': 4387.76, 'close': 4158.92, 'open': 4217.9} .....
```


