# Web scrape for insider trading, Finviz
# Script for data collection
# Felix Hu
################################################################

import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json
import pandas as pd

def getLatestInsiderTrading():
    req = Request("https://finviz.com/insidertrading.ashx", headers={'User-Agent': 'Mozilla/5.0'}) # disguise ourselves as a Mozilla browser
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    table = soup.find_all(lambda tag: tag.name=='table')
    rows = table[5].findAll(lambda tag: tag.name=='tr') # rows contains each row of the table row[1] row[2]...
    labels = [x.text for x in rows[0].find_all('td')] # table column names

    org = list()
    for i in range(1,len(rows)):
        out=[]
        td=rows[i].find_all('td')
        out=out+[x.text for x in td]
        org.append(out)

    df = pd.DataFrame(org, columns=labels)
    return df

def getTopInsiderTrading():
    req = Request("https://finviz.com/insidertrading.ashx?or=-10&tv=100000&tc=7&o=-transactionValue", headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    table = soup.find_all(lambda tag: tag.name=='table')
    rows = table[5].findAll(lambda tag: tag.name=='tr') # rows contains each row of the table row[1] row[2]...
    labels = [x.text for x in rows[0].find_all('td')] # table column names

    org = list()
    for i in range(1,len(rows)):
        out=[]
        td=rows[i].find_all('td')
        out=out+[x.text for x in td]
        org.append(out)

    df = pd.DataFrame(org, columns=labels)
    return df

def match_class(target):
    '''
    https://stackoverflow.com/questions/11331071/get-contents-by-class-names-using-beautiful-soup
    '''                                                     
    def do_match(tag):                                                          
        classes = tag.get('class', [])                                          
        return all(c in classes for c in target)                                
    return do_match  

def getInsiderTradingForTicker(ticker):
    req = Request("https://finviz.com/quote.ashx?t="+str(ticker), headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    table = soup.find_all(lambda tag: tag.name=='table')
    rows = table[9].findAll(lambda tag: tag.name=='tr')
    labels = [x.text for x in rows[0].find_all('td')] # table column names
    print(soup.find_all(match_class(["insider-buy-row-2"])))

getInsiderTradingForTicker("IMMU")