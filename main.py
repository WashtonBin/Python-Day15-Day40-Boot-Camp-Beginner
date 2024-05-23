#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"
with open("./Input/Letters/starting_letter.txt") as read_invited:
    read_invitation = read_invited.read()

with open ("./Input/Names/invited_names.txt") as name_file:
    contents = name_file.readlines()
    for i in range(8):
        content_space = contents[i].strip()
        with open(f"./Output/ReadyToSend/{content_space}.txt", mode="w") as write_letter:
            replace_invited_name = read_invitation.replace(PLACEHOLDER, content_space)
            write_letter.write(replace_invited_name)

read_invited.close()
name_file.close()
write_letter.close()

##