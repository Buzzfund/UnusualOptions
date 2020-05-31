#usage: py <this.py> [-v]
#where adding -v makes it print out all the options that had weird v/oi
#...actually, literally ANYTHING makes it do that, not just -v

#REMEMBER THE HFC DISCREPANCY
#takes like...a minute to run
import sys
import requests
import time
from datetime import datetime, timedelta
import datetime
#from yahoo_earnings_calendar import YahooEarningsCalendar

inp = False     #gonna be used for -v flag
try:
    inp = sys.argv[1]
    inp = True
except:
    pass

apikey = ""

if(apikey==""):
    print("bro cmon input ur api key (line 23)")
    exit()

stocks = ["AAN","AAP","AAXN","ABT","ACM","ADBE","AIG","AKAM","ALB","ALXN","AMAT","AMTD","ANET","ANIK","ANTM","APPN","ARCH",
          "ARMK","ARWR","ASHR","ATH","ATRC","ATUS","ATVI","AVGO","AVLR","AXP","AYX","AZN","BAM","BBY","BC","BFYT","BG","BHVN",
          "BIDU","BILI","BILL","BKLN","BLUE","BP","BRK/B","BSX","BUD","BURL","BX","CAH","CAKE","CARG","CAT","CB","CBRL","CDAY",
          "CHGG","CHRW","CHWY","CI","CL","CMCSA","COP","COST","COUP","CREE","CRM","CRWD","CSOD","CSX","CTSH","CTVA","CTXS",
          "CVLT","CVNA","CVS","CVX","CYBR","DBX","DD","DDOG","DDS","DFS","DGX","DHI","DHR","DIN","DISH","DKNG","DOCU",
          "DOW","DOX","DOUK","DUST","EA","EAT","EBAY","EMB","EMN","ENPH","EOG","ERI","ESTC","ETSY","EXAS","EXC","EXEL","EXPE",
          "EYE","FAZ","FB","FDX","FE","FISV","FLIR","FLT","FND","FNV","FSCT","FSLR","FSLY","FTNT","FVRR","GD","GDXJ",
          "GILD","GIS","GLD","GO","GOLD","GRMN","GRUB","GS","GSK","GSX","HD","HDS","HES","HFC","HLF","HLT","HMC","HOG","HON",
          "HRL","HSBC","HSY","IAC","IBM","IIVI","IMMU","IOVA","IRBT","JD","JNJ","JNPR","K","KHC","KKR","KL","KMB","KMT","KNX",
          "KO","KR","KWEB","LBTYK","LEA","LEG","LEN","LITE","LLY","LM","LMT","LNC","LOGI","LOGM","LOW","LRCX","LULU",
          "LVGO","LVS","LYFT","LYV","MA","MAR","MCD","MDLA","MDT","MET","MGNX","MIDD","MKC","MMM","MMSI","MO","MPC","MRK",
          "MRTX","MRVL","MS","MSI","MTCH","MTSI","NEE","NEM","NEP","NET","NFLX","NKE","NLOK","NOC","NOW","NTAP","NTNX","NUGT",
          "NVDA","NVS","NXPI","NXST","OIH","OKTA","OLED","OLLI","ORCL","OTIS","OZK","PAGS","PAYC","PCTY","PD","PDD","PEP",
          "PFSI","PG","PHM","PLNT","PM","PNC","PPD","PPL","PRAA","PRU","PSX","PVH","PYPL","QCOM","QGEN","QLYS","QRVO","QSR",
          "RCII","RCUS","RDFN","RDS/A","RDS/B","RH","RIO","RL","RNG","RTX","SAIL","SBUX","SCHW","SDGR","SE","SFM","SHAK",
          "SIX","SKY","SMAR","SMH","SO","SPG","SPR","SSNC","STMP","STX","STZ","SWKS","SYY","TAP","TCO","TCOM","TDG","TDOC",
          "TEAM","TER","TGT","THO","TIF","TJX","TMUS","TOL","TSEM","TSM","TSN","TTD","TTWO","TWOU","TXN","TXRH","TXT","UDOW",
          "UHS","UNH","USB","USO","UUP","V","VIRT","VLO","VMC","VNQ","VTR","VZ","W","WBA","WCC","WDAY","WDC","WELL","WEN","WIX",
          "WM","WMT","WPM","WRK","WYNN","XBI","XHB","XLNX","XPO","YELP","YETI","YNDX","YY","Z","ZEN","ZG","ZION","ZM","ZTO"]
