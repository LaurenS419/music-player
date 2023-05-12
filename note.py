# Lauren Spee
# 261008497

import musicalbeeps

class Note:
    OCTAVE_MIN = 1
    OCTAVE_MAX = 7
    
    def __init__(self, duration, pitch, octave=1, accidental='natural'):
        ''' (float, str, int, str) -> NoneType
        Creates an object of type Note.
        >>> note = Note(4.0, "D", 5, "sharp")
        >>> note.pitch
        'D'
        >>> note = Note(.5, 'F', 1)
        >>> note.accidental
        'natural'
        >>> note = Note(8000.5, 'A', 6, 'flat')
        >>> note.duration
        8000.5
        '''
        
        if type(duration) != float or duration < 0:
            raise AssertionError("Incorrect duration value.")
        if type(pitch) != str or pitch.upper() not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'R']:
            raise AssertionError("Incorrect pitch value.")
        if type(octave) != int or octave > self.OCTAVE_MAX or octave < self.OCTAVE_MIN:
            raise AssertionError("Incorrect octave value.")
        if type(accidental) != str:
            raise AssertionError("Incorrect accidental value.")
        if accidental not in ['natural', 'sharp', 'flat']:
            raise AssertionError("Incorrect accidental value.")
        
        self.duration = duration
        self.pitch = pitch
        self.octave = octave
        self.accidental = accidental
        
    def __str__(self):
        ''' () -> str
        Returns a string containing specific class attributes
        of the class object.
        >>> note = Note(4.0, "D", 5, "sharp")
        >>> print(note)
        4.0 D 5 sharp
        >>> note = Note(.5, 'F', 1)
        >>> print(note)
        0.5 F 1 natural
        >>> note = Note(8000.5, 'A', 6, 'flat')
        >>> print(note)
        8000.5 A 6 flat
        '''
        return str(self.duration) + " " + self.pitch + " " + str(self.octave) + " " + self.accidental
    
    def play(self, player):
        ''' (Player) -> NoneType
        Takes a list of note objects in the melody object
        and returns the sum of the durations of each note.
        '''
        
        if self.accidental == 'sharp':
            acc = '#'
        elif self.accidental == 'flat':
            acc = 'b'
        else:
            acc = ''
        
        if self.pitch == 'R':
            note_played = 'pause'
        else:
            note_played = self.pitch + str(self.octave) + acc
        
        player.play_note(note_played, self.duration)


    
        
    