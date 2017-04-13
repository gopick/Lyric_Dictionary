# Song Detail generation 


## Creation 

1. First obtained the filemxm_dataset_train.txt https://labrosa.ee.columbia.edu/millionsong/musixmatch

2. The file above doesn't contain track names and, the words associated with the tracks have trivial words and also contains spelling mistakes. 

3. We have manually chosen which words to use, and have corrected the spellings of the words. 

4. To get the track details we have used an api provided by musixmatch. Check :https://developer.musixmatch.com/. This step can be made much faster if you take a premium account on the website.

5. After getting the track details, the words used in a track and the number of times each word is used, we use dict.py to create data in a form that will be entered in the database
