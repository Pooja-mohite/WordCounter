import tkinter as tk
from tkinter import messagebox

def count_words():
    """
    Counts the number of words in the input text from the user and displays the result.
    """
    user_text = text_input.get("1.0", tk.END).strip()  # Get text from the Text widget
    if not user_text:
        # Show an error message if the input is empty
        messagebox.showerror("Error", "Please enter some text to count the words.")
        return
    
    word_count = len(user_text.split())  # Count words
    # Display the word count in a message box
    messagebox.showinfo("Word Count", f"The number of words in your text is: {word_count}")

# Create the main window
root = tk.Tk()
root.title("Word Counter")
root.geometry("400x300")  # Set the window size

# Add a label to instruct the user
label = tk.Label(root, text="Enter your text below:", font=("Arial", 14))
label.pack(pady=10)

# Add a text widget for user input
text_input = tk.Text(root, wrap="word", height=10, font=("Arial", 12))
text_input.pack(padx=10, pady=10, expand=True, fill="both")

# Add a button to trigger the word count
count_button = tk.Button(root, text="Count Words", font=("Arial", 12), command=count_words)
count_button.pack(pady=10)

# Run the application
root.mainloop()
