
def arrondir_notes(notes) :
    result =[] 
    for note in notes :
        if note < 40 :
            result.append(note)
        else : 
            result.append(note) 
    return result

notes = [38, 42, 83, 76, 89, 71, 59]
notes_arrondies = arrondir_notes(notes)
print(notes_arrondies)               

#round
#arrondiSuperieur