import time
from datetime import date
from yahoo_fin import stock_info as si
import datetime
from ib_insync import *
import calendar
import requests

ib = IB()  
ib.connect('127.0.0.1', 7496, clientId=1)
nflx_contract = Option('spy', 20220408, 448, 'C', 'SMART')
data = ib.reqMktData(nflx_contract)

ib.sleep(0.5)
print(data.last)
# key = 'x4lRSvZy2P23SyFZjHUGELtPA8NySeHEXqNaSUVJXjAKMQtUzsLpOpfS6I8I'


# if date.today().weekday()<5:
#     date1 = 4-date.today().weekday()
#     strikedateforIB = (datetime.date.today() + datetime.timedelta(days=date1)).strftime("%Y%m%d")
#     test = []
#     datee = ['%Y','%m','%d']
#     for i in datee:
#         test.append(int((date.today() + datetime.timedelta(days=date1)).strftime(i)))
#     d=datetime.datetime(test[0], test[1], test[2], 0, 0)
#     strikedate= ( calendar.timegm(d.timetuple()) )

# ticker = []
# while True:
#     for i in range(1):
#         row = []
#         for j in range(1):
#             row.append(str(input('Enter your ticker name: ')))
#             row.append(float(input('Enter your call price target: ')))
#             row.append(float(input('Enter your put price target: ')))
#             row.append(float(input('Enter your call strike price: ')))
#             row.append(float(input('Enter your put strike price: ')))
#             row.append(float(input('Enter your contract quantity: ')))
#         ticker.append(row)    
#     userprompt = input('would you like to add more targets today?')
#     if userprompt in ("No","no","nope"):

#         break
# print(ticker)



# while True:
#     for x in ticker:
#         stockprice =round(si.get_live_price(x[0]),2)
#         print(stockprice, '- ', (x[0]))
# #CALL CONTRACT
#         if stockprice > x[1]:
#             #Get options price price-----------
#             url = 'https://mboum.com/api/v1/op/option/?symbol={symbol}&expiration={strikedate}&apikey={key}'.format(strikedate=strikedate, key=key,symbol=x[0] )
#             response = requests.get(url)
#             test = response.json()
#             api = (test['data']['optionChain']['result'][0]['options'][0]['calls'])
#             for apicall in api:
#                 if apicall["strike"] == x[3]:
#                     orderprice= round((apicall['ask']+apicall['bid'])/2+0.05,2)
#                     print(orderprice)
#             #execute order
#             callcontract = Option(x[0], strikedateforIB, x[3], 'C', 'SMART')
#             ib.qualifyContracts(callcontract)
#             print(x) 
#             print(stockprice)
#             order = ib.bracketOrder('BUY', x[5], orderprice, round(orderprice+(orderprice*20/100),2), round(orderprice-(orderprice*30/100),2))
            
#             for o in order:
#                  ib.placeOrder(callcontract, o)   
#             ib.sleep(1)
#             ticker.remove(x)
#             break
# #PUTS CONTRACT
#         if stockprice < x[2]:

#             #Get options price price-----------
#             url = 'https://mboum.com/api/v1/op/option/?symbol={symbol}&expiration={strikedate}&apikey={key}'.format(strikedate=strikedate, key=key,symbol=x[0] )
#             response = requests.get(url)
#             test = response.json()
#             api = (test['data']['optionChain']['result'][0]['options'][0]['puts'])
#             for apicall in api:
#                 if apicall["strike"] == x[4]:
#                     print(apicall['bid'])
#                     orderprice= round((apicall['ask']+apicall['bid'])/2,2)
#                     print(orderprice)
#             #execute order
#             putcontract = Option(x[0], strikedateforIB, x[4], 'P', 'SMART')
    
#             print(x) 
#             print(stockprice)
#             order = ib.bracketOrder('BUY', x[5], orderprice, round(orderprice+(orderprice*20/100),2), round(orderprice-(orderprice*30/100),2))
#             for o in order:
#                  ib.placeOrder(putcontract, o)   
            
#             ib.sleep(1)
#             ticker.remove(x)
#             break
#         time.sleep(2)
#     if not ticker:
#         print('all triggered')
#         break
# ib.disconnect()