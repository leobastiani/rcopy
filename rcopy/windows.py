#!python3
#encoding=utf-8
from __future__ import absolute_import, division, print_function

import sys
import time

import pyperclip
from pynput import keyboard

DEBUG = sys.flags.debug or False

def debug(*args):
    if not DEBUG:
        return
    print(*args)

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

def vk(key):
    if hasattr(key, 'value'):
        return key.value.vk
    return key.vk

def on_press(key):
    debug("Pressed:", repr(key))
    if hasattr(key, 'char') and key.char == '\x16':
        time.sleep(0.01)
        execute()
        return

def main():
    execute()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
