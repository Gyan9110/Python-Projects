import tkinter as tk
import webbrowser
from tkinter import ttk, messagebox

# Encryption
def encryption(st, shift):
    result = ""
    for i in st:
        if i == " ":
            result += " "
            continue
        if i.isupper():
            result += chr(((ord(i) - ord("A") + shift) % 26) + ord("A"))
        else:
            result += chr(((ord(i) - ord("a") + shift) % 26) + ord("a"))
    return result

# Decryption
def decryption(st2, shift2):
    result = ""
    for i in st2:
        if i == " ":
            result += " "
            continue
        if i.isupper():
            result += chr(((ord(i) - ord("A") - shift2) % 26) + ord("A"))
        else:
            result += chr(((ord(i) - ord("a") - shift2) % 26) + ord("a"))
    return result

def encrypt():
    text = entry_text.get()
    shift = int(entry_shift.get())
    encrypted_text = encryption(text, shift)
    result_label.config(text=f"Encrypted text: {encrypted_text}", bg="wheat")

def decrypt():
    text = entry_text.get()
    shift = int(entry_shift.get())
    decrypted_text = decryption(text, shift)
    result_label.config(text=f"Decrypted text: {decrypted_text}", bg="wheat")

def callback(url):
    webbrowser.open_new(url)

def on_enter(event):
    event.widget.config(bg='lightblue')

def on_leave(event):
    event.widget.config(bg='white')

# Create the main window
root = tk.Tk()
root.title("Encryption/Decryption GUI")
root.iconbitmap(r"pic.ico")
root.geometry("500x400")
root.minsize(400, 300)
root.maxsize(500, 400)
root.config(bg="wheat")
win = tk.Label(root, text="CEASER CIPHER ENCRYPTION / DECRYPTION", font=("Times New Roman", 16), bg="wheat")
win.pack(pady=15)
foot = tk.Label(root, text="MADE BY : Gyan Gupta", font="Arial 9 bold", cursor="hand2")
foot.pack(side="bottom", anchor="s", fill=tk.X)
foot.bind("<Button-1>", lambda e: callback("https://github.com/Gyan9110/pygameWorks"))
foot.bind("<Enter>", on_enter)
foot.bind("<Leave>", on_leave)

# Create and place widgets
label_text = tk.Label(root, text="Enter text:", bg="wheat")
label_text.pack(pady=5)
entry_text = tk.Entry(root, width=50)
entry_text.pack(pady=5)

label_shift = tk.Label(root, text="Enter shift key:", bg="wheat")
label_shift.pack(pady=5)
entry_shift = tk.Entry(root, width=10)
entry_shift.pack(pady=5)

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt, relief=tk.RIDGE, cursor="hand2")
encrypt_button.pack(pady=10)
encrypt_button.bind("<Enter>", on_enter)
encrypt_button.bind("<Leave>", on_leave)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt, relief=tk.RIDGE, cursor="hand2")
decrypt_button.pack(pady=10)
decrypt_button.bind("<Enter>", on_enter)
decrypt_button.bind("<Leave>", on_leave)

result_label = tk.Label(root, text="")
result_label.pack(pady=20)

# Run the application
root.mainloop()
