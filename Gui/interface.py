import tkinter as tk
from tkinter import messagebox

from logic import generate_strong_password, save_password, classify_password_strength


def create_gui():
    window = tk.Tk()
    window.title("Password Generator")
    window.geometry("400x500")
    window.resizable(False, False)
    window.configure(bg="#f0f0f0")

    # Password Length
    tk.Label(window, text="Password Length:", bg="#f0f0f0").pack(pady=10)
    length_entry = tk.Entry(window, width=10)
    length_entry.pack()

    # Checkboxes Frame
    checkbox_frame = tk.Frame(window, bg="#f0f0f0")
    checkbox_frame.pack(pady=10)

    use_upper = tk.BooleanVar(value=True)
    use_lower = tk.BooleanVar(value=True)
    use_digits = tk.BooleanVar(value=True)
    use_punct = tk.BooleanVar(value=True)

    tk.Checkbutton(checkbox_frame, text="Include Uppercase", variable=use_upper, bg="#f0f0f0").pack(anchor='w')
    tk.Checkbutton(checkbox_frame, text="Include Lowercase", variable=use_lower, bg="#f0f0f0").pack(anchor='w')
    tk.Checkbutton(checkbox_frame, text="Include Digits", variable=use_digits, bg="#f0f0f0").pack(anchor='w')
    tk.Checkbutton(checkbox_frame, text="Include Punctuation", variable=use_punct, bg="#f0f0f0").pack(anchor='w')

    # Output
    tk.Label(window, text="Generated Password:", bg="#f0f0f0").pack(pady=5)
    output_entry = tk.Entry(window, width=40, justify='center', font=("Courier", 12), state='readonly')
    output_entry.pack(pady=5)

    # Strength Label
    strength_label = tk.Label(window, text="", bg="#f0f0f0", fg="blue")
    strength_label.pack(pady=5)

    # Generate Handler
    def generate_and_show():
        try:
            length_str = length_entry.get()
            if not length_str.strip():
                raise ValueError("Password length cannot be empty.")

            length = int(length_str)
            if length < 1:
                raise ValueError("Length must be >= 1")
        except ValueError as e:
            messagebox.showerror("Invalid Input", f"Invalid input: {e}")
            return  # 🚫 Blocca la generazione

        password = generate_strong_password(length, use_upper.get(), use_lower.get(), use_digits.get(), use_punct.get())
        if password:
            output_entry.config(state='normal')
            output_entry.delete(0, tk.END)
            output_entry.insert(0, password)
            output_entry.config(state='readonly')

            strength = classify_password_strength(password)
            colors = {"Weak": "red", "Medium": "orange", "Strong": "green"}
            strength_label.config(text=f"Strength: {strength}", fg=colors.get(strength, "blue"))
        else:
            messagebox.showwarning("Selection Missing", "Please select at least one character set.")

    # Save Handler
    def save_password_handler():
        password = output_entry.get()
        if password:
            save_password("passwords.txt", password)
            messagebox.showinfo("Saved", "Password saved to passwords.txt.")
        else:
            messagebox.showwarning("No Password", "Please generate a password first.")

    # Buttons
    tk.Button(window, text="Generate", command=generate_and_show).pack(pady=5)
    tk.Button(window, text="Save", command=save_password_handler).pack()

    # Hotkey: Enter per generare
    window.bind('<Return>', lambda event: generate_and_show())

    window.mainloop()

if __name__ == "__main__":
    create_gui()


