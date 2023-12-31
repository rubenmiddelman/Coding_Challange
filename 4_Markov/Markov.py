"""
 # @ Author: Ruben Middelman
 # @ Create Time: 2023-10-28 04:24:28
 # @ Modified by: Ruben Middelman
 # @ Modified time: 2023-10-28 04:59:19
 # @ Description:
    Midi Markov chain that creates a new midi file based on an old midi file
 # @ TODO: note length, velocity, multi notes at the same time.
 """

import mido
import random
import numpy as np


def Init_File():
    midi_File = mido.MidiFile("Fur Elise.mid", clip=True)
    return midi_File


# Reads a MIDI file and adds all the notes to the list
def Read_File(file):
    message_List = []
    for msg in file:
        if msg.type == "note_on":
            message_List.append(msg.note)
    return message_List


# makes pairs for the Markov chain
def Make_Pairs(list_Of_Notes):
    list_Of_Pairs = []
    for i in range(len(list_Of_Notes)):
        if i < (len(list_Of_Notes) - 1):
            pair = (
                list_Of_Notes[i],
                list_Of_Notes[i + 1],
            )  # Use tuples for pairs instead of list, this is needed for dictionary
            list_Of_Pairs.append(pair)
    return list_Of_Pairs


# Fills the dictionary with the notes that are assinged with it
def Fill_Dict(pairs_Of_Notes):
    note_Dict = {}
    for note_1, note_2 in pairs_Of_Notes:
        if note_1 in note_Dict:
            note_Dict[note_1].append(note_2)
        else:
            note_Dict[note_1] = [note_2]
    return note_Dict


# takes the dict and generates a list of new notes
def Make_List_Of_Notes(dict, full_Note_List, amount_Of_Notes):
    new_Song = []
    note_Num = random.randint(0, len(full_Note_List))
    first_Note = full_Note_List[note_Num]
    new_Song.append(first_Note)
    for i in range(amount_Of_Notes):
        new_Song.append(np.random.choice(dict[new_Song[-1]]))
    return new_Song


# sets the note list into a midi track
def Transform_List_To_Midi(new_Notes_List):
    new_File = mido.MidiFile()
    new_Track = mido.MidiTrack()
    new_File.tracks.append(new_Track)
    for note in new_Notes_List:
        new_Track.append(mido.Message("program_change", program=12, time=0))
        new_Track.append(mido.Message("note_on", note=note, velocity=64, time=32))
        new_Track.append(mido.Message("note_off", note=note, velocity=127, time=100))
    print("your new song is saved")
    new_File.save("your_new_song.mid")


# run everything
og_File = Init_File()
note_List = Read_File(og_File)
pairs_Of_Notes = Make_Pairs(note_List)
note_Dict = Fill_Dict(pairs_Of_Notes)
new_Song = Make_List_Of_Notes(note_Dict, note_List, 40)
Transform_List_To_Midi(new_Song)
