# import tabula
# tabula.environment_info()
# df = tabula.read_pdf('C:\\Users\\mizan\\Documents\\MIT Courses\\rhood_0721.pdf',pages = '3')
# print(df)

import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt

X =pd.read_csv("transactions.tsv",sep="\t")
df=pd.DataFrame(X)

# Cleaning up data

print(df.info())
df["Year"]=None
df["B,S,D,O"]=None
df["Stock Name"]=None
df["Float Total"]=None


print(df.columns)
for ind in df.index:
	if df['Date'][ind][-4:]== '2020':
		df["Year"][ind]=2020
	else:
		df["Year"][ind]=2021
	if df['Total'][ind]=='Canceled':
		df.drop([ind], inplace = True)
	elif df['Total'][ind]=='Placed':
		df.drop([ind], inplace = True)
	elif df['Total'][ind]=='Rejected':
		df.drop([ind], inplace = True)
for ind in df.index:
	z=df["Type"][ind].find('Dividend')
	x=df["Type"][ind].find('Buy')
	y=df["Type"][ind].find('Sell')

	a=df["Type"][ind].find('Deposit')
	b=df["Type"][ind].find('Withdrawal')
	c=df["Type"][ind].find('Placed')


	# print(x,y,z)
	if z != -1:
		df["Stock Name"][ind]=df["Type"][ind][:z]
		df["B,S,D,O"][ind]="Dividend"
	elif y != -1:
		df["Stock Name"][ind]=str(df["Type"][ind][:y])
		df["B,S,D,O"][ind]="Sell"
		if df["Stock Name"][ind]=="Plug Power":
			print("Fount it!!")
	elif x != -1:
		df["Stock Name"][ind]=df["Type"][ind][:x]
		df["B,S,D,O"][ind]="Buy"

	elif a != -1:
		df["Stock Name"][ind]="N/A"
		df["B,S,D,O"][ind]="Deposit"
	elif b != -1:
		df["Stock Name"][ind]="N/A"
		df["B,S,D,O"][ind]="Withdrawal"

	else:
		df["Stock Name"][ind]="Idk"
		df["B,S,D,O"][ind]="Idk"


for ind in df.index:
	if (df['B,S,D,O'][ind]== "Buy") or (df['B,S,D,O'][ind]== "Sell"):

		x=df["Stock Name"][ind].find('Market')
		y=df["Stock Name"][ind].find('Limit')
		a=str(df["Total for Shares"][ind])
		z=a.find('.')
		b=df["Stock Name"][ind].find('Stop Loss')
		c=df["Stock Name"][ind].find('Trailing')

		df["Total for Shares"][ind]=a[:z+3]


		# print(x,y,z)
		if x != -1:
			df["Stock Name"][ind]=df["Stock Name"][ind][:x-1]

		elif y != -1:
			df["Stock Name"][ind]=df["Stock Name"][ind][:y-1]
		elif b != -1:
			df["Stock Name"][ind]=df["Stock Name"][ind][:b-1]
		elif c!= -1:
			df["Stock Name"][ind]=df["Stock Name"][ind][:c-1]


	if (df['B,S,D,O'][ind]== "Dividend"):
		df["Total for Shares"][ind]=df["Total"][ind][:3]



for ind in df.index:
	if (df['B,S,D,O'][ind]== "Sell") or (df['B,S,D,O'][ind]== "Dividend") or (df['B,S,D,O'][ind]== "Buy"):
		a=df["Total for Shares"][ind][1:]

		if a.find(',')!=-1:
			a=a[:a.find(',')]+a[a.find(',')+1:]
		df["Float Total"][ind]=float(a)

total_earned=0.00
for ind in df.index:
	if (df['B,S,D,O'][ind]== "Sell") or (df['B,S,D,O'][ind]== "Dividend"):
		total_earned+= df["Float Total"][ind]
		# print("Positive: " , total_earned)
	elif (df['B,S,D,O'][ind]== "Buy"):
		total_earned-= df["Float Total"][ind]
		# print("negative: " , total_earned)
print("total earned: " , total_earned+9818.00)

