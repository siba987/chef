import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something")
    audio = r.listen(source)

    try:
        print("You said:" + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("could not understand audio")
    except sr.RequestError as e:
        print(format(e))
