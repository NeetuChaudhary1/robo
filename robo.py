import speech_recognition as sr
import pyttsx3 as p
import webbrowser
import datetime



def say(text):
    engine = p.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    engine.setProperty('rate', 200) 

    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=0.5
        audio=r.listen(source)
    try:
        query=r.recognize_google(audio,language="en-in")
       
        print(f"user said: {query}")
        return query
    except Exception as e:
        return "some error occurred"

def Hindi():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        query=r.recognize_google(audio,language="hi-in")
        print(f"user said: {query}")
        return query
    except Exception as e:
        return "some error occurred"
    
def tamil():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        query=r.recognize_google(audio,language="ta-in")
        print(f"user said: {query}")
        return query
    except Exception as e:
        return "some error occurred"    
    
def punjabi():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        query=r.recognize_google(audio,language="pa-in")
        print(f"user said: {query}")
        return query
    except Exception as e:
        return "some error occurred"    
    
def gujrati():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        query=r.recognize_google(audio,language="gu-in")
        print(f"user said: {query}")
        return query
    except Exception as e:
        return "some error occurred"

if __name__ == '__main__':
    print("welcome to my robo")
    say("Raam Raam")
    while True:
      print("listenning...")
      say("English, Hindi ,punjabi,Tamil or gujrati")
      print("English, Hindi , Punjabi,Tamil or Gujrati")
      query=takeCommand()
      say(query)
      if "English".lower() in query.lower():
          print("listenning...")
          query=takeCommand()
          say(query)
          say("you can also ask me to open sites like youtube, google, wikipedia and the time")
          print("In English,You can also ask me to open sites like youtube, google, wikipedia and the time")
          sites=[["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google","https://www.google.com"]]
          for site in sites:
              if f"open {site[0]}".lower() in query.lower():
                 say(f"openning {site[0]} sir...")
                 webbrowser.open(site[1])
          if "the time" in query:
              strftime=datetime.datetime.now().strftime("%H:%M:%S")
              say(f"sir the time is {strftime}")
      if "Hindi".lower() in query.lower():
          print("listenning...")
          query=Hindi()        
      if "Gujarati".lower() in query.lower():
          print("listenning...")
          query=gujrati()              
      if "Punjabi".lower() in query.lower():
          print("listenning...")
          query=punjabi()  
      if "Tamil".lower() in query.lower():
          print("listenning...")
          query=tamil()  
      if "stop".lower() in query.lower():
         exit()                  
     
        
    
