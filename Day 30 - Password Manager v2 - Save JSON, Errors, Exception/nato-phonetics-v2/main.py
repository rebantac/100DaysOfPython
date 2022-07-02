# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

letter_is_left = True
while letter_is_left:
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Only letters allowed")
    else:
        letter_is_left = False
print(output_list)
