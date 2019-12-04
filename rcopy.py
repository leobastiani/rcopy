#!python3
#encoding=utf-8
from __future__ import print_function, division, absolute_import

import sys
import pyperclip
from pynput import keyboard

# The key combination to check
COMBINATIONS = [
    {keyboard.Key.ctrl_l, keyboard.KeyCode(char='v')},
    {keyboard.Key.ctrl_l, keyboard.KeyCode(char='V')}
]

# The currently active modifiers
current = set()

strings = sys.argv[1:]
i = 0

def execute():
    global i
    pyperclip.copy(strings[i])
    i+=1
    if i == len(strings):
        sys.exit(0)

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()
        current.remove(key)

execute()
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
