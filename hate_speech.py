# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 12:10:30 2020

@author: HP
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('hate_speech.csv')
#lookin at the shape of the dataset
rows,cols=df.shape
#columns
df.columns
#sample rows
df.head()
#lookin at first tweet
df.tweet[0]

#preprocessing
df2=df[["offensive_language","tweet"]]
df2.tweet=df.tweet.apply(lambda x:x.split(":",1))
#lookina t tweets
df2.tweet[0]
#removing the user name
for i in range(0,rows):
    if len(df2.tweet[i])>1:
        df2.tweet[i]=df2.tweet[i][1]
    else:
        df2.tweet[i]=df2.tweet[i][0]
#convertng offensive language to binary
df2["offensive_language"]= df2.offensive_language.apply(lambda x:1 if x>0 else 0 )

#text processing
#converting text to lower
df2.tweet=df2.tweet.apply(lambda x:x.lower())
#keeping only the text
import re
df2.tweet=df2.tweet.apply(lambda x:re.sub(pattern='[^a-zA-Z]',repl=" ",string=x))
#removing stopwords
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
df2.tweet=df2.tweet.apply(lambda x:x.split())
from nltk.stem.porter import PorterStemmer
stem=PorterStemmer()
df2.tweet=df2.tweet.apply(lambda x:[stem.stem(word) for word in x if word not in set(stopwords.words('english'))])

#creating the sparse matrix
df2.tweet=df2.tweet.apply(lambda x:" ".join(x))
corpus=[x for x in df2.tweet]
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=1500)
sparse_matrix=cv.fit_transform(corpus).toarray()
#cv.get_feature_names()

#dataframe of the sparse matrix with dependent variable
df0=pd.DataFrame(sparse_matrix,columns=cv.get_feature_names())
df0["hate"]=df2['offensive_language']

#classification
x=df0.drop("hate",axis=1)
y=df0['hate'].values

#splitting train test data
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=101)

#model building
import tensorflow
import keras 
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense

#initializing the ANN
ann_cls=Sequential()
#adding input and first layer
ann_cls.add(Dense(output_dim=750,input_dim=1499,activation='relu',init='uniform'))
#adding 2nd hidden layer
ann_cls.add(Dense(output_dim=750,activation='relu'))
#adding output layer
ann_cls.add(Dense(output_dim=1,activation='sigmoid'))
#compiling ANN
ann_cls.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
#fitting the data
ann_cls.fit(x_train,y_train,batch_size=100,epochs=10)
#saving the model
ann_cls.save('hate_speech.model')
#loading model
ann_cls=load_model('hate_speech.model')

#predicting
ypred=ann_cls.predict(x_test)
ypred=(ypred >0.5)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test, ypred)
cm


data={}
for i in x_train.columns.unique():
        data[i]=0
        temp=pd.DataFrame(data,columns=x_train.columns.unique(),index=[0])
temp.to_csv("hate_headers.csv",index=False)

def user_speech(text):
    #text=input("Enter a sentence:")
    temp_list=text.split()
    for i in temp_list:
        if i in temp.columns:
            temp[i]=1
    temp_pred=ann_cls.predict(temp)
    if temp_pred>0.5:
        #print("hate")
        return "hate"
    else:
        return "fine"



