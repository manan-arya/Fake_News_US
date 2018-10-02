
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import pickle
from sklearn.feature_extraction.text import CountVectorizer
import sys


# In[2]:


def func(text):
    
    entry_dict = {'title':["Specter of Trump Loosens Tongues, if Not Purse Strings, in Silicon Valley - The New York Times"],
             'text':[text]}
    
    entry = pd.DataFrame(entry_dict)
    
    import warnings
    
    warnings.filterwarnings("ignore")
    
    loaded_model = pickle.load(open(r".\fake_news_model.sav",'rb'))
    
    loaded_vectorizer = pickle.load(open(r'.\fake_news_vectorizer.sav','rb'))
    
    sparsed_entry=loaded_vectorizer.transform(entry['text'])
    
    prediction = loaded_model.predict(sparsed_entry)
    
    if prediction[0] == 0:
        return("\nWarning: News maybe a fake one!!\n")
    else:
        return("\nDon't worry, news is a true one!!\n")
    
    
    input("Press a button to close")


# ## Driver function

# print("\nEnter the News\n")
# text = input()
# 
# out = func(text)
# print(out)
