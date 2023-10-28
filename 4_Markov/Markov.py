"""
 # @ Author: Ruben Middelman
 # @ Create Time: 2023-10-28 04:24:28
 # @ Modified by: Ruben Middelman
 # @ Modified time: 2023-10-28 04:59:19
 # @ Description:
    Midi Markov chain that creates a new midi file based on an old midi file
 """
import mido
import random
import numpy as np

midi_File = mido.MidiFile("Fur Elise.mid", clip=True)


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


def Make_List_Of_Notes(dict, full_Note_List, amount_Of_Notes):
    new_Song = []
    note_Num = random.randint(0, len(full_Note_List))
    first_Note = full_Note_List[note_Num]
    new_Song.append(first_Note)
    for i in range(amount_Of_Notes):
        new_Song.append(np.random.choice(dict[new_Song[-1]]))
    return new_Song


note_List = Read_File(midi_File)
pairs_Of_Notes = Make_Pairs(note_List)
note_Dict = Fill_Dict(pairs_Of_Notes)
new_Song = Make_List_Of_Notes(note_Dict, note_List, 40)
print(new_Song)
