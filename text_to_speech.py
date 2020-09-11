from gtts import gTTS
import os
f=open(r"C:\Users\hp\Desktop\text.txt")
sptext=f.read().replace("\n"," ")
language="en"
output=gTTS(text = sptext, lang=language,slow=False)
output.save("firstmethod.mp3")
f.close()
os.system("start firstmethod.mp3")
