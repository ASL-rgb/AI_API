import pyaudio
import speech_recognition
import openai
from gtts import gTTS
from playsound import playsound
from openai import Engine
import re

def speech_rec():
    recognizer = speech_recognition.Recognizer()

    while True:
        try:
            # Setup Microphone and set parameters to interupt recording
            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=1)
                audio = recognizer.listen(mic)
                #speech is translated by google translater to text

                text = recognizer.recognize_google(audio, language='de-DE')
                text = text.lower()
                print(text)

                return text

        except speech_recognition.UnknownValueError:
            print('error occuered')
            recognizer = speech_recognition.Recognizer()
            continue

def OpenAI_API_Req(speech_text, counter):
    # need to outsource API Key!
    cleanText = ""
    openai.api_key = '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'
    response = openai.Completion.create(
        engine='text-babbage-001',
        prompt=speech_text,
        temperature=0.5,
        max_tokens=25,

    )

    resp = response.choices[0].text.split('.')
    string_resp = str(resp)
    cleanText = string_resp.strip('\n')

    print(cleanText)
    tts = gTTS(text=cleanText, lang='de-DE', slow=False)
    savefile = 'AI_Out%s.mp3' % counter
    tts.save(savefile)
    playsound(savefile)
    '''text = ""
    
    '''


if __name__ == '__main__':
    counter = 0
    while True:
        counter += 1
        speech_text = speech_rec()
        OpenAI_API_Req(speech_text, counter)
