# Lauren Spee
# 261008497

import musicalbeeps
from note import Note

class Melody():
    
    def __init__(self, filename):
        ''' (str) -> NoneType
        Creates an object of type Melody.
        >>> hot_cross_buns = Melody("hotcrossbuns.txt")
        >>> len(hot_cross_buns.notes)
        17
        >>> song = Melody('tetris.txt')
        >>> song.author
        'Nikolay Nekrasov, Hirokazu Tanaka'
        >>> song = Melody('fur_elise.txt')
        >>> song.title
        'Fur Elise'
        '''
        
        fobj = open(filename, 'r')
        file_list = []
        note_list = []
        counter1 = 2
        counter2 = 2
        counter3 = 0
        index_list = []
        
        for line in fobj:
            file_list.append(line.strip())
         
        while counter1 < len(file_list):
            item = file_list[counter1].split()
            repeat = item[4]
            
            if repeat == 'true':
                index_list.append(counter1)
                
            counter1 += 1
        
        end_index_list = index_list[1::2]
        start_index_list = index_list[0::2]

        while counter2 < len(file_list):
            item = file_list[counter2].split()
            duration = float(item[0])
            pitch = item[1]
            octave = int(item[2])
            accidental = item[3]

            note_list.append(Note(duration, pitch, octave, accidental.lower()))
            
            if counter2 in end_index_list:
                for elmt in file_list[start_index_list[counter3]:end_index_list[counter3]+1]:
                    item_in = elmt.split()
                    duration_in = float(item_in[0])
                    pitch_in = item_in[1]
                    octave_in = int(item_in[2])
                    accidental_in = item_in[3]
                    
                    note_list.append(Note(duration_in, pitch_in, octave_in, accidental_in.lower()))

                counter3 += 1

            counter2 += 1
                
        self.title = file_list[0]
        self.author = file_list[1]
        self.notes = note_list
        
        fobj.close()

    def play(self, player):
        ''' (Player) -> NoneType
        Calls the class Player to use the computer's
        speakers to play the objects of type Note.
        '''
        
        for note in self.notes:
            note.play(player)
         
    def get_total_duration(self):
        ''' () -> float
        Takes a list of note objects in the melody object
        and returns the sum of the durations of each note.
        >>> song = Melody("hotcrossbuns.txt")
        >>> song.get_total_duration()
        8.0
        >>> song = Melody("birthday.txt")
        >>> song.get_total_duration()
        13.0
        >>> song = Melody("tetris.txt")
        >>> song.get_total_duration()
        15.5
        '''
        durations = []
        total_duration = 0
        
        for elmt in self.notes:
            durations.append(elmt.duration)
                
        for item in durations:
            total_duration += item
        
        return total_duration
       
    def lower_octave(self):
        ''' () -> bool
        Changes all the octaves in each note object
        in the melody to one lesser, and returns True
        if it can without going out of the octave range,
        False if not.
        >>> song = Melody("hotcrossbuns.txt")
        >>> song.lower_octave()
        True
        >>> song = Melody("tetris.txt")
        >>> song.lower_octave()
        True
        >>> song = Melody("birthday.txt")
        >>> song.lower_octave()
        True
        '''
        
        for elmt in self.notes:
            if (elmt.octave - 1) < Note.OCTAVE_MIN:
                return False
        
        for elmt in self.notes:
            elmt.octave -= 1
            
        return True
    
    def upper_octave(self):
        ''' () -> bool
        Changes all the octaves in each note object
        in the melody to one greater, and returns True
        if it can without going out of the octave range,
        False if not.
        >>> song = Melody("hotcrossbuns.txt")
        >>> song.upper_octave()
        True
        >>> song = Melody("tetris.txt")
        >>> song.upper_octave()
        True
        >>> song = Melody("birthday.txt")
        >>> song.upper_octave()
        True
        '''
        
        for elmt in self.notes:
            if (elmt.octave + 1) > Note.OCTAVE_MAX:
                return False
        
        for elmt in self.notes:
            elmt.octave += 1
            
        return True
         
    def change_tempo(self, modifier):
        ''' (float) -> NoneType
        Changes the durations of each Note object by
        the float modifier.
        >>> song = Melody("hotcrossbuns.txt")
        >>> song.change_tempo(0.25)
        >>> song.get_total_duration()
        2.0
        >>> song = Melody("hotcrossbuns.txt")
        >>> song.change_tempo(2.0)
        >>> song.get_total_duration()
        16.0
        >>> song = Melody("tetris.txt")
        >>> song.change_tempo(1.5)
        >>> song.get_total_duration()
        23.25
        '''
        if type(modifier) != float:
            raise AssertionError("Invalid modifier type.")
        
        for elmt in self.notes:
            elmt.duration *= modifier


