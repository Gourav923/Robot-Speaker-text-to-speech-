#import python text to speech library
import pyttsx3
print('Welcome to RoboWorld')
#make a engine for initialization
robo= pyttsx3.init()
#while loop for infinite result
while True:
    talk=input('Enter your sentence/word: ') #take input from user
    #to stop the loop
    if talk=='exit':
        break
    #for pronounce the word/sentence
    robo.say(talk)
    # for aun and wait 
    robo.runAndWait()