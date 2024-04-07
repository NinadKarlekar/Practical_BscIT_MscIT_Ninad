# Natural Language Processing

M. Sc (Information Technology)
Natural Language Processing



## Index

| Sr.No. | Name | README | DOWNLOAD |
| --- | --- | --- | --- |
| [Prac1A](/MscIT/Semester%204/Natural_Language_Processing/Practical01/) <br> [Prac1B](/MscIT/Semester%204/Natural_Language_Processing/Practical01/) | 1A. Convert file Text to Speech. <br> 1B. Convert file Speech to Text. | [Prac1A](#prac1) <br> [Prac1B](#prac1) |  [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Semester%204/Natural_Language_Processing/Practical01/NLP_1A_TTS.py) <br> [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Semester%204/Natural_Language_Processing/Practical01/NLP_1B_STT.py) |


******************
---------------------

## Prac1

1A. Convert file Text to Speech.


<details>
<summary>CODE</summary>

```python
# Import the required module for text to speech conversion

#!pip install gtts
from gtts import gTTS

# This module is imported so that we can play the converted audio
import os

# The text that you want to convert to audio
mytext = "Hello Everyone!My name is Ninad"

# Language in which you want to convert
language = "en"

# Passing the text and language to the engine, here we have marked slow=False. Which tells the module that the converted audio should have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named welcome
myobj.save("welcome1.mp3")

# Playing the converted file
#os.system("mpg321 welcome.mp3")

```

</details>

<br>


1B. Convert file Speech to Text.


<details>
<summary>CODE</summary>


```python
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

```

</details>

******************************************************

## Prac2



******************************************************