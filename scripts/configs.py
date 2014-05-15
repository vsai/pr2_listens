#Configuration file
import os
import pyaudio

#important path names
PATH_TO_SPEECH_PROFILE = os.path.join(os.getcwd(), 'speech.noise-profile')
BASE_DIR = os.path.join(os.getcwd(), 'files/')

#Audio Controls
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

#Publisher/Subscriber Topics
KEEP_SERVER_ALIVE_TOPIC = 'initiateRecord'
WORDS_HEARD_TOPIC = 'wordsHeard'

#Other configurations
STREAM_TIMEOUT_TIME = 10 #seconds
