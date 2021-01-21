from sklearn.linear_model import LinearRegression
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot  as plt
import pandas as pd
import html5lib
import sqlite3



class TradeBot:
    def getsensexdata(self):
        """
        this is a functions to get live sensex data it will give you sensex data        
        """
        try:
            r = requests.get("https://www.google.com/search?q=live+sensex+today&oq=live+sensex&aqs=chrome.0.69i59j69i57j0j69i60l3.2776j1j7&sourceid=chrome&ie=UTF-8")
            soup = BeautifulSoup(r.text, "html.parser")
            print(soup.find_all("div")[95].get_text())
            print(soup.find_all("div")[102].get_text())
        
        except Exception as e:
            print("check internet connection")

    def getstockdata(self):
        """
        this is function to get live stock data
        """
        try:
            r = requests.get("https://www.google.com/search?q=live+stock&oq=live+stock+&aqs=chrome..69i57j0i20i131i263i433j0i131i433j0i433j0j0i20i263j0i395i433j0i395j0i131i395i433j0i395.4629j1j7&sourceid=chrome&ie=UTF-8")
            soup = BeautifulSoup(r.text, "html.parser")
            s = soup.find_all("div")[45].get_text()
            print(s)
        
        except Exception as e:
            print("check internet connection")

    def getgrowthrate(self):
        """
        get live growth rate
        """
        try:
            r = requests.get("https://www.google.com/search?sxsrf=ALeKk03nOsnG7krHBxKP1FQtR348S0d1Gg%3A1611213069713&ei=DSkJYLLvKtud4-EPqIS9kAs&q=live+growth+rate+of+india&oq=live+growth+&gs_lcp=CgZwc3ktYWIQARgBMgIIADIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yCAgAEBYQChAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeOgcIIxDqAhAnOgQIIxAnOgQIABBDOgcIABCxAxBDOgcIABAUEIcCOgUIABCxAzoFCAAQyQM6BQgAEJIDOggIABCxAxCDAToNCAAQsQMQgwEQFBCHAjoECAAQCjoICC4QxwEQrwE6BAgAEA06BggAEA0QHjoICAAQDRAFEB5QsJkFWI_dBWDy6AVoB3ABeACAAf8CiAHeGZIBCDAuMTEuNC4xmAEAoAEBqgEHZ3dzLXdperABCsABAQ&sclient=psy-ab")
            soup = BeautifulSoup(r.text, "html.parser")
            s = soup.find_all("div")[30].get_text()
            print(s)
        
        except Exception as e:
            print("check internet connection")
    
    def getgoldprice(self):
        """
        get gold price
        """
        try:
            r = requests.get("https://www.google.com/search?sxsrf=ALeKk01ZUCf3TiZ2owI69Ae4X3CKT4Q3Vw%3A1611213464092&ei=mCoJYL6RBfCF4-EP84GP2As&q=live+international+gold+price&oq=live+international&gs_lcp=CgZwc3ktYWIQARgAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADoHCCMQ6gIQJzoHCCMQJxCdAjoECCMQJzoECAAQQzoTCC4QsQMQgwEQxwEQowIQFBCHAjoFCAAQsQM6BwgAELEDEEM6DAgjECcQnQIQRhD6AToHCAAQyQMQQzoFCAAQkgM6CAgAELEDEIMBOgsIABCxAxCDARCRAjoFCAAQkQI6CggAELEDEBQQhwI6BAgAEAM6BwgAEBQQhwI6BggAEBYQHjoICAAQFhAKEB5QrBVYvFlg_WpoAnABeAGAAdUDiAGSHpIBCjAuMTMuNS4wLjGYAQCgAQGqAQdnd3Mtd2l6sAEKwAEB&sclient=psy-ab")
            soup = BeautifulSoup(r.text, "html.parser")
            s = soup.find_all("div")[30].get_text()
            print(s)
        
        except Exception as e:
            print("check internet connection")

while True:
    bot = TradeBot()
    query = input(">>>")
    if 'gold price' in query:
        bot.getgoldprice()
    
    elif 'sensex' in query:
        bot.getsensexdata()
    
    elif 'growth rate' in query:
        bot.getgrowthrate()
    
    elif 'stock' in query:
        bot.getstockdata()
    


    



