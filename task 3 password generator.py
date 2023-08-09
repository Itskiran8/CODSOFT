import tkinter as tk
import random
import string

def generate_password():
    # length of the password
    length = int(length_entry.get())

    # pool of characters to generate password from
    characters = string.ascii_letters + string.digits + string.punctuation

    # generate random password by selecting characters from the pool
    password = ''.join(random.choice(characters) for _ in range(length))

    # display the generated password in the result label
    result_label.config(text=password)

# create the GUI window
window = tk.Tk()
window.title("Password Generator")

# create a label for the length input
length_label = tk.Label(window, text="Password Length:")
length_label.pack()

# create an entry field for inputting the password length
length_entry = tk.Entry(window)
length_entry.pack()

# create a button to generate password
generate_button = tk.Button(window, text="Generate", command=generate_password)
generate_button.pack()

# create a label to display the generated password
result_label = tk.Label(window, text="")
result_label.pack()

# create a gui window
window.geometry("250x200")
# start the GUI event loop
window.mainloop()