for ind in df.index:
	if (df['B,S,D,O'][ind]== "Deposit"):
		a=str(df["Total"][ind][1:])
		if a.find(',')!=-1:
			a=a[:a.find(',')]+a[a.find(',')+1:]
		df["Total"][ind]=float(a)

	elif (df['B,S,D,O'][ind]== "Withdrawal"):
		a=str(df["Total"][ind][2:])
		if a.find(',')!=-1:
			a=a[:a.find(',')]+a[a.find(',')+1:]
		df["Total"][ind]=float(a)

# for ind in df.index:
# 	if ((df['B,S,D,O'][ind]== "Deposit") or (df['B,S,D,O'][ind]== "Withdrawal"))
# 		a=df["Tottal"][ind][1:]

# 		if a.find(',')!=-1:
# 			a=a[:a.find(',')]+a[a.find(',')+1:]
# 		df["Total"][ind]=float(a)




import datetime
print(df["Date"][7])
print(df["Date"][8])
print(df["Date"][9])
df["Date"][7]=df["Date"][11]
df["Date"][8]=df["Date"][11]
df["Date"][9]=df["Date"][11]

# for ind in df.index:
# 	a=str(df["Date"])
# 	print(a, ind)
# 	a=pd.to_datetime(a)
# 	df["Date"][ind]=a

# for ind in df.index:

# 	df["Date"][ind]=df["Date"][ind].to_datetime
print("Done")
total_earned=0.00
dt=[]
amount=[]
total=[]

df=df[::-1]
df2=df[:]
for ind in df.index:
	if (df['B,S,D,O'][ind]== "Deposit"): 
		total_earned+= df["Total"][ind]
		amount.append(df["Total"][ind])
		dt.append(df["Date"][ind])
		total.append(total_earned)
	elif (df['B,S,D,O'][ind]== "Withdrawal"):
		total_earned-= df["Total"][ind]
		amount.append(df["Total"][ind]*-1)
		dt.append(df["Date"][ind])
		total.append(total_earned)

		# print("Positive: " , total_earned)


print("total invested: " , total_earned)

print(len(dt), len(amount), len(total))

df["Shares"]=0.00

for ind in df.index:
	# print(ind, df["Price per share"][ind])
	if type(df["Price per share"][ind]) == type("hello"):

			a=(df["Price per share"][ind][1:])
			if a.find(",") != -1:
				a=a[:a.find(",")]+a[a.find(",")+1:]
				df["Shares"][ind]=df["Float Total"][ind]/float(a)
			else:
				df["Shares"][ind]=df["Float Total"][ind]/float(a)

			# print(ind,df["Float Total"][ind], float(a),'Ans: ', df["Float Total"][ind]/float(a)  )

		# a=float(df["Price per share"][ind])
		# a=float(a)


st_dict={}#price per trade
dt_dict={}#Date of trade
shares_dict={} # number of shares per trade
for ind in df.index:
	if df["B,S,D,O"][ind]=="Buy" :
		if df["Stock Name"][ind] in st_dict:
			st_dict[df["Stock Name"][ind]].append(df["Float Total"][ind]*-1)
			dt_dict[df["Stock Name"][ind]].append(df["Date"][ind])
			shares_dict[df["Stock Name"][ind]].append(df["Shares"][ind])
			
		
		else:
			
			st_dict[df["Stock Name"][ind]]=[df["Float Total"][ind]*-1]
			dt_dict[df["Stock Name"][ind]]=[df["Date"][ind]]
			shares_dict[df["Stock Name"][ind]]=[df["Shares"][ind]]

	elif df["B,S,D,O"][ind]=="Sell":
		if df["Stock Name"][ind] in st_dict:
			
			st_dict[df["Stock Name"][ind]].append(df["Float Total"][ind])
			dt_dict[df["Stock Name"][ind]].append(df["Date"][ind])
			shares_dict[df["Stock Name"][ind]].append(df["Shares"][ind]*-1)
		else:
			st_dict[df["Stock Name"][ind]]=[df["Float Total"][ind]]
			dt_dict[df["Stock Name"][ind]]=[df["Date"][ind]]
			shares_dict[df["Stock Name"][ind]]=[df["Shares"][ind]*-1]
