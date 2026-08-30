# moormonkey, 03/07/2025
# A program to practice subtracting Polybius square numbers (two-digit numbers where each digit is from 1-5, ie 11, 51, 15, 55).
# Randomly generates a "cipher number" (two Polybius square numbers added together) and a "key number" (what to subtract from it).

import random

def getPolybiusNumber():
    return 10 * random.randint(1, 5) + random.randint(1, 5)

print("\033[2J\033[1;1HType EXIT to exit the program, type KEY to generate a new key number, or type any integer to see if you subtracted correctly.")
key = getPolybiusNumber()
text = "KEY"
count = 0
correct = 0
cipher = 0
while text != "EXIT":
    if text == "KEY":
        key = getPolybiusNumber()
        print(f"\033[2;1HYour key is {key}\033[4;1H\033[K")
    else:
        try:
            text = int(text)
            count += 1
            if text == cipher:
                correct += 1
                print(f"\033[4;1H\033[K{text} is correct!")
            else:
                print(f"\033[4;1H\033[K{text} is incorrect. The answer was {cipher}.")
        except:
            pass
    cipher = getPolybiusNumber()
    text = input(f"\033[3;1H\033[K{cipher + key} ").upper()
print(f"\033[4;1H\033[KSession complete. You got {correct} out of {count} correct.")