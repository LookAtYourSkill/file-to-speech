from gtts import gTTS
import os

path = 'path where the mp3 file should be saved'

file = input('Which file would you like to have read to you? ? (Full Path where the file is)')
file_open = open(str(file), "r").read().replace("\n", " ")

language = input('What language you want? \nde = german/en = english\n')
if str(language) == 'en':
    language = 'en'
else:
    language = 'de'

speech = gTTS(text=str(file_open), lang=language, slow=False)

name = input('What name should the file have ?')
speech.save(path+'F2S'+str(name)+'.mp3')
os.system(f'start {path}F2S{str(name)}.mp3')
