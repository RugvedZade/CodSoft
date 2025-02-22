import tkinter as tk
import random

# Game rules
rules = {
    "Rock": "Scissors",
    "Scissors": "Paper",
    "Paper": "Rock"
}

# Colors for Dark Theme
BG_COLOR = "#1e1e1e"
TEXT_COLOR = "#ffffff"
BUTTON_COLOR = "#333333"
HIGHLIGHT_COLOR = "#ff9800"

# Score tracking
user_score = 0
computer_score = 0

def get_computer_choice():
    return random.choice(list(rules.keys()))

def play(user_choice):
    global user_score, computer_score
    computer_choice = get_computer_choice()

    # Determine the winner
    if user_choice == computer_choice:
        result_text.set(f"It's a tie! 🤝\nComputer also chose {computer_choice}")
    elif rules[user_choice] == computer_choice:
        user_score += 1
        result_text.set(f"You win! 🎉\nComputer chose {computer_choice}")
    else:
        computer_score += 1
        result_text.set(f"You lose! 😢\nComputer chose {computer_choice}")

    score_text.set(f"Score - You: {user_score} | Computer: {computer_score}")

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x500")
root.config(bg=BG_COLOR)

# Title Label
title_label = tk.Label(root, text="Rock ✊ Paper ✋ Scissors ✌️", fg=TEXT_COLOR, bg=BG_COLOR, font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# Result Label
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, fg=HIGHLIGHT_COLOR, bg=BG_COLOR, font=("Arial", 12))
result_label.pack(pady=10)

# Score Label
score_text = tk.StringVar()
score_text.set("Score - You: 0 | Computer: 0")
score_label = tk.Label(root, textvariable=score_text, fg=TEXT_COLOR, bg=BG_COLOR, font=("Arial", 12))
score_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.pack(pady=20)

def create_button(text):
    return tk.Button(button_frame, text=text, font=("Arial", 12, "bold"), fg=TEXT_COLOR, bg=BUTTON_COLOR, width=10, height=2, command=lambda: play(text))

rock_btn = create_button("Rock")
paper_btn = create_button("Paper")
scissors_btn = create_button("Scissors")

rock_btn.grid(row=0, column=0, padx=5, pady=5)
paper_btn.grid(row=0, column=1, padx=5, pady=5)
scissors_btn.grid(row=0, column=2, padx=5, pady=5)

# Run the game window
root.mainloop()
