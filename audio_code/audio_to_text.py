import speech_recognition as sr
import pyttsx3
 

r = sr.Recognizer()
#intializing array for duplicate word
arr=[]

def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
     
while(1):   
     
    
    try:
         
        # use the microphone as source for input.
        with sr.Microphone() as source2:
             
            r.adjust_for_ambient_noise(source2, duration=0.2)
             
            #listens for the user's input
            audio2 = r.listen(source2)
             
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print("Did you say ",MyText)
            if MyText in arr:
                break
            else:
                continue
            arr.append(MyText)
            SpeakText(MyText)
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")