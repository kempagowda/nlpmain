# text to speech
# pip install gtts
# pip install playsound
# import required for text to speech conversion
from gtts import gTTS
import os
mytext = "Welcome to Natural Language programming"
language = "en"
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("myfile.mp3")
os.system("myfile.mp3")
print("myfile.mp3 has been saved.")
