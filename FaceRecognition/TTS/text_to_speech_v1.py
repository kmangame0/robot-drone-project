# coding=utf-8
import json
import pyaudio  
import wave  
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1

text_to_speech = TextToSpeechV1(
    username='7c4c7d85-4936-4e0e-9235-86b25e539c2d',
    password='ULaXMJvfG3xq',
    x_watson_learning_opt_out=True)

#with open(join(dirname(__file__), 'text.wav'), 'wb') as audio_file:
    #audio_file.write(text_to_speech.synthesize('Hello world! My name is Watson!', accept='audio/wav', voice="en-US_AllisonVoice"))

chunk = 1024   
f = wave.open(r"text.wav","rb")   
p = pyaudio.PyAudio()   
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                channels = f.getnchannels(),  
                rate = f.getframerate(),  
                output = True)  

data = f.readframes(chunk)  

while data != '':  
    stream.write(data)  
    data = f.readframes(chunk)  

 
stream.stop_stream()  
stream.close()  
 
p.terminate()  
