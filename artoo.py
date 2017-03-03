#!/usr/bin/env python

import os
import random
import snowboydecoder
import sys
import signal

from subprocess import Popen

# artoo core based on snowboy demo
TOP_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCE_FILE = os.path.join(TOP_DIR, "resources/common.res")
MODEL_DIR = os.path.join(TOP_DIR, "resources/models")


interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted


def hello_artoo():
    print('You Said "Hello R2"!')
    omxp = Popen(['omxplayer',os.path.join('hello_artoo.mp3')])


def how_was_your_day_artoo():
    print('You Said "How was your day, R2"!')
    i = len([name for name in os.listdir(SOUND_DIR) if not os.path.isfile(name)]) - 1
    s = random.randint(0,i)
    response = [name for name in os.listdir(SOUND_DIR) if not os.path.isfile(name)][s]
    omxp = Popen(['omxplayer',os.path.join(response)])
    

models = []
model_list = [n for n in os.listdir(MODEL_DIR) if not os.path.isfile(n)]
for model in model_list:
    models.append(os.path.join(MODEL_DIR, model))
    print("model: {0}".format(os.path.join(MODEL_DIR, model)))


callbacks = []
# write callbacks for any identified models
for m in [os.path.splitext(n)[0] for n in os.listdir(MODEL_DIR) if not os.path.isfile(n)]:
    callbacks.append(m)
    print("callback: {0}".format(m))


#if len(sys.argv) != 3:
#    print("Error: need to specify 2 model names")
#    print("Usage: python demo.py 1st.model 2nd.model")
#    sys.exit(-1)

#models = sys.argv[1:]

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

sensitivity = [0.5]*len(models)
detector = snowboydecoder.HotwordDetector(models, sensitivity=sensitivity)
#callbacks = [lambda: snowboydecoder.play_audio_file(snowboydecoder.DETECT_DING),
#             lambda: snowboydecoder.play_audio_file(snowboydecoder.DETECT_DONG)]
print('Listening... Press Ctrl+C to exit')

# main loop
# make sure you have the same numbers of callbacks and models
detector.start(detected_callback=callbacks,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()
