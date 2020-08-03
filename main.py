import random
import string

def randomPasswordGenerator(length):
    numbers = string.digits
    letters = string.ascii_letters
    punctuations = string.punctuation
    allCharacter = numbers+letters+punctuations

    randomSequence = random.Random.choices(random,population=allCharacter,k=length)
    randomPassword = "" 
    for element in randomSequence:
        randomPassword += element

    return randomPassword 

while True:
    print("Random Password Generator")
    passwrdLength = input("Enter the Lenth of the Password")

    if passwrdLength.isdigit():
        print(f"Password Generated >>> {randomPasswordGenerator(int(passwrdLength))}")
        inputP = input("Do you want to Generate another Password?(y/n) ")
        if inputP.lower()=="y":
            continue
        else:
            exit()
    else:
        print("Enter a Valid Password.")
        continue