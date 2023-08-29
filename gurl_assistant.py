import pyttsx3
import pywhatkit
import wikipedia
import datetime
import speech_recognition as sr

r = sr.Recognizer()

phoneNumbers = {'arjun':'11111111','amal':'22222222222','sayuj':'333333333333','jerin':'4444444444','vazha':'55555555'}
exit  = 0

def commands():
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print('Listening... Ask Now....')
                audioin = r.listen(source)
                my_text = r.recognize_google(audioin)
                my_text = my_text.lower()
                print(my_text)
                
            #song
            if 'play' in my_text:
                my_text = my_text.replace('play','')
                speak('Playing'+my_text+'in youtube ....')
                pywhatkit.playonyt(my_text)
            
            #date
            elif 'date' in my_text:
                today = datetime.date.today()
                speak(today)
                
            #time
            elif 'time' in my_text:
                timenow = datetime.datetime.now().strftime('%H:%M')
                speak(timenow)
            
            #details
            elif 'tell me about' in my_text:
                person = my_text.replace('tell me about','')
                info = wikipedia.summary(person,1)
                speak(info)
            
            #phoneNumbers
            elif 'phone number' in my_text:
                names = list(phoneNumbers)
                for name in names:
                    if name in my_text:
                        print(name+"'s phone number is "+phoneNumbers[name])
                        speak(name+"'s phone number is "+phoneNumbers[name])

            else:
                speak('Data not found, could u ask something else')

        except sr.UnknownValueError:
                print("Could not understand audio")
        except sr.RequestError as e:
                print(f"Could not request results; {e}")  


def speak(command):
    engine = pyttsx3.init() #object declaration to get what we give as text is converted to speech 
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(command)
    
    engine.runAndWait()

speak('welcome to your girl assistant, how can i help you')

while(True):
    commands()
    