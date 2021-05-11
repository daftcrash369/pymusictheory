import random

# Public API
def GenerateRandomScale():
    scaleRoot = random.choice(westernNotes)
    scaleId = random.randrange(len(scaleTypes))
    return [ MakeScale_Interal( scaleRoot, scaleTypes[scaleId] ), scaleRoot, scaleNames[scaleId] ]

def GenerateRandomChord():
    chordRoot = random.choice(westernNotes)
    chordId = random.randrange(len(chordTypes))
    return [ MakeChord_Interal( chordRoot, chordTypes[chordId] ), chordRoot, chordNames[chordId] ]

def MakeScaleByName( rootNote, scaleFormName ):    
    return MakeScale_Interal( rootNote, scaleTypes[GetScaleFormIndex_Interal(scaleFormName.lower())] )

def MakeChordByName( rootNote, chordFormName ):    
    return MakeChord_Interal( rootNote, chordTypes[GetChordFormIndex_Interal(chordFormName.lower())] )

# Interal functions
def MakeScale_Interal( root, scaleForm ):
    rootNodeIndex = GetRootNodeIndex_Internal(root)
    return ApplyAndReturnForm_Internal(rootNodeIndex, scaleForm)

def MakeChord_Interal( root, chordForm ):
    rootNoteIndex = GetRootNodeIndex_Internal(root)
    return ApplyAndReturnForm_Internal(rootNoteIndex, chordForm)

def ApplyAndReturnForm_Internal( rootNodeIndex, form ):
    structureNotes = []
    structureNotes.append(westernNotes[rootNodeIndex])

    numberOfNotes = len(westernNotes)
    nextIndex = rootNodeIndex
    for i in range(len(form)):
        nextIndex = (rootNodeIndex + form[i]) % numberOfNotes
        structureNotes.append(westernNotes[nextIndex])
    return structureNotes

def GetRootNodeIndex_Internal( rootNote ):
    for i in range(len(westernNotes)):
        note = westernNotes[i]
        if( note == rootNote ):
            return i

def GetScaleFormIndex_Interal( scaleName ):
    for i in range(len(scaleNames)):
        if( scaleNames[i].lower() == scaleName ):
            return i

def GetChordFormIndex_Interal( chordName ):
    for i in range(len(chordNames)):
        if( chordNames[i].lower() == chordName ):
            return i

#Data
westernNotes = [
    "A", "A#",
    "B",
    "C", "C#",
    "D", "D#",
    "E",
    "F", "F#",
    "G", "G#",
]

scaleNames       = [ "Maj", "min", "harmonic", "melodic", "ionian", "dorian", "phrygian", "lydian", "mixolydian", "aeolian", "locrian"]
majorScale       = [ 2, 4, 5, 7, 9, 11 ]
minorScale       = [ 2, 3, 5, 7, 8, 10 ]
harmonicMinScale = [ 2, 3, 5, 7, 8, 11 ]
melodicMinScale  = [ 2, 3, 5, 7, 9, 11 ]
ionianScale      = [ 2, 4, 5, 7, 9, 11 ]
dorianScale      = [ 2, 3, 5, 7, 9, 10 ]
phrygianScale    = [ 1, 3, 5, 7, 8, 10 ]
lydianScale      = [ 2, 4, 6, 7, 9, 11 ]
mixolydianScale  = [ 2, 4, 5, 7, 9, 10 ]
aeolianScale     = [ 2, 3, 5, 7, 8, 10 ]
locrianScale     = [ 1, 3, 4, 6, 8, 10, 11 ]
scaleTypes       = [ majorScale, minorScale, harmonicMinScale, melodicMinScale, ionianScale, dorianScale, phrygianScale, lydianScale, mixolydianScale, aeolianScale, locrianScale ]


chordNames   = [ "Maj", "min", "dim", "Maj7", "min7", "dom7", "sus2", "sus4", "aug", "aug7" ]
majorChord   = [ 4, 7 ]
minorChord   = [ 3, 7 ]
dimChord     = [ 3, 6 ]
maj7Chord    = [ 4, 7, 11 ]
min7Chord    = [ 3, 7, 10 ]
dom7Chord    = [ 4, 7, 10 ]
sus2Chord    = [ 2, 7 ]
sus4Chord    = [ 5, 7 ]
augChord     = [ 4, 8 ]
dim7Chord    = [ 3, 6, 9]
aug7Chord    = [ 4, 8, 10 ]
minMaj7Chord = [ 3, 7, 11 ]
maj9Chord    = [ 4, 7, 11, 14 ]
min9Chord    = [ 3, 7, 10, 14 ]
minMaj9Chord = [ 3, 7, 11, 14 ]
sharp11Chord = [ 4, 7, 11, 18 ] # (#11)
lydDomChord  = [ 4, 7, 10, 18 ] #lydian dominant
six9Chord    = [ 4, 7, 9, 14 ] #6/9 chord
dom7flat5Chord = [ 4, 6, 10 ] #half-diminished
chordTypes   = [ majorChord, minorChord, dimChord, maj7Chord, min7Chord, dom7Chord, sus2Chord, sus4Chord, augChord, aug7Chord ]
