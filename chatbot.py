import openai
import pyttsx3

openai.api_key = "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"

engine = pyttsx3.init()
conversation = ""

i=1
while (i != 0):
     question = input("H: ")
     conversation += "\nHumano: " + question + "\nAI:"
     response = openai.Completion.create(
         engine="text-davinci-003",
         prompt=conversation,
         temperature=0.9,
         max_tokens=150,
         top_p=1,
         frequency_penalty=0,
         presence_penalty=0.6,
         stop=["\n", " H:", " AI:"]
     )
     anwer = response.choices[0].text.strip()
     conversation += anwer

     print("AI: " + anwer + "\n")
     engine.say(anwer)
     engine.runAndWait()
