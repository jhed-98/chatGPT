import pyttsx3
import string
import random

number_of_strings = 5
length_of_string = 8
for x in range(number_of_strings):
    audio_cadena = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
#   print(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))

  
engine = pyttsx3.init()
# Control the rate. Higher rate = more speed
engine.setProperty("rate", 150)
text = "Hola mundo. Este audio quedará guardado en un archivo"
output_file = "audio_"+audio_cadena+".mp3"
engine.save_to_file(text,output_file)
engine.runAndWait()
