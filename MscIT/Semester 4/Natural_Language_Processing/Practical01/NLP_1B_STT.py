#Aim: Convert audio file Speech to Text.
#Note: required to store the input file "NLP_test.wav" in the current folder before running the program.

#!pip install SpeechRecognition pydub
import speech_recognition as sr
filename = "MscIT\\Semester 4\\Natural_Language_Processing\\Practical01\\NLP_test.wav"

# initialize the recognizer
r = sr.Recognizer()
# open the file
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)
