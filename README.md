# TwitterPredictStream

```flow
st=>start: Input_Dir:>http://www.google.com[blank]
e=>Training_Set:>http://www.google.com
op1=>operation: jsonWrapper.py
op2=>operation: list.py


st->op1->cond
op1->op2->e

``

with "jsonWrapper.py" we have selected the non retweets from the downloaded data.  
With "list.py" we have merged the msg parts of the tweets into one bigger file  

Because of:  
```python

df = pd.Series(list_of_wordlen)  
print(df.describe())

for i in range(90,100):  
	pprint(df.quantile(i/100))  
  
for i in range(990,1000):  
	pprint(df.quantile(i/1000))  
```  
Our training sequence length is going to be 23.

it is might long a bit but we are going to see  
We are going to hash all the links as: last_eight_char(md5(http))  
We change compile(loss='categorical_crossentropy', optimizer='adam')  
into  
compile(loss='sparse_categorical_crossentropy', optimizer='adam')  

because our matrix would be too big for our memory so we are going to use integers  
@[stack](https://stackoverflow.com/questions/46293734/memoryerror-in-keras-utils-np-utils-to-categorical)  
because tensorflow/core/common_runtime/bfc_allocator.cc:275] Allocator (GPU_0_bfc) ran out of memory trying to allocate  
we try to train with smaler batch size  
fit(X, y, epochs=1, batch_size=4, callbacks=callbacks_list) instead of batch_size=64 or 128
@[stack](https://stackoverflow.com/questions/36927607/how-can-i-solve-ran-out-of-gpu-memory-in-tensorflow)
### Thank you [atajti](https://github.com/atajti) for the starting data!
