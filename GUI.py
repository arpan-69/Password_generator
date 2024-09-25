import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pyperclip  # For clipboard functionality
from main import generate_password


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Password Generator")

        # Label and Entry for password length
        tk.Label(root, text="Password Length:").pack(pady=5)
        self.length_var = tk.IntVar(value=8)  # Default length set to 8
        tk.Entry(root, textvariable=self.length_var).pack(pady=5)

        # Label and Combobox for password complexity options
        tk.Label(root, text="Select Password Complexity:").pack(pady=5)
        self.complexity_var = tk.StringVar(value='4.Characters+Numbers+Special characters')  # Default complexity
        complexity_options = ttk.Combobox(
            root,
            textvariable=self.complexity_var,
            values=[
                '1.Only characters',
                '2.Only numbers',
                '3.Characters+Numbers',
                '4.Characters+Numbers+Special characters'
            ]
        )
        complexity_options.pack(pady=5)

        # Button to generate password
        tk.Button(root, text="Generate Password", command=self.generate_password).pack(pady=10)

        # Entry to display generated password (read-only)
        self.password_var = tk.StringVar()
        tk.Entry(root, textvariable=self.password_var, state='readonly', width=30).pack(pady=5)

        # Button to copy generated password to clipboard
        tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard).pack(pady=5)

    def generate_password(self):
        """Generates a password based on user input for length and complexity."""
        try:
            # Fetch the length and complexity selected by the user
            length = self.length_var.get()
            complexity = self.complexity_var.get()

            # Generate the password using the imported function
            password = generate_password(length, complexity)

            if password:
                self.password_var.set(password)
            else:
                raise ValueError("Please select a valid complexity option.")

        except ValueError as error:
            # Display an error message if something goes wrong
            messagebox.showerror("Error", str(error))

    def copy_to_clipboard(self):
        """Copies the generated password to the system clipboard."""
        password = self.password_var.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")
        else:
            messagebox.showwarning("No Password", "Please generate a password first!")