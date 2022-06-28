#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


import pandas

nato_phon_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_phon_data)

nato_phon_dict = { row.letter:row.code for (index, row) in nato_phon_data.iterrows() }
# print(nato_phon_dict)

user_input = input("Enter word: ")

letter_list = [nato_phon_dict[letter.upper()] for letter in user_input]
print(letter_list)