stocks2 = ["AAN","AAP","AAXN"]
stocks3 = ["AAN","AAP","AAXN","ABT","ACM","ADBE","AIG","AKAM","ALB","ASHR"] #there are 10 in here
removed = ["DIA","EWJ","EWU","EWW","EWY","FAS","IBB","IEF","IGV","INDA","ITB","IWO","IYR","KRE","LQD","SDOW","SH","SVXY","SXPL",
			"TLT","UPRO","UVXY","XLB","XLC","XLI","XLK","XLP","XLU","XLV","XLY","XME","XOP","XRT"]

def ndays(N):    #gets date N days from now
    dnd = int(time.time()+N*60*60*24)
    return datetime.datetime.utcfromtimestamp(dnd).strftime('%Y-%m-%d')

def quote(symbol):
    endpoint = "https://api.tdameritrade.com/v1/marketdata/"+symbol+"/quotes"
    payload = {'apikey':apikey}
    content = requests.get(url=endpoint,params=payload)
    return content.json()

def price(symbol):
    return quote(symbol)[symbol]["lastPrice"]

def volume(symbol):
    return quote(symbol)[symbol]["totalVolume"]

def instrument(symbol):
    endpoint = "https://api.tdameritrade.com/v1/instruments"
    payload = {'apikey':apikey,
               'symbol':symbol,
               'projection':'symbol-search'
              }
    content = requests.get(url=endpoint,params=payload)
    return content.json()

def dte(symbol):    #days until earnings
    val = 0
    try:
        val = (yec.get_next_earnings_date(symbol)-time.time())/(60*60*24)
    except:
        val = -5 #why not?
    return val

def getchain(symbol):    #gets chain given symbol
    endpoint = r"https://api.tdameritrade.com/v1/marketdata/chains"
    payload = {'apikey':apikey,
               'symbol':symbol,
               'range':'OTM',
               'strikeCount':10,
               'toDate':ndays(12),
               'fromDate':ndays(1)
              }
    content = requests.get(url=endpoint,params=payload)
    return content.json()



def criteria(symbol):
    q = quote(symbol)
    if(q[symbol]["lastPrice"]<20):
        return False
    if(q[symbol]["lastPrice"]>300):
        return False
    if(q[symbol]["totalVolume"]<1000000):
        return False
    if(q[symbol]["totalVolume"]>15000000):
        return False
    return True

def opts1(symbol,prin):        #given symbol, do blah blah blah unusual optionsd
    datum = getchain(symbol)
    ans = False
    #print(data["callExpDateMap"]["2020-05-08:0"]["100.0"][1]["totalVolume"])
    for s in datum:
        if type(datum[s]) is dict:
            for key in datum[s]:
                for key2 in datum[s][key]:
                    #for i in range(len(data[s][key][key2])+1)
                    #but i think len=1 always
                    tv = datum[s][key][key2][0]["totalVolume"]
                    oi = datum[s][key][key2][0]["openInterest"]
                    if(tv>500):
                        if((tv+1)/(oi+1)>10):
                            ans = True
                            if(prin):
                                print("TICKER: "+datum["symbol"])
                                print("EXPIRY: "+key.split(":",1)[0])
                                print("OPTION: "+s[:-10])
                                print("STRIKE: "+key2)
                                print("VOLUME: "+str(tv))
                                print("OPEN I: "+str(oi))
                                print("--------------------")
    return ans

start = time.time()
symbols = []
for i in stocks:
    if(criteria):
        if(opts1(i,inp)):
            symbols.append(i)

print(symbols)


