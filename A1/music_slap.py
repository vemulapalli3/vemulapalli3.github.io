import serial
import pygame
import sys

noteInp = serial.Serial('COM4', 9600)

pygame.mixer.init()

octave = 4

while True:
    keys = {'c': 'C'+str(octave),
            'd': 'D'+str(octave),
            'e': 'E'+str(octave),
            'f': 'F'+str(octave),
            'g': 'G'+str(octave),
            'a': 'A'+str(octave),
            'b': 'B'+str(octave),
            'D': 'Db'+str(octave),
            'E': 'Eb'+str(octave),
            'G': 'Gb'+str(octave),
            'A': 'Ab'+str(octave),
            'B': 'Bb'+str(octave)}

    inp = noteInp.read(1)
    inp1 = str(inp)
    mainInp = inp1[2]
    
    if mainInp == 'q':
        if(octave > 3):
            octave -= 1
        continue
    elif mainInp == 'w':
        if(octave < 5):
            octave += 1
        continue
    note = pygame.mixer.Sound('sounds/' + keys[mainInp] + '.wav')
    note.play()
