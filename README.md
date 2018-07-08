# TwitterPredictStream

  * With "jsonWrapper.py" we have selected the non retweets from the downloaded data.  
  * With "list.py" we have merged the msg parts of the tweets into one bigger file  

  * Our training sequence length is going to be 23 because of:  
```python

df = pd.Series(list_of_wordlen)  
print(df.describe())

for i in range(90,100):  
	pprint(df.quantile(i/100))  
  
for i in range(990,1000):  
	pprint(df.quantile(i/1000))  
``` 
It is might long a bit but we are going to see  
  * We are going to hash all the links as: last_eight_char(md5(http))  
  * We use compile(loss='sparse_categorical_crossentropy',  
Because our matrix would be too big for our memory so we are going to use integers  
@[stack](https://stackoverflow.com/questions/46293734/memoryerror-in-keras-utils-np-utils-to-categorical)  

* Instead of batch_size=64 or 128 ; we try to train with smaler batch size because of 
```python
tensorflow/core/common_runtime/bfc_allocator.cc:275] Allocator (GPU_0_bfc) ran out of memory trying to allocate
```  
```python 
fit(X, y, epochs=1, batch_size=4, callbacks=callbacks_list)
```  
 @[stack](https://stackoverflow.com/questions/36927607/how-can-i-solve-ran-out-of-gpu-memory-in-tensorflow)
### Thank you [atajti](https://github.com/atajti) for the starting data!
