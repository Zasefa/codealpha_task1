import random

words = {
    "Programming Languages": ["python", "java", "cpp"],
    "Fruits": ["apple", "banana", "mango"],
    "Animals": ["tiger", "lion", "zebra"]
}

category = random.choice(list(words.keys()))
secret_word = random.choice(words[category])

display = ["_"] * len(secret_word)
lives = 6
guessed_letters = []

print("Welcome to Hangman!")
print("Category:", category)

while lives > 0:

    print("\nWord:", " ".join(display))
    print("Lives left:", lives)

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:

        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display[i] = guess

        print("Correct!")

    else:
        lives -= 1
        print("Wrong Guess!")

    if "_" not in display:
        print("\nCongratulations!")
        print("You guessed the word:", secret_word)
        break

if lives == 0:
    print("\nGame Over!")
    print("The word was:", secret_word)    