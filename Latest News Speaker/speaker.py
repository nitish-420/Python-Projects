def speak(str):
    from win32com.client import Dispatch

    speak=Dispatch("SAPI.SpVoice")

    speak.Speak(str)

if __name__ == "__main__":
    speak("This is used by nitish to make news speaker")
