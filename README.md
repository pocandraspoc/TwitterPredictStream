# TwitterPredictStream

with "jsonWrapper.py" I have selected the non retweets from the downloaded data.  
With "list.py" I have merged the msg parts of the tweets into one bigger file

BEcause  
df = pd.Series(list_of_wordlen)  
  
#pprint(df.describe())  
for i in range(90,100):  
	pprint(df.quantile(i/100))  
  
for i in range(990,1000):  
	pprint(df.quantile(i/1000))  
    
### Thank you [atajti](https://github.com/atajti) for the starting data!
