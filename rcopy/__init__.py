#!python3
#encoding=utf-8
from __future__ import print_function, division, absolute_import

import sys
import pyperclip
from pynput import keyboard

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

def on_release(key):
    if hasattr(key, 'char') and key.char == '\x16':
        execute()

def main():
    if len(strings) > 0:
        execute()
        with keyboard.Listener(on_release=on_release) as listener:
            listener.join()

if __name__ == "__main__":
    main()