x=0.00			
plug=[]
dt_plug=[]
for ind in df.index:
	if (df2['Stock Name'][ind]=="Plug Power") and (df2['B,S,D,O'][ind]=="Sell"):

		plug.append(x+df["Float Total"][ind])
		dt_plug.append(df2["Date"][ind])
	elif (df2['Stock Name'][ind]=="Plug Power") and (df2['B,S,D,O'][ind]=="Buy"):
		plug.append(x-df["Float Total"][ind])
		dt_plug.append(df2["Date"][ind])


	# print(df2["Stock Name"][ind])
plug[-1]=plug[-1]+188.16


print('plug',plug)
		



# plt.figure(figsize=(9, 3))
# plt.subplot(131)
# plt.scatter(dt, total)
# plt.subplot(132)



# plt.scatter(dt_dict['Coinbase'], st_dict['Coinbase'])
# plt.subplot(133)
# plt.scatter(dt_plug,plug)

# plt.suptitle('Categorical Plotting')
# plt.show()

print("done")
# print(plug)
print(df.info())
# print(st_dict.get('Plug Power'))
# print(st_dict)
print(shares_dict['Coinbase'])

df3 =pd.read_csv("Rhood_official.csv")
ticker_dict={}
for ind in df3.index:
	if df3["Description"][ind] in ticker_dict:
		ticker_dict[df3["Description"][ind]]=df3["Instrument"][ind]
	else:
		ticker_dict[df3["Description"][ind]]=df3["Instrument"][ind]
a={}
for key in ticker_dict:
	if ticker_dict[key] not in a:
		a[ticker_dict[key]] = key
	else:
		x=len(key)
		y=len(a[ticker_dict[key]])
		if x>y:
			pass
		else:
			a[ticker_dict[key]] = key

x=[]
y=[]
z=[]
z=pd.DataFrame(z)

for key in a:
	x.append(key)
	y.append(a[key])
b={}
for key in a:
	b[a[key]]=key
ticker_dict=b
z["stock"]=y
z["ticker"]=x

z.to_csv('C:\\Users\\mizan\\Documents\\MIT Courses\\test3.csv')




# print(ticker_dict)

df["Ticker"]='Idk'
ticker_dict["iShares Global Clean Energy ETF"]="ICLN"
ticker_dict["Best"]="BBY"
ticker_dict["VanEck Vectors Oil Services ETF"]="OIH"

for ind in df.index:
	if df["Stock Name"][ind] in ticker_dict:
		df["Ticker"][ind]=ticker_dict[df["Stock Name"][ind]]


		# print(df["Stock Name"][ind], ticker_dict[df["Stock Name"][ind]])

# import matplotlib.dates as mdates
# x=[]
# y=[]
# z=[]
# x=pd.DataFrame(x)
# b=[]
# for key in ticker_dict:
# 	a=(key.find('Div:') != -1)
# 	c= (key.find('Fee') != -1)
# 	d=(key.find('Tax') != -1)
# 	if a or c or d:
# 		b.append(key)
# for key in b:
# 	del ticker_dict[key]
# for key in ticker_dict:
# 	z.append(key)
# 	y.append(ticker_dict[key])
# x['Name']=z
# x['Ticker']=y
# x.to_csv('C:\\Users\\mizan\\Documents\\MIT Courses\\test2.csv')
print (ticker_dict["iShares Global Clean Energy ETF"])

df.to_csv('C:\\Users\\mizan\\Documents\\MIT Courses\\Rhood_history_final.csv')


# import yfinance as yf
import pickle



e=open('rhood_dt_dict.pkl', "wb")
f=open('rhood_ticker_dict.pkl', "wb")
g=open('rhood_st_dict.pkl', "wb")
h=open('rhood_share_dict.pkl', "wb")

pickle.dump(st_dict,g)
pickle.dump(dt_dict,e)
pickle.dump(ticker_dict,f)
pickle.dump(shares_dict,h)

e.close()
f.close()
g.close()
h.close()
print("Done")
