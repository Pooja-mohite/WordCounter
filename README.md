# Word Counter Application

## Overview
This is a simple Python application that counts the number of words in a text input by the user. It uses the Tkinter library to provide a graphical user interface (GUI) where users can enter their text, and upon clicking a button, the number of words in the text is displayed in a pop-up message box.

## Requirements
- Python 3.x (ensure that Tkinter is installed with your Python installation)

## How to Run the Application

1. **Install Python**:
   - Make sure you have Python 3.x installed. If you don't, download and install it from [https://www.python.org/downloads/](https://www.python.org/downloads/).

2. **Install Tkinter**:
   - Tkinter is included with Python by default, but if it is not available, you can install it using the following command (depending on your operating system):
     - For Windows/macOS/Linux: Tkinter is usually included by default with Python.
     - On Ubuntu/Linux, use: `sudo apt-get install python3-tk`.

3. **Save the Python Script**:
   - Save the code as `word_counter.py` (or any name you prefer with `.py` extension).

4. **Run the Application**:
   - Open a terminal (command prompt) and navigate to the directory where the `word_counter.py` script is saved.
   - Run the script using the command: 
     ```
     python word_counter.py
     ```
     This will open the Word Counter application.

## Functionality
- **Text Input**: Users can type or paste any text into the text box.
- **Count Words**: After entering the text, users can click the "Count Words" button to calculate the number of words in the input.
- **Message Box**: If the text input is empty, an error message will appear asking the user to enter some text. Otherwise, the word count will be displayed in a pop-up message box.

## Code Explanation

- **count_words function**: This function retrieves the text entered by the user in the Text widget, splits the text into words, counts the number of words, and displays the result in a message box.
- **Tkinter Widgets**:
  - **Label**: Displays a prompt to the user to "Enter your text below".
  - **Text Widget**: A multi-line text box where the user can enter the text.
  - **Button**: When clicked, this triggers the `count_words` function to count and display the word count.


