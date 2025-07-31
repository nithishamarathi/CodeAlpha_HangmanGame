import tkinter as tk
from tkinter import scrolledtext

def get_response(user_input):
    user_input = user_input.lower()
    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand."

def send_message():
    user_input = input_box.get()
    if user_input.strip() == "":
        return
    # Display user's message
    chat_area.configure(state='normal')
    chat_area.insert(tk.END, "You: " + user_input + "\n")
    chat_area.configure(state='disabled')
    chat_area.yview(tk.END)

    response = get_response(user_input)
    # Display bot's response
    chat_area.configure(state='normal')
    chat_area.insert(tk.END, "Bot: " + response + "\n")
    chat_area.configure(state='disabled')
    chat_area.yview(tk.END)

    input_box.delete(0, tk.END)

def enter_pressed(event):
    send_message()

# Create main window
window = tk.Tk()
window.title("Simple Chatbot")

# Create conversation text area with scroll
chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, state='disabled', width=50, height=20)
chat_area.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create input box
input_box = tk.Entry(window, width=40)
input_box.grid(row=1, column=0, padx=10, pady=10)
input_box.bind("<Return>", enter_pressed)

# Create send button
send_button = tk.Button(window, text="Send", width=10, command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

window.mainloop()