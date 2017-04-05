#!/usr/bin/env python

import os
import io
import random
import ConfigParser

from subprocess import Popen
from datetime import datetime

TOP_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(TOP_DIR, "resources/models")
SOUND_DIR = os.path.join(TOP_DIR, "resources/sounds")
CONFIG_DIR = os.path.join(TOP_DIR, "artoo.cfg")

config = ConfigParser.RawConfigParser(allow_no_value=True)
config.read(CONFIG_DIR)

def artoo_listen():
    print(os.path.join(SOUND_DIR, 'hello_artoo.mp3'))
    config.set('flags','hey_artoo',datetime.now())
    print('Artoo was listening at {0}'.format(config.get('flags','hey_artoo')))
    omxp = Popen(['omxplayer',os.path.join(SOUND_DIR, 'hello_artoo.mp3')])


def artoo_listening():
    l = config.get('flags','hey_artoo')
    return l


def get_dictionary():
    return {os.path.join(MODEL_DIR, "hello_artoo.pmdl"): lambda: hello_artoo(),
            os.path.join(MODEL_DIR, "hey_artoo.pmdl"): lambda: hello_artoo(),
            os.path.join(MODEL_DIR, "how_was_your_day_artoo.pmdl"): 
            lambda: how_was_your_day_artoo()}


def hey_artoo():
    print('You Said "Hey Artoo"!')
    artoo_listen()


def hello_artoo():
    print('You Said "Hello R2"!')
    artoo_listen()


def how_was_your_day_artoo():
    print('You Said "How was your day, R2"!')
    print(os.path.join(SOUND_DIR, 'how_was_your_day_artoo.mp3'))
    i = len([name for name in os.listdir(SOUND_DIR) if not os.path.isfile(name)]) - 1
    s = random.randint(0,i)
    response = [name for name in os.listdir(SOUND_DIR) if not os.path.isfile(name)][s]
    omxp = Popen(['omxplayer',os.path.join(SOUND_DIR, response)])
