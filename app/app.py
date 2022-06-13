# reading a second row in csv
import csv
noise_amp=[]         #an empty list to store the second column
with open('500.csv', 'r') as rf:
    reader = csv.reader(rf, delimiter=',')
    for row in reader:
        noise_amp.append(row[1]) # which row we need to read , 1 is frist row , 2 is second row
    print(noise_amp)

list = noise_amp[301:500]
print(list)

# Define the ticker list
import pandas as pd
import yfinance as yf
#list = ['']
for i in list:
  tickers_list = [i]

# Fetch the data
  #import yfinance as yf
  name = yf.download(tickers_list,'2015-1-1')
#data = yf.download(tickers_list,'2015-1-1')
  name.to_csv('{stock}.csv'.format(stock = i))
# Print first 5 rows of the data
  print(name.head())
#print(data.head())