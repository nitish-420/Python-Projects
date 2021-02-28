def speak(str):
    from win32com.client import Dispatch

    speak=Dispatch("SAPI.SpVoice")

    speak.Speak(str)

import json
import requests
url = ('http://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey=ce0a4af8d2814e3f97a21282f7983c8e')
response = requests.get(url)
data=dict(response.json())

hdlns=list()
for item in data["articles"]:
    if item.get("source").get("id")=='the-times-of-india':
        hdlns.append(item.get("title"))
i=1
speak("Nitish , welcomes you here , have a good day")
for item in hdlns:
    speak(f"Headline number {i} : {item}")
    i+=1


