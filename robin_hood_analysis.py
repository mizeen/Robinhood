import pandas as pd
import yfinance as yf 
import matplotlib.pyplot as plt
import numpy as np
import pickle

df =pd.read_csv("Rhood_official.csv")
df=pd.DataFrame(df)
df['Activity Date']=pd.to_datetime(df['Activity Date'],errors='coerce')
df2=df.copy(deep=True)
df2['Quantity']=pd.to_numeric(df2['Quantity'], errors='coerce')
df2['Activity Date']=pd.to_datetime(df2['Activity Date'],errors='coerce')
df2 = df2.replace(np.nan, 0, regex=True)
ticker=df.Instrument.unique()


# data=yf.download(ticker_list,start="2020-03-01", end="2021-09-15",group_by='tickers' )
# # print(data)
# ticker_data=pd.DataFrame(data)
# ticker_data.to_csv('C:\\Users\\mizan\\Documents\\MIT Courses\\Rhood_ticker_history.csv', index=True)

ticker_data=pd.read_csv("Rhood_ticker_history.csv")
ticker_data=pd.DataFrame(ticker_data)
ticker_data.rename(columns={ ticker_data.columns[0]: "Date" }, inplace = True)
ticker_data['Date'] =pd.to_datetime( ticker_data['Date'], errors='coerce')

# a=ticker_data.iloc[:,1]
# ticker_data.set_index()
# # print(a)
# ticker_data.to_csv('C:\\Users\\mizan\\Documents\\MIT Courses\\Rhood_ticker_history2.csv', index=True)



# loading data from previous session's pickled data

e=open('ticker_value_dict.pkl', "rb")
f=open('ticker_date_dict.pkl', "rb")
g=open('ticker_share_dict.pkl', "rb")
h=open('ticker_dict.pkl', "rb")

ticker_value_dict=pickle.load(e)
ticker_date_dict=pickle.load(f)
total_share_dict=pickle.load(g)
ticker_dict= pickle.load(h)

# ticker_dict={} #individual trade
# total_share_dict={}  # cumulative trade amount
# ticker_date_dict={} #date of trade
# ticker_value_dict={} #value of the stock 



# for x in ticker:
# 	ticker_dict[x]=[]
# 	ticker_date_dict[x]=[]
# 	ticker_value_dict[x]=[]
# df2=df2[::-1]
# for ind in df2.index:
# 	if ((df2['Trans Code'][ind] == 'BUY') or (df2['Trans Code'][ind]=='SELL')):
# 		ticker_dict[df2['Instrument'][ind]].append(df2['Quantity'][ind])
# 		ticker_date_dict[df2['Instrument'][ind]].append(df2['Activity Date'][ind])
# for stock in ticker_date_dict:
# 	for date in ticker_date_dict[stock]:
# 		ticker_value_dict[stock].append(ticker_data.loc[ticker_data['Date'] == date, [stock]])

# def sum_matrix(x):
# 	y=x[:]
# 	total=0
# 	for i in range(len(x)):
# 		total=total+x[i]
# 		y[i]=total

# 	return y
# for stock in ticker_dict:
# 	total_share_dict[stock]=sum_matrix(ticker_dict[stock])


# #Pickling data so we don't have to generate it every time
# e=open('ticker_value_dict.pkl', "wb")
# f=open('ticker_date_dict.pkl', "wb")
# g=open('ticker_share_dict.pkl', "wb")
# h=open('ticker_dict.pkl', "wb")

# pickle.dump(ticker_value_dict,e)
# pickle.dump(ticker_date_dict,f)
# pickle.dump(total_share_dict,g)
# pickle.dump(ticker_dict,h)


# e.close()
# f.close()
# g.close()
# h.close()



# plug_shares=ticker_dict['DOW']
# print(plug_shares)
# plug_date=ticker_date_dict['DOW']

# fig=plt.figure(1)
# plt.plot(plug_date,plug_shares)
# fig2=plt.figure(2)

# plug_total=total_share_dict['DOW']

# plt.plot(plug_date,plug_total)
# plt.show()

# # plug_values= ticker_value_dict['PLUG']
# # plug_values=pd.DataFrame(plug_values)
# print((plug_values))
# print('ticker value', ticker_value_dict['PLUG'])
# print(ticker_value_dict)




# print(ticker_dict['PLUG'])
# print(ticker_date_dict['PLUG'])
# print(total_share_dict['PLUG'])
# plug_shares=ticker_dict['ICAGY']
# plug_dates=ticker_date_dict['ICAGY']
# plug_shares_total=total_share_dict['ICAGY']
# fig2=plt.figure(2,figsize=(5,5))
# plt.plot(plug_dates,plug_shares_total)
# plt.xticks(rotation=45)

def plot_stock(ticker):
	plug_shares=ticker_dict[ticker]
	plug_dates=ticker_date_dict[ticker]
	plug_shares_total=total_share_dict[ticker]
	fig4=plt.figure(4,figsize=(10,10))
	plt.plot(plug_dates,plug_shares)
	plt.title(ticker + " Shares")
	fig5=plt.figure(5,figsize=(10,10))
	plt.plot(plug_dates,plug_shares_total)
	plt.title(ticker + " total")
	plt.show()

print(ticker)
test_stock=input('Put the ticker')
plot_stock(test_stock)






# deposit_withdrawl=df[df['Trans Code']=='ACH']

# deposit_withdrawl =pd.DataFrame(deposit_withdrawl)

# # # deposit_withdrawl.to_csv('C:\\Users\\mizan\\Documents\\MIT Courses\\Rhood_Deposit_history.csv', index=False)

# # '''Plotting deposit and withdrawl history'''
# def to_money(x):

# 	if x[0]=='$':
# 		x=x[1:]
# 		x=float(x)
# 	else:
# 		x=x[2:-1]
# 		x=float(x)
# 	return x

# x_date=deposit_withdrawl[['Activity Date']].copy(deep = True)
# x_date.reset_index(drop=True, inplace=True)


# y_amount=deposit_withdrawl[['Amount']].copy(deep=True)
# y_amount.reset_index(drop=True, inplace=True)



# for ind in y_amount.index:
# 	# print(y_amount['Amount'][ind])
# 	neg=False
# 	if y_amount['Amount'][ind].find('(') != -1:
# 		y_amount['Amount'][ind]=y_amount['Amount'][ind].strip('()')
# 		neg=True
# 	y_amount['Amount'][ind]=y_amount['Amount'][ind].strip('$')
# 	y_amount['Amount'][ind]=y_amount['Amount'][ind].replace(',','')
# 	y_amount['Amount'][ind]=float(y_amount['Amount'][ind])
# 	if neg:
# 		y_amount['Amount'][ind]=y_amount['Amount'][ind]*-1



# x_date=x_date[::-1]
# y_amount=y_amount[::-1]
# y_amount.reset_index(drop=True, inplace=True)
# x_date.reset_index(drop=True, inplace=True)
# y_amount['Cumulative']=None
# y=0
# for ind in y_amount.index:
# 	y=y+y_amount['Amount'][ind]
# 	y_amount['Cumulative'][ind]=y
# plt.rcParams.update({'font.size': 12})
# fig=plt.figure(6, figsize=(10,5))
# plt.plot(x_date['Activity Date'],y_amount['Cumulative'], marker ='o', alpha=.8, label='Amount Invested')
# plt.legend(loc='best')
# plt.title("Mizanur's Investment History")
# plt.xlabel('Dates', loc='center')
# plt.ylabel('Dollar Amount')
# plt.xticks(rotation=90)
# plt.show()





# 



