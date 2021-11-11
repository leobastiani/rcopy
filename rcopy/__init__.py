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

# The key combination to check
COMBINATIONS = [
    {keyboard.Key.ctrl_l, keyboard.KeyCode(char='v')},
    {keyboard.Key.ctrl_l, keyboard.KeyCode(char='V')}
]

# The currently active modifiers
pressedButtons = set()

strings = sys.argv[1:]
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

if __name__ == "__main__":
    main()
