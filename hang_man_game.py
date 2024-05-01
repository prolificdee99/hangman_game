import random

words = ["python", "java", "kotlin", "javascript", "ruby", "swift"]
chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word]
attempts = 8
incorrect_guesses = []
score = 0

print("Welcome to Hangman!")

while attempts > 0 and '_' in word_display:
    print("\n" + ''.join(word_display))
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
    else:
        print("The letter does not exist")
        if guess not in incorrect_guesses:
            incorrect_guesses.append(guess)
        attempts -= 1

if '_' not in word_display:
    score = attempts * 10  # Assign points based on remaining attempts
    print("You guessed the word")
    print(''.join(word_display))
    print("You survived!")
    print("Your score:", score)
else:
    print("You ran out of attempts. The word was:", chosen_word)
    print("You lost. Try again!")
