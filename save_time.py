import pyttsx3
from datetime import datetime 
# from datetime import date

# today = date.today()
now = datetime.now()
audio_cadena = format(now.day)+"-"+format(now.month)+"-"+format(now.year)+"_"+format(now.hour)+"."+format(now.minute)+"."+format(now.second)

engine = pyttsx3.init()
# Control the rate. Higher rate = more speed
engine.setProperty("rate", 150)
text = "Hola mundo. Este audio quedará guardado en un archivo"
output_file = "audio_"+audio_cadena+".mp3"
engine.save_to_file(text,output_file)
engine.runAndWait()
