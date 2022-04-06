import time
from datetime import date
from yahoo_fin import stock_info as si
import datetime
from ib_insync import *
import calendar
import requests

ib = IB()  
ib.connect('127.0.0.1', 7496, clientId=1)

if date.today().weekday()<5:
    date1 = 4-date.today().weekday()
    strikedateforIB = (datetime.date.today() + datetime.timedelta(days=date1)).strftime("%Y%m%d")

ticker = []
while True:
    for i in range(1):
        row = []
        for j in range(1):
            row.append(str(input('Enter your ticker name: ')))
            row.append(float(input('Enter your call price target: ')))
            row.append(float(input('Enter your put price target: ')))
            row.append(float(input('Enter your call strike price: ')))
            row.append(float(input('Enter your put strike price: ')))
            row.append(float(input('Enter your contract quantity: ')))
        ticker.append(row)    
    userprompt = input('would you like to add more targets today?')
    if userprompt in ("No","no","nope"):

        break
print(ticker)

while True:
    for x in ticker:
        stockprice =round(si.get_live_price(x[0]),2)
        print(stockprice, '- ', (x[0]))
#CALL CONTRACT
        if stockprice > x[1]:
            #Get options price price----------
            #execute order
            callcontract = Option(x[0], strikedateforIB, x[3], 'C', 'SMART')
            ib.qualifyContracts(callcontract)
            data = ib.reqMktData(callcontract)
            ib.sleep(1)
            orderprice = data.last
            order = ib.bracketOrder('BUY', x[5], orderprice, round(orderprice+(orderprice*20/100),2), round(orderprice-(orderprice*30/100),2))
            
            for o in order:
                 ib.placeOrder(callcontract, o)   
            ib.sleep(1)
            ticker.remove(x)
            break
#PUTS CONTRACT
        if stockprice < x[2]:
            #Get options price price----------
            #execute order
            putcontract = Option(x[0], strikedateforIB, x[4], 'P', 'SMART')
            ib.qualifyContracts(putcontract)
            data = ib.reqMktData(putcontract)
            ib.sleep(1)
            orderprice = data.last
            order = ib.bracketOrder('BUY', x[5], orderprice, round(orderprice+(orderprice*20/100),2), round(orderprice-(orderprice*30/100),2))
            
            for o in order:
                 ib.placeOrder(putcontract, o)   
            ib.sleep(1)
            ticker.remove(x)
            break
        time.sleep(2)
    if not ticker:
        print('all triggered')
        break
ib.disconnect()