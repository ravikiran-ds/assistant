# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 01:48:18 2020

@author: HP
"""
import speech_recog as sr
from speak import SpeakText
import tensorflow
import keras
from keras import models
import pandas as pd
from search import search_term
from search import search_youtube

#loading the model
model=models.load_model("hate_speech.model")
#taking input from users
speak=SpeakText()
#getting voice input from user
#text=sr.get_text_from_speech() 
def take_inp():
    text=input("Enter text :") 
    temp=text.split()
    #predicitng
    x=pd.read_csv("hate_headers.csv")
    for i in temp:
        if i in x.columns.unique():
            x[i]=1
    pred=model.predict(x)
    return pred,text
    print("{} is the list of values  {} is the text {} is the prediction for hate.".format(temp,text,pred[0][0]))
#take_inp()

def response(text,speed=200,sound=5):
    speak.Speak(text,speed,sound)

#quores set
quotes=pd.read_csv('quots.csv', sep=" ", header=None,dtype={0:str})
quotes.drop([0],inplace=True)
for i in range(1,len(quotes)+1):
    quotes[0][i]=quotes[0][i].replace("\x9d","")
    quotes[0][i]=quotes[0][i].replace("\t","")

#facts set
facts=pd.read_csv('facts.csv')
for i in range(0,len(facts)):
    facts["facts"][i]=facts["facts"][i].replace('\x9d',"")
    facts["facts"][i]=facts["facts"][i].replace('â€',"'")

from random import randint 
def hate_response():
    #print('hate')
    qu=randint(0,len(quotes))
    response(quotes.iloc[qu,0],speed=150,sound=10)
    response("do not hate",speed=100,sound=10)  
def normal_response():
    #print('normal')
    fa=randint(0,len(facts))
    response(facts.iloc[fa,0],speed=150,sound=10)
    #response("Good for you",speed=100,sound=5)


#responding to input
def out():
    pred=take_inp()
    if pred[0][0]>0.7:
        hate_response()
        out()
    else:
        normal_response()
        out()

def hate_speech():
    i=1
    while i==1:
        try:
            out()
        except KeyboardInterrupt:
            print("good bye")
            response("Good Bye",speed=120,sound=7)
            i=2
            
def search():
    _,text=take_inp()
    search_term(text)

def youtube():
    _,text=take_inp()
    search_youtube(text)

#hate speech assistant
hate_speech()
#search assistant
search()
#search youtube
youtube()


    

