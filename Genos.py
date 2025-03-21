import sys
import tkinter as tk
from tkinter import messagebox
from assistant import greetMe, speak
from search import searchGoogle, searchYoutube, searchWikipedia
from utils import takeCommand
from Dictapp import openappweb, closeappweb

def hear_me():
    query = entry.get()
    if query:
        print(f"Query: {query}")
        # Call your existing functions here
        # For example: process_query(query)
    else:
        messagebox.showwarning("Input Error", "Please enter a query.")

def main():
    is_awake = False  # Track if the assistant is awake or not

    while True:
        query = takeCommand().lower().strip()
        if not query or query == "none":
            continue  # Skip empty inputs

        print(f"Captured command: {query}")  # Debugging statement

        # Exit or sleep mode
        if any(cmd in query for cmd in ["exit", "terminate", "quit", "shutdown", "sleep mode"]):
            speak("Goodbye, Buddy! Going into sleep mode.")
            sys.exit()

        if not is_awake:
            if "wake up" in query:
                greetMe()
                is_awake = True
            continue  # Skip processing if not awake

        # Basic responses
        responses = {
            "hello": "Hello Buddy, how are you?",
            "i am fine": "That's great to hear.",
            "how are you": "Perfect!",
            "thank you": "You're welcome."
        }
        for key, response in responses.items():
            if key in query:
                speak(response)
                break  # Stop after the first match

        # Function Calls
        if "open" in query:
            openappweb(query)
        elif "close" in query:
            closeappweb(query)
        elif "google" in query:
            searchGoogle(query)
        elif "youtube" in query:
            searchYoutube(query)
        elif "wikipedia" in query:
            searchWikipedia(query)

# Create the main window for the UI
root = tk.Tk()
root.title("Personalized AI Assistant 🤖")
root.geometry("400x200")
root.configure(bg="#e0f7fa")

# Create the entry text box
entry = tk.Entry(root, width=30, font=("Arial", 14), bg="#f0f8ff")
entry.pack(pady=20)

# Create the hearing button
hear_button = tk.Button(root, text="🎤 Hear Me", command=hear_me, bg="#4CAF50", fg="white", font=("Arial", 12))
hear_button.pack(pady=10)

# Run the application
if __name__ == "__main__":
    root.mainloop()