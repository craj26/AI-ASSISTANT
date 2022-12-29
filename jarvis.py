import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyjokes



engine = pyttsx3.init()


def speak(bol):

	engine.say(bol)
	engine.runAndWait()



def time():
	Time=datetime.datetime.now().strftime("%I:%M:%S")
	speak(Time)


 
def date():

	year =int(datetime.datetime.now().year)
	month =str(datetime.datetime.now().month)
	day =int(datetime.datetime.now().day)
	speak(day)
	speak(month)
	speak(year)

def wishme():
	speak("welcome back sir")
	
	

	hour =datetime.datetime.now().hour
	if hour >=6 and hour <12:
		speak("good morning sir")
	elif hour >=12 and hour <17:
		speak("good afternoon sir")
	else :
		speak("good night sir")

	
	speak("Jarvis at your service. Please tell me how can i help you?")   



def bolo():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		
		print("listening.....")
		r.pause_threshold = 5
		audio = r.listen(source)

	try:
		print("recognizing...")    
		query = r.recognize_google(audio,language='en-in')
		print(query)

	except Exception as E:
		print(E)
		speak("say again please")


		return "none"

	return(query)
def jokes():
	speak(pyjokes.get_joke())    
 

if __name__ == "__main__":
	wishme()
	while True:
		query = bolo().lower()
		if "time" in query:
			time()
			
		elif 'search in chrome' in query:
			speak("What should i search")
			chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
			search = bolo().lower()
			wb.get(chromepath).open_new_tab(search +'.com')
		elif 'play songs' in query:
			songs_dir = 'D:\\song\\Evergreen'
			songs = os.listdir(songs_dir)
			os.startfile(os.path.join(songs_dir, songs[0]))
		elif 'joke' in query:
			jokes()

		elif 'offline' in query:
			quit()            
		else:
			quit()        
	
	
