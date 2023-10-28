"""
 # @ Author: Ruben Middelman
 # @ Create Time: 2023-10-28 04:24:28
 # @ Modified by: Ruben Middelman
 # @ Modified time: 2023-10-28 04:59:19
 # @ Description:
    Midi Markov chain that creates a new midi file based on an old midi file
 """

import mido

midi_File = mido.MidiFile("Fur Elise.mid", clip=True)


# Reads a MIDI file and adds all the notes to the list
def Read_File(file):
    message_List = []
    for msg in file:
        if msg.type == "note_on":
            message = [msg.note, msg.velocity]
            message_List.append(message)
    return message_List


def Apply_Markov(List_Of_Notes):
    i = 0
    multiple_Notes = []
    for notes in List_Of_Notes:
        initial_Note = notes[0]
        for notes_2 in List_Of_Notes:
            if initial_Note == notes_2[0]:
                if (i + 1) <= len(List_Of_Notes):
                    Two_Notes_Togheter = [notes, List_Of_Notes[i + 1]]
                    multiple_Notes.append(Two_Notes_Togheter)
            i += 1
    return multiple_Notes


print(Apply_Markov(Read_File(midi_File)))
