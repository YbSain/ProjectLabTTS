import speech_recognition as sr

r = sr.Recognizer()

def listen_and_convert():
    with sr.Microphone() as source:
        print("Listening. . .")
        r.adjust_for_ambient_noise(source, duration = 0.5)
        audio = r.listen(source)


    try:
        print("Recognizing. . .")
        text = r.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from google Web Speech API; {0}".format(e))

listen_and_convert()