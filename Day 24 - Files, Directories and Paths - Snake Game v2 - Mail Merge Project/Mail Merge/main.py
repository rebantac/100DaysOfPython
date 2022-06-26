#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as name_file:
    name_list = name_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_matter = letter_file.read()

    for name in name_list:
        name_stripped = name.strip()
        new_letter = letter_matter.replace("[name]", name_stripped)
        with open(f"./Output/ReadyToSend/letter_for_{name_stripped}.txt", mode="w") as send_letter:
            send_letter.write(new_letter)