import random
import tkinter as tk
import string

def generate_password(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

def display_password(length):
    password = generate_password(length)
    password_display.config(text=f"{length} Digit Password Generated: {password}")

# Main Window
root = tk.Tk()
root.title("GeoPass, v[1.00]")
root.geometry("450x450")

# ASCII Art Label
ascii_art_label = tk.Label(root, text=".---. .----..----. .----.  .--.   .----. .----.\n/   __}| {_ /  {}  \\| {}  }/ {} \\ { {__  { {__\n\\  {_ }| {__\\      /| .--'/  /\\  \\.-._} }.-._} }\n `---' `----'`----' `-'   `-'  `-'`----' `----'")
ascii_art_label.pack()

# Password Displaying Labels
password_display = tk.Label(root, text="")
password_display.pack()

# Buttons to Generate Passwords
button_10 = tk.Button(root, text="Generate 10 Digit Password", command=lambda: display_password(10))
button_10.pack()

button_25 = tk.Button(root, text="Generate 25 Digit Password", command=lambda: display_password(25))
button_25.pack()

button_50 = tk.Button(root, text="Generate 50 Digit Password", command=lambda: display_password(50))
button_50.pack()

button_75 = tk.Button(root, text="Generate 75 Digit Password", command=lambda: display_password(75))
button_75.pack()

# Run the Tkinter event loop
root.mainloop()
