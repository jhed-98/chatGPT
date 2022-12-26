import pyttsx3

engine = pyttsx3.init()
# Control the rate. Higher rate = more speed
# Controla la tasa. Puntuación alta
engine.setProperty("rate", 150)
text = "Hola mundo. Visita JhEd"
engine.say(text)

# Queue another audio
# Poner en cola otro audio

another_text = "I like Python"
engine.say(another_text)
engine.runAndWait()
# Ejecuta esperando terminar todo el audio
