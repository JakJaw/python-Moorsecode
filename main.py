from code import Morse

def split(text):
    return [char for char in text]

on = True
while on:
    final_text = []
    text = str(input("Write what u wanna say in Morse Code: ")).upper()

    splitted = split(text)
    for letter in splitted:
        final_text.append(f"{Morse[letter]} ")

    print("Your Morse code is: \n"," ".join(final_text))
    exit = str(input("Do u wanna convert more words? (Y/N): "))
    if exit == "N":
        on = False
print("Goodbye...")