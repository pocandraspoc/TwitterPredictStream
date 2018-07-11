# TwitterPredictStream
## TODO
  * Write down abstract, what this roject is about
  * Add the architecture of the hole project to have a better understanding  
    
      
        
  * With "jsonWrapper.py" we have selected the non retweets from the downloaded data.  
  * With "concatenate.py" we have merged the msg parts of the tweets into one bigger file.  
<p align="center">  
	<img src="https://i.imgur.com/cboql4P.png" alt="https://i.imgur.com/cboql4P.png" class="shrinkToFit transparent" width="126" height="732">
 </p>

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
  * Because our matrix would be too big for our memory so we are going to use integers we use: @[stack](https://stackoverflow.com/questions/46293734/memoryerror-in-keras-utils-np-utils-to-categorical)   
  ```python
compile(loss='sparse_categorical_crossentropy', ...) 
```  
  * Instead of batch_size=64 or 128 ; we try to train with smaler batch size because of: @[stack](https://stackoverflow.com/questions/36927607/how-can-i-solve-ran-out-of-gpu-memory-in-tensorflow)
```python
tensorflow/core/common_runtime/bfc_allocator.cc:275] Allocator (GPU_0_bfc) ran out of memory trying to allocate
```  

```python 
fit(X, y, epochs=1, batch_size=4, callbacks=callbacks_list)
```  

### Thank you [atajti](https://github.com/atajti) for the starting data!  
## Concept-s  
  * [Efficient BackProp](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf)
  * [Working with large datasets like Imagenet ](https://github.com/keras-team/keras/issues/68)
  * [Keras Multi GPU DOC](https://keras.io/utils/#multi_gpu_model)
  * [How to train on multi-GPUs when using fit_generator](https://github.com/keras-team/keras/issues/9502)
