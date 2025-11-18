import random

words = ["apple", "banana", "cherry", "grape", "orange"]
hidden_word = random.choice(words)
secret = ['_']* len(hidden_word)
wrong = 0
maxite = 6

correct = []
while wrong < maxite and '_' in secret:
    guess = input("Guess the letter: ")
    if guess in correct:
        print("You already guessed it.")
    else:
        if guess in hidden_word:
            for i in range(len(hidden_word)):
                if hidden_word[i] == guess:
                    secret[i] = guess
            correct.append(guess)
            print("you guessed correctly")
        else:
            wrong +=1
            print("Wrong Guess")
            print(f"{maxite - wrong} guess left")

print("Current Word:", " ".join(secret))
if '_' not in secret:
    print("Congratulations!!! You guessed correctly", hidden_word)
else:
    print("You ran out of moves. The word is: ", hidden_word)
