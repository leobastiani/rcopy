#!python3
#encoding=utf-8
from __future__ import absolute_import, division, print_function

import sys
import time
import re

import pyperclip
from pynput import keyboard

DEBUG = sys.flags.debug or False

def debug(*args):
    if not DEBUG:
        return
    print(*args)

# The currently active modifiers
pressedButtons = set()

def getStringsFromClp():
    ret =  re.split(r'[\n\r]+', pyperclip.paste())
    if ret[-1] != '':
        ret.append('')
    return ret

strings = getStringsFromClp() if len(sys.argv) == 1 else sys.argv[1:]
i = 0

def execute():
    debug("execute()")
    global i
    pyperclip.copy(strings[i])
    i+=1
    if i == len(strings):
        sys.exit(0)

def keyRepr(key):
    if hasattr(key, 'char'):
        return key.char
    return key

def on_press(key):
    pressedButtons.add(keyRepr(key))
    debug("Pressed:", repr(key))
    debug("pressedButtons == {keyboard.Key.cmd, 'v'}:",pressedButtons == {keyboard.Key.cmd, 'v'})
    if pressedButtons == {keyboard.Key.cmd, 'v'}:
        time.sleep(0.01)
        execute()

def on_release(key):
    try:
        pressedButtons.remove(keyRepr(key))
    except KeyError:
        pass

execute()
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
