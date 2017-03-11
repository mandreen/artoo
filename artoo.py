#!/usr/bin/env python

import snowboydecoder
import callback
import signal

# artoo core based on snowboy demo
interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted


# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

models = callback.get_dictionary().keys()
sensitivity = [0.5]*len(models)
detector = snowboydecoder.HotwordDetector(models, sensitivity=sensitivity)
print('Listening... Press Ctrl+C to exit')


# main loop
detector.start(detected_callback=callback.get_dictionary().values(),
               interrupt_check=interrupt_callback,
               sleep_time=0.03)


detector.terminate()
