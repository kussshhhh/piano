import numpy as np
import sounddevice as sd

def generate_piano_note(freq, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    
    # Fundamental frequency
    note = np.sin(2 * np.pi * freq * t)
    
    # Add harmonics
    note += 0.5 * np.sin(2 * np.pi * freq * 2 * t)  # 1st overtone
    note += 0.3 * np.sin(2 * np.pi * freq * 3 * t)  # 2nd overtone
    note += 0.2 * np.sin(2 * np.pi * freq * 4 * t)  # 3rd overtone
    
    # Apply envelope
    envelope = np.exp(-t * 5)  # Quick attack, exponential decay
    note *= envelope
    
    return note

def play_note(frequency, duration):
    samples = generate_piano_note(frequency, duration)
    
    # Normalize to 16-bit range
    samples = (samples * 32767 / np.max(np.abs(samples))).astype(np.int16)
    
    # Play the sound
    sd.play(samples, samplerate=44100)
    sd.wait()

# Example usage: Play a middle C (261.63 Hz) for 2 seconds
play_note(261.63, 2)