import os
import time

from gtts import gTTS
from googletrans import Translator
import soundfile as sf
import speech_recognition as sr
from pytesseract import pytesseract
from PIL import Image

def speach_text(audio,_id):
    try:
        # Create a Recognizer object
        OGG_FILE = audio
        #     print(1)
        #     # ovozli habar faylini .wav formatiga aylantirish
        data, samplerate = sf.read(OGG_FILE)
        sf.write('data/voices/'+str(_id)+"1.wav", data, samplerate)
        #
        os.remove(audio)
        r = sr.Recognizer()

        # Read the audio file
        with sr.AudioFile('data/voices/'+str(_id)+"1.wav") as source:
            audio = r.record(source)

        # Transcribe the audio
        text = r.recognize_google(audio)
        os.remove('data/voices/'+str(_id)+"1.wav")
        return text
    except:
        return "No speach"

def photo_text(imgn):
    try:
        img = Image.open(imgn)
        text = pytesseract.image_to_string(img)
        os.remove(imgn)
        return text
    except:return "so'z topilmadi"


def translator_text(text):
    trans = Translator()
    holat = trans.detect(text).lang
    if holat == 'uz':
        holat = 'uz_en'
        rt = trans.translate(text=text,dest='en',src='uz').text
    elif holat == 'en':
        holat = 'en_uz'
        rt = trans.translate(text=text,dest='uz',src='en').text
    else:
        rt1 = trans.translate(text=text,dest='en',src='uz').text
        rt2 = trans.translate(text=text,dest='uz',src='en').text
        if rt1==rt2:
            holat = 'uz_en'
            rt = trans.translate(text=text, dest='en', src='uz').text
        elif rt1 == text:
            holat = 'en_uz'
            rt = trans.translate(text=text, dest='uz', src='en').text
        elif rt2 == text:
            holat = 'uz_en'
            rt = trans.translate(text=text, dest='en', src='uz').text
        else:
            holat = 'uz_en'
            rt = trans.translate(text=text, dest='en', src='uz').text
    return {'text':f" TRANSLATION:\n{rt}",'type':holat}


def word_audio(word, t):
    """
    :param words:
    :return:
    """
    # ovozli habar yaratish
    word = word.split('TRANSLATION:\n')[t]
    tts = gTTS(word)
    # ovozli habarni saqlash
    tts.save(f"data/audio/{word}.mp3")
    return f"data/audio/"+word+".mp3"