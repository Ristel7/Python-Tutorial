import pyttsx3

engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


command = "hello"  # This would normally come from your microphone

if "hello" in command:
    speak("Hello Priyanshu, how can I help you with your code today?")
