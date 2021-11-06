from gtts import gTTS
import os

path = 'path where the mp3 file should be saved'

file = input('Welches File möchtest du vorgelesen bekommen? (Full Path)')
file_open = open(str(file), "r").read().replace("\n", " ")

language = input('Welche Sprache möchtest du? \nde/en\n')
if str(language) == 'en':
    language = 'en'
else:
    language = 'de'

speech = gTTS(text=str(file_open), lang=language, slow=False)

name = input('Wie soll das File heißen?')
speech.save(path+'F2S'+str(name)+'.mp3')
os.system(f'start {path}F2S{str(name)}.mp3')
