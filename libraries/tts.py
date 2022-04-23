from gtts import gTTS
import os
  
# Language in which you want to convert
input_text = input('Enter a text:')

myobj = gTTS(text=input_text, lang='my', slow=False)
  
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("welcome.mp3")
  
# Playing the converted file
os.system("mpg321 welcome.mp3")