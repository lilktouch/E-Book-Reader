from gtts import gTTS
import os

mytext = 'Welcome to Sarthak's world!'
language = 'en'
myobj = gTTS(text=1984.pdf, lang=language, slow=False)
myobj.save("EBook 1984")
os.system("mpg321 EBook 1984")