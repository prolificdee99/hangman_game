import random

# Hangman stages (visual representation)
HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ==="""
]

# Word list (you can expand it)
WORDS = ["python", "programming", "hangman", "student", "developer", "github"]

def choose_word():
    return random.choice(WORDS)

def play_hangman():
    word = choose_word()
    guessed = ["_"] * len(word)
    guessed_letters = set()
    attempts = len(HANGMAN_PICS) - 1

    print("🎮 Welcome to Hangman Game!")
    print("Guess the word, one letter at a time.\n")

    while attempts > 0 and "_" in guessed:
        print(HANGMAN_PICS[len(HANGMAN_PICS) - 1 - attempts])
        print("Word:", " ".join(guessed))
        print(f"Attempts left: {attempts}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}\n")

        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ Good guess!\n")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
        else:
            print("❌ Wrong guess!\n")
            attempts -= 1

    # End of game
    if "_" not in guessed:
        print("🎉 Congratulations! You guessed the word:", word)
    else:
        print(HANGMAN_PICS[-1])
        print("💀 Game Over! The word was:", word)

# Main loop
if __name__ == "__main__":
    while True:
        play_hangman()
        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("👋 Thanks for playing Hangman!")
            break
