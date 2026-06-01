import random

colors = ["red", "blue", "green", "black", "white"]
word = random.choice(colors)
guessed = "_" * len(word)
wrong = 0

while wrong < 6 and "_" in guessed:
    print("\n", guessed)
    letter = input("Enter a letter: ").lower()
    new_word = ""

    for i in range(len(word)):
        if word[i] == letter or word[i] in guessed:
            new_word += word[i] + " "
        else:
            new_word += "_ "

    if guessed == new_word:
        wrong += 1
        print("Wrong Guess!")

    guessed = new_word

if "_" not in guessed:
    print("🎉 You Won! Word is:", word)
else:
    print("😢 You Lost! Word is:", word)
