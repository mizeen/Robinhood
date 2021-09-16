import yfinance as yf
import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt
import pickle
import datetime

df =pd.read_csv("Rhood_history_final.csv")
df=pd.DataFrame(df)
a=[]



e=open('rhood_dt_dict.pkl', "rb")
f=open('rhood_ticker_dict.pkl', "rb")
g=open('rhood_st_dict.pkl', "rb")
h=open('rhood_share_dict.pkl', "rb")

dt_dict=pickle.load(e) # date of trade
ticker_dict=pickle.load(f) # ticker name and ticker
st_dict=pickle.load(g) # Price per trade
share_dict=pickle.load(h) # number of share per trade

# print(df["Date"].max)
# print(df["Date"].min)


start_date="2020-03-16"
end_date="2021-09-01"
pfizer=yf.Ticker('PFE')
pfe_hist=pfizer.history(start=start_date, end=end_date)
print(pfe_hist)
print(pfe_hist["Close"])

from datetime import date, timedelta

sdate = date(2020,3,16)   # start date
edate = date(2021,9,1)   # end date

delta = edate - sdate       # as timedelta

all_date=[]

for i in range(delta.days + 1):
    day = sdate + timedelta(days=i)
    all_date.append(str(day))
all_stock_history=[]
all_stock_history=pd.DataFrame(all_stock_history)
# all_stock_history["Dates"]=all_date
a=[]
for key in ticker_dict:
	if ticker_dict[key] in ["--", "PS", "CZZ",'TRNE','GMHI','FMCI','IPOC','MYL','LGF','TLRD']:
		# print(ticker_dict[key])
		a.append(ticker_dict[key])
		pass
	else:
		a.append(ticker_dict[key])

		x= yf.Ticker(ticker_dict[key])
		x_hist=x.history(start=start_date,end=end_date)
		# print(ticker_dict[key])
		y=x_hist["Close"]
		y=pd.DataFrame(y)
		all_stock_history[ticker_dict[key]]=y
all_stock_history.to_csv('C:\\Users\\mizan\\Documents\\MIT Courses\\Rhood_all_stock_history.csv')

a=pd.DataFrame(a)
print(a.info())
a.to_csv('C:\\Users\\mizan\\Documents\\MIT Courses\\test_list.csv')

df2=df["Date"]
df2=pd.DataFrame(df2)
for key in ticker_dict:
	df2[ticker_dict[key]]=None
df2["Total"]= None
share_tracking_dict={}
for key in ticker_dict:
	share_tracking_dict[ticker_dict[key]]=0
# share_history_dict=
# for key in ticker_dict:


# print(share_tracking_dict)

master_total=0
# for ind in df.index:
# 	if df['B,S,D,O'][ind]=='Deposit':



# print(df2)
df2.to_csv('C:\\Users\\mizan\\Documents\\MIT Courses\\Rhood_history_master.csv')



# print(dt_dict)
# print(st_dict)





