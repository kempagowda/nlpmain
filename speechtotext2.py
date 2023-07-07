import speech_recognition as sr

# initialize the recognizer
r = sr.Recognizer()

with sr.Microphone() as source:

    print("Listening...")
    r.pause_threshold = 1
    r.adjust_for_ambient_noise(source)

# listen for the data (load audio to memory)
    audio = r.listen(source)
    # recognize (convert from speech to text)
    print("Recognizing")

    request = r.recognize_google(audio, language="en-in")
    print(request)
