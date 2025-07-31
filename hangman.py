import tkinter as tk
import random
from tkinter import messagebox

# Predefined word list
words = ["apple", "tiger", "chair", "river", "plane"]
word = random.choice(words)
guessed = ["_"] * len(word)
guessed_letters = []
wrong_guesses = 0
max_guesses = 6

# Function to update the display
def update_display():
    word_label.config(text="Word: " + " ".join(guessed))
    guesses_label.config(text=f"Wrong guesses left: {max_guesses - wrong_guesses}")
    letters_label.config(text="Guessed letters: " + ", ".join(guessed_letters))

# Function to handle guess
def make_guess():
    global wrong_guesses

    guess = entry.get().lower()
    entry.delete(0, tk.END)

    if len(guess) != 1 or not guess.isalpha():
        messagebox.showwarning("Invalid Input", "Please enter a single letter.")
        return

    if guess in guessed_letters:
        messagebox.showinfo("Already Guessed", "You already guessed that letter.")
        return

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        wrong_guesses += 1

    update_display()

    if "_" not in guessed:
        messagebox.showinfo("Game Over", f"🎉 You won! The word was: {word}")
        root.destroy()
    elif wrong_guesses == max_guesses:
        messagebox.showinfo("Game Over", f"😢 You lost! The word was: {word}")
        root.destroy()

# GUI window
root = tk.Tk()
root.title("Hangman Game")
root.geometry("400x300")

word_label = tk.Label(root, text="Word: " + " ".join(guessed), font=("Arial", 18))
word_label.pack(pady=10)

guesses_label = tk.Label(root, text=f"Wrong guesses left: {max_guesses - wrong_guesses}")
guesses_label.pack()

letters_label = tk.Label(root, text="Guessed letters: ")
letters_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack()

guess_button = tk.Button(root, text="Guess", command=make_guess)
guess_button.pack(pady=10)

update_display()
root.mainloop()