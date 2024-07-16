import os 
import time
import platform
import numpy as np
import sounddevice as sd 
import threading
from pynput import keyboard



if platform.system() == 'Windows':
    import msvcrt
else:
    import tty
    import sys
    import termios

notes = {
    'a': 261.63,  # C4
    'w': 277.18,  # C#4
    's': 293.66,  # D4
    'e': 311.13,  # D#4
    'd': 329.63,  # E4
    'f': 349.23,  # F4
    't': 369.99,  # F#4
    'g': 392.00,  # G4
    'y': 415.30,  # G#4
    'h': 440.00,  # A4
    'u': 466.16,  # A#4
    'j': 493.88,  # B4
    'k': 523.25,  # C5
    'o': 554.37,  # C#5
    'l': 587.33,  # D5
}

def clear_screen() :
    os.system('cls' if platform.system() == 'Windows' else 'clear') 

def generate_note(freq, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate*duration), False)

    #fundamental frequency
    note = np.sin(2 * np.pi * freq * t)

    note += 0.5 * np.sin(2*np.pi*freq*2*t)
    note += 0.3 * np.sin(2*np.pi*freq*3*t)
    note += 0.2 * np.sin(2*np.pi*freq*4*t)

    envelope = np.exp(-t * 5)
    note *= envelope

    return note


def play_note(key, duration = 0.5):

    if key not in notes:
        print(f"Note '{key}' not found in the dictionary")
        return
    
    frequency = notes[key]
    samples = generate_note(frequency, duration)

    samples = (samples * 32767 / np.max(np.abs(samples)).astype(np.int16))

    sd.play(samples, samplerate=44100)
    # sd.wait()

def on_press(key):
    try:
        k = key.char.lower()
        if k in notes:
            threading.Thread(target=play_note, args = (k,)).start()
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        return False


def draw_piano():
    print("\n")
    print("  W   E       T   Y   U       O")
    print(" ┌─┐ ┌─┐    ┌─┐ ┌─┐ ┌─┐    ┌─┐")
    print(" │ │ │ │    │ │ │ │ │ │    │ │")
    print(" │ │ │ │    │ │ │ │ │ │    │ │")
    print(" └─┘ └─┘    └─┘ └─┘ └─┘    └─┘")
    print("┌───┬───┬───┬───┬───┬───┬───┬───┬───┐")
    print("│ A │ S │ D │ F │ G │ H │ J │ K │ L │")
    print("└───┴───┴───┴───┴───┴───┴───┴───┴───┘")


def get_char():
    if platform.system() == 'Windows':
        return msvcrt.getch().decode('utf-8').lower() 
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd) 
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings) 
        
        return ch.lower() 


def main():
    clear_screen() ;
    print("Welcome to the terminal Piano!")
    print("Press the keys on your keyboard to play notes, or Q to quit")

    while True: 
        draw_piano()

        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
        # key = get_char() 

        # if key == 'q':
        #     print("Thanks for playing!")
        #     break
        # elif key in notes: 
        #     clear_screen()
        #     play_note(key)
        # else:
        #     clear_screen()
        #     print("Invalid key try again.")

if __name__ == "__main__":
    main()

