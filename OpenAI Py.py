import tkinter as tk
import openai

# Function to get information for the search term using GPT
def get_information(search_term):
    # Set the OpenAI API key
    openai.api_key = "API_KEY_HERE"

    # Use GPT to generate text for the search term
    prompt = f"What is {search_term}?"
    model_engine = "text-davinci-002"
    completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.5)
    message = completions.choices[0].text

    # Return the generated text
    return message

# Function to display the information in the GUI and enable the copy button
def display_information(information):
    # Clear the label and set the new text
    label.config(text=information)

    # Enable the copy button
    copy_button.config(state="normal")

# Function to copy the information to the clipboard
def copy_information():
    # Copy the text to the clipboard
    root.clipboard_clear()
    root.clipboard_append(label["text"])

    # Disable the copy button
    copy_button.config(state="disabled")

# Create the main window
root = tk.Tk()
root.title("Information Retriever")

# Create the search term entry field
search_term_entry = tk.Entry(root)
search_term_entry.pack()

# Create the search button
search_button = tk.Button(root, text="Search", command=lambda: display_information(get_information(search_term_entry.get())))
search_button.pack()

# Create the label to display the information
label = tk.Label(root, text="")
label.pack()

# Create the copy button
copy_button = tk.Button(root, text="Copy", state="disabled", command=copy_information)
copy_button.pack()

# Run the main loop
root.mainloop()
