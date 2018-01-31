morse_dictionary = { # PROVIDES TRANSLATION FROM ALPHABET TO MORSE
    'A' : ".-",
    'B' : "-...",
    'C' : "-.-.",
    'D' : "-..",
    'E' : ".",
    'F' : "..-.",
    'G' : "--.",
    'H' : "....",
    'I' : "..",
    'J' : ".---",
    'K' : "-.-",
    'L' : ".-..",
    'M' : "--",
    'N' : "-.",
    'O' : "---",
    'P' : ".--.",
    'Q' : "--.-",
    'R' : ".-.",
    'S' : "...",
    'T' : "-",
    'U' : "..-",
    'V' : "...-",
    'W' : ".--",
    'X' : "-..-",
    'Y' : "-.--",
    'Z' : "--..",
    '1' : ".----",
    '2' : "..---",
    '3' : "...--",
    '4' : "....-",
    '5' : ".....",
    '6' : "-....",
    '7' : "--...",
    '8' : "---..",
    '9' : "----.",
    '0' : "-----"
}

alpha_dictionary = { # PROVIDES TRANSLATION FROM MORSE TO ALPHABET
    '.-' : "A",
    '-...' : "B",
    '-.-.' : "C",
    '-..' : "D",
    '.' : "E",
    '..-.' : "F",
    '--.' : "G",
    '....' : "H",
    '..' : "I",
    '.---' : "J",
    '-.-' : "K",
    '.-..' : "L",
    '--' : "M",
    '-.' : "N",
    '---' : "O",
    '.--.' : "P",
    '--.-' : "Q",
    '.-.' : "R",
    '...' : "S",
    '-' : "T",
    '..-' : "U",
    '...-' : "V",
    '.--' : "W",
    '-..-' : "X",
    '-.--' : "Y",
    '--..' : "Z",
    '.----' : "1",
    '..---' : "2",
    '...--' : "3",
    '....-' : "4",
    '.....' : "5",
    '-....' : "6",
    '--...' : "7",
    '---..' : "8",
    '----.' : "9",
    '-----' : "0"
}

def file_load(path,option): # SAFELY OPENS A FILE
    try:
        file = open(path,option) # USING PATH AND OPERATION
    except IOError: # IF AN ERROR IS THROWN WHILE OPENING
        print("NULL FILE RETURNED")
        file = None # RETURNS NONE AND IS HANDLED LATER
    return file

def get_data(file): # GET DATA FROM FILE
    morse_list = [] # DATA VARIABLE
    for line in file: # ITERATES LINE BY LINE
        morse_list.append(line)
    if not(len(morse_list) == 0):
        return morse_list
    return None # RETURN NONE IF THE FILE LIST IS EMPTY

def translate_morse(data_line): # TRANSLATES FROM MORSE TO ALPHABET
    piece = "" # TEMPORARY HOLDER
    final_data = "" # FINAL OUTPUT STRING
    for character in data_line: # FOR EACH CHARACTER IN LINE
        if (character == ' '): # SPACE INDICATES THAT A LETTER HAS BEEN PASSED
            if not (piece == ""):
                final_data += alpha_dictionary[piece] # ADDS THE LETTER USING THE DICTIONARY
            piece = "" # RESETS THE HOLDER
            continue
        if (character == '/'): # SLASH INDICATES THAT THE CHARACTER IS SPACE
            if not(piece == ""):
                final_data += alpha_dictionary[piece] # IF THERE EXISTS DATA IN THE HOLDER ITS ADDED
            final_data += ' ' # ADDS THE EXPECTED SPACE
            piece = ""
            continue
        piece += character # ADDS THE MORSE CHARACTER
    if not(piece == ""):
        final_data += alpha_dictionary[piece]
    return final_data

def translate_alpha(data_line): # TRANSLATES FROM ALPHABET TO MORSE
    final_data = "" # FINAL OUTPUT DATA
    for character in data_line: # ITERATES THROUGH ALL CHARACTERS IN LINE
        if (character == ' '): # IF CHARACTER IS SPACE IT ADDS SLASH
            piece = '/ '
            final_data += piece
            continue
        if (character == "\n"):
            break
        piece = morse_dictionary[character.upper()] # CONVERTS THE ALPHA CHARACTER TO MORSE USING THE DICTIONARY
        final_data += piece # ADDS THE CONVERTED CHARACTER
        final_data += ' '
    return final_data[:-1] # RETURNS THE FINAL DATA EXCEPT FOR THE LAST SPACE

if __name__ == "__main__":
    final_list = [] # DATA LIST
    data_file = file_load("C:/Users/Akatosh/Desktop/Akatosh/Explorer/Morse_Code.txt","r") # OPENS A FILE
    raw_data = get_data(data_file) # GETS THE FILE DATA
    if (raw_data == None): # ENDS IF NO DATA IS PRESENTED
        print("NO DATA OBTAINED")
        quit()
    for item in raw_data: # ITERATES LINE BY LINE IN DATA
        final_list.append(translate_alpha(item)) # TRANSLATES EVERY LINE
    print(final_list) # PRINTS THE FINAL PRODUCT
    for child in final_list:
        print(translate_morse(child))
    quit()
