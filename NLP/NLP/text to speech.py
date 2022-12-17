from gtts import gTTS
from playsound import playsound
mytext="pully ko sadi chahiye"
language="en"
myobj=gTTS(text=mytext,lang=language,slow=False)
myobj.save('myfiles.mp3')
playsound('myfiles.mp3')
