import pyttsx3 #It'll convert text to speech
import speech_recognition as sr #It'll convert speech to text
import pyaudio #audio input/output
import datetime
import wikipedia 
import webbrowser #used to open browser programatically
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak('Good Morning!')
    elif hour>=12 and hour<12:
        speak('Good Afternoon!')
    else:
        speak('Good Evening')

    speak('Hi Iam Siri How may I help you')

def takeCommand():
    #It takes microphone input from the user and gives string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening......')
        # r.pause_threshold = 1 #it'll pause
        audio = r.listen(source)

    try:
        print('recognizing...')
        query = r.recognize_google(audio,language="en-in")
        print("user said:", query)

    except Exception as e:
        # print(e)
        print('say that again please....')
        return "None"
    return query
        
# def sendEmail(to,content):
#     server = smtplib.SMTP('smtp.gmail.com',587)#587 is port number
#     server.ehlo()
#     server.login('youremail.gmail','your-password')
#     server.sendmail('youremail@gmail.com', to, content)
#     server.close()


if __name__ == "__main__":
    wishMe()
    start = True
    while start:
        query = takeCommand().lower()
        # logic and executing task based on query
        if 'wikipedia' in query:
            speak('searching wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak('according to wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('openinng youtube..')
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            speak('openinng google..')
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            speak('openinng stackoverflow..')
            webbrowser.open("stackoverflow.com")
        
        elif 'open instagram' in query:
            speak('openinng instagram..')
            webbrowser.open("instagram.com")
            
        elif 'play deva deva' in query:
            speak('playing...')
            webbrowser.open("https://youtu.be/WjAPDofGg28")

        
        elif 'play spirits' in query:
            speak('playing...')
            webbrowser.open("")
        
        
        elif 'play padharo mhare' in query:
            speak('playing...')
            webbrowser.open("https://youtu.be/IEQ9Vj8lPa4")

        
        elif 'open facebook' in query:
            speak('openinng facebook..')
            webbrowser.open("facebook.ccom")
            
        # elif 'playmusic' in query:
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak('sir the time is',strTime)

        elif 'open code' in query:
            code_path ="C:\\Users\\kisho\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(code_path)

        # elif "email to deepak" in query:
        #     #you have to enable "less secure app" in gmail seetting to sent email or it won't work
        #     try:
        #         speak('what should i say')
        #         content = takeCommand()
        #         to = ""
        #         sendEmail(to,content)
        #         speak('email has been sent')
        #     except:
        #         speak('sorry my friend .I am not able to deny this email')
        elif 'exit' in query:
            start = False
