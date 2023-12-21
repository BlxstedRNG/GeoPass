import random
import tkinter as tk
import string

def generate_password(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

def display_password(length):
    password = generate_password(length)
    password_display.config(text=f"""Password:
    {password}""")

def copy_password():
    # Hide the Tkinter window
    root.withdraw()
    # Clear the clipboard
    root.clipboard_clear()
    # Append only the password to the clipboard
    # Use split to separate the text by a colon and take the second element
    root.clipboard_append(password_display.cget("text").split(":")[1].strip())
    # Update the Tkinter window
    root.update()


# Main Window
root = tk.Tk()
root.title("GeoPass, v[1.1]")
root.geometry("450x450")

# Welcome message
welcome_message = tk.Label(root, text="""Welcome to
GeoPass""")
welcome_message.pack()

# Password Displaying Labels
password_display = tk.Label(root, text="")
password_display.pack()

# Buttons to Generate Passwords
button_10 = tk.Button(root, text="Generate 10 char. password", command=lambda: display_password(10))
button_10.pack()

button_25 = tk.Button(root, text="Generate 25 char. password", command=lambda: display_password(25))
button_25.pack()

button_50 = tk.Button(root, text="Generate 50 char. password", command=lambda: display_password(50))
button_50.pack()

button_75 = tk.Button(root, text="Generate 75 char. password", command=lambda: display_password(75))
button_75.pack()

# Button to Copy Password
button_copy = tk.Button(root, text="Copy password", command=copy_password)
button_copy.pack()

# Run the Tkinter event loop
root.mainloop()

