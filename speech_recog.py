# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 01:23:45 2020

@author: HP
"""
# Python program to translate 
# speech to text and text to speech 
  
  
import speech_recognition as sr 
import pyttsx3  


def get_text_from_speech():
    # Initialize the recognizer  
    r = sr.Recognizer()  
    MyText=""
    while(MyText==""):     
            with sr.Microphone() as source2: 
                # wait for a second to let the recognizer 
                # adjust the energy threshold based on 
                # the surrounding noise level  
                r.adjust_for_ambient_noise(source2, duration=0.2) 
                  
                #listens for the user's input  
                audio2 = r.listen(source2) 
                  
                # Using ggogle to recognize audio 
                MyText = r.recognize_google(audio2) 
                MyText = MyText.lower()
    return MyText
#get_text_from_speech()
      
            
              
   