with open("./Input/Names/invited_names.txt.txt", mode="r") as n:
    names = n.read().splitlines()

with open("./Input/Letters/starting_letter.txt.txt", mode="r") as letter:
    letter_example = letter.read()
    for name in names:
        with open(f"./Output/ReadyToSend/{name}_letter.txt", mode="w") as letters:
            letters.write(letter_example.replace("[name]", f"{name}"))
