import os 
import time
import platform 
from pysinewave import SineWave
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

sinewave = SineWave(pitch = 0, pitch_per_second = 100)

def play_note(frequency):

    print(f"Playing note at  {frequency} Hz") 
    sinewave.set_pitch(frequency)
    sinewave.play()
    time.sleep(0.3)
    sinewave.stop()
    
    # time.sleep(0.3) 


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
        key = get_char() 

        if key == 'q':
            print("Thanks for playing!")
            break
        elif key in notes: 
            clear_screen()
            play_note(notes[key])
        else:
            clear_screen()
            print("Invalid key try again.")

if __name__ == "__main__":
    main()

