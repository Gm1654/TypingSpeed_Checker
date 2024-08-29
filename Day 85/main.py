import tkinter as tk
from tkinter import messagebox
import time
import difflib

# Sample text for the user to type
sample_text = ("The quick brown fox jumps over the lazy dog. "
               "This sentence contains every letter of the alphabet, "
               "which makes it perfect for a typing test.")

class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("600x400")

        # Instruction label
        self.label = tk.Label(root, text="Type the following text as quickly as you can:", font=("Arial", 14))
        self.label.pack(pady=10)

        # Sample text label
        self.sample_text_label = tk.Label(root, text=sample_text, font=("Arial", 12), wraplength=580)
        self.sample_text_label.pack(pady=10)

        # Text entry widget for typing
        self.text_entry = tk.Text(root, height=10, font=("Arial", 12), wrap='word')
        self.text_entry.pack(pady=10)
        self.text_entry.config(state=tk.DISABLED)  # Disable until start

        # Start button
        self.start_button = tk.Button(root, text="Start", command=self.start_test, font=("Arial", 12))
        self.start_button.pack(pady=5)

        # Result label
        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        self.start_time = None

    def start_test(self):
        # Reset the text entry box and result label
        self.text_entry.config(state=tk.NORMAL)  # Enable typing
        self.text_entry.delete(1.0, tk.END)
        self.result_label.config(text="")
        
        # Start timing and enable typing
        self.start_time = time.time()
        self.text_entry.bind("<KeyRelease>", self.check_typing)
        self.text_entry.focus()

    def check_typing(self, event):
        typed_text = self.text_entry.get(1.0, tk.END).strip()

        # Calculate accuracy based on the length of the typed text
        sample_fragment = sample_text[:len(typed_text)]
        matcher = difflib.SequenceMatcher(None, sample_fragment.lower(), typed_text.lower())
        accuracy = matcher.ratio() * 100  # Convert ratio to percentage

        # Update the result label with dynamic accuracy
        self.result_label.config(text=f"Accuracy: {accuracy:.2f}%")

        # Check if the user has finished typing the sample text
        if typed_text.lower().replace(" ", "").replace("\n", "") == sample_text.lower().replace(" ", "").replace("\n", ""):
            self.end_test()

    def end_test(self):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        words_typed = len(sample_text.split())
        wpm = (words_typed / elapsed_time) * 60

        # Display the final result with typing speed and accuracy
        final_text = self.text_entry.get(1.0, tk.END).strip()
        matcher = difflib.SequenceMatcher(None, sample_text.lower(), final_text.lower())
        final_accuracy = matcher.ratio() * 100  # Convert ratio to percentage

        self.result_label.config(text=f"Your typing speed is: {int(wpm)} words per minute\nAccuracy: {final_accuracy:.2f}%")
        self.text_entry.unbind("<KeyRelease>")
        self.text_entry.config(state=tk.DISABLED)  # Disable typing after completion
        messagebox.showinfo("Test Complete", f"Your typing speed is: {int(wpm)} WPM\nAccuracy: {final_accuracy:.2f}%")

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedApp(root)
    root.mainloop()







































# from tkinter import *
# import random
# import time

# class TypingSpeedTest:
#     def __init__(self, window):
#         self.window = window
#         self.window.title("Typing Speed Test")

#         # A list of sentences to randomly choose from
#         self.sentences = [
#             "The quick brown fox jumps over the lazy dog.",
#             "Python is a powerful and versatile programming language.",
#             "Practice makes perfect.",
#         ]
#         self.current_sentence = ""
#         self.typing_start_time = None
#         self.typing_finished = False

#         self.title_label = Label(window, text="Typing Speed Text", font=("Times New Roman", 24, "bold"), padx=200)
#         self.title_label.grid(row=0, column=1)

#         # Displaying the random sentences
#         self.sentence_label = Label(window, text="", font=("Arial", 16))
#         self.sentence_label.grid(row=1, column=1)

#         # place for users to type in
#         self.entry = Entry(window, font=("Arial", 14))
#         self.entry.grid(row=2, column=1)

#         # view the results
#         self.result_label = Label(window, text="Typing Speed: \nAccuracy:", font=("Arial", 14))
#         self.result_label.grid(row=3, column=1)

#         # start button
#         self.start_button = Button(window, text="Start Typing Test", command=self.start_typing_test, font=("Arial", 14))
#         self.start_button.grid(row=4, column=1)

#     def start_typing_test(self):
#         # start the game
#         if not self.typing_finished:
#             self.current_sentence = random.choice(self.sentences)
#             self.sentence_label.config(text=self.current_sentence)
#             self.entry.delete(0, END)
#             self.result_label.config(text="Typing Speed: \nAccuracy:")
#             self.typing_start_time = time.time()
#             self.start_button.config(text="Finish Typing Test")
#             self.typing_finished = True
#         else:
#             # end the game
#             typed_text = self.entry.get()
#             elapsed_time = time.time() - self.typing_start_time
#             words = typed_text.split()
#             word_count = len(words)

#             # Calculate typing speed in words per minute (WPM)
#             wpm = int((word_count / elapsed_time) * 60)

#             # Check accuracy
#             accuracy = self.calculate_accuracy(typed_text, self.current_sentence)

#             # Display the result
#             result_text = f"Typing Speed: {wpm} WPM\nAccuracy: {accuracy}%"
#             self.result_label.config(text=result_text)

#             self.start_button.config(text="Start Again")
#             self.typing_finished = False

#     def calculate_accuracy(self, typed_text, original_text):
#         typed_words = typed_text.split()
#         original_words = original_text.split()

#         correct_words = 0

#         for typed_word, original_word in zip(typed_words, original_words):
#             if typed_word == original_word:
#                 correct_words += 1

#         accuracy = (correct_words / len(original_words)) * 100
#         return round(accuracy, 2)


# root = Tk()
# app = TypingSpeedTest(root)
# root.mainloop()