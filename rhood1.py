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
		df["Stock Name"][ind]=df["Type"][ind][:y]
		df["B,S,D,O"][ind]="Sell"
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

		df["Total for Shares"][ind]=a[:z+2]


		# print(x,y,z)
		if x != -1:
			df["Stock Name"][ind]=df["Stock Name"][ind][:x]

		elif y != -1:
			df["Stock Name"][ind]=df["Stock Name"][ind][:y]
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



plt.figure(figsize=(9, 3))
plt.subplot(131)
plt.scatter(dt, total)
plt.subplot(132)
plt.scatter(dt, amount)

plt.suptitle('Categorical Plotting')
plt.show()

print("done")


# import matplotlib.dates as mdates

df.to_csv('C:\\Users\\mizan\\Documents\\MIT Courses\\Rhood_history_final.csv')
