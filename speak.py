# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 01:53:17 2020

@author: HP
"""
import pyttsx3  

class SpeakText(): 
    # Initialize the engine
    engine= pyttsx3.init()
    def __init__(self):
       self.rate=SpeakText.engine.getProperty("rate")
       #print(self.rate)
       self.volume=SpeakText.engine.getProperty("volume")
    
    def Speak(self,command,speed=0,sound=0):
        if(speed==0):
            SpeakText.engine.setProperty('rate', self.rate)
        else:
            SpeakText.engine.setProperty('rate', speed)
        if(sound==0):
            SpeakText.engine.setProperty('volume',self.volume)
        else:
            SpeakText.engine.setProperty('volume', sound)
        self.engine.say(command)  
        self.engine.runAndWait() 
        
        




  