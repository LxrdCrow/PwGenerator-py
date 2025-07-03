# interface.py

import tkinter as tk
from tkinter import messagebox, ttk, BooleanVar

from logic import generate_strong_password, save_password, classify_password_strength


def create_gui():
    # Dark mode colors
    BG_COLOR = "#1e1e1e"
    FG_COLOR = "#ffffff"
    ENTRY_BG = "#2c2c2c"
    BUTTON_BG = "#3a3a3a"
    CHECKBOX_SELECT_BG = BG_COLOR

    window = tk.Tk()
    window.title("Password Generator")
    window.geometry("400x520")
    window.resizable(False, False)
    window.configure(bg=BG_COLOR)

    # Password Length
    tk.Label(window, text="Password Length:", bg=BG_COLOR, fg=FG_COLOR).pack(pady=10)
    length_entry = tk.Entry(window, width=10, bg=ENTRY_BG, fg=FG_COLOR, insertbackground=FG_COLOR)
    length_entry.pack()

    # Checkboxes Frame
    checkbox_frame = tk.Frame(window, bg=BG_COLOR)
    checkbox_frame.pack(pady=10)

    use_upper = tk.BooleanVar(value=True)
    use_lower = tk.BooleanVar(value=True)
    use_digits = tk.BooleanVar(value=True)
    use_punct = tk.BooleanVar(value=True)

    tk.Checkbutton(checkbox_frame, text="Include Uppercase", variable=use_upper, bg=BG_COLOR, fg=FG_COLOR, selectcolor=CHECKBOX_SELECT_BG).pack(anchor='w')
    tk.Checkbutton(checkbox_frame, text="Include Lowercase", variable=use_lower, bg=BG_COLOR, fg=FG_COLOR, selectcolor=CHECKBOX_SELECT_BG).pack(anchor='w')
    tk.Checkbutton(checkbox_frame, text="Include Digits", variable=use_digits, bg=BG_COLOR, fg=FG_COLOR, selectcolor=CHECKBOX_SELECT_BG).pack(anchor='w')
    tk.Checkbutton(checkbox_frame, text="Include Punctuation", variable=use_punct, bg=BG_COLOR, fg=FG_COLOR, selectcolor=CHECKBOX_SELECT_BG).pack(anchor='w')

    # Output
    tk.Label(window, text="Generated Password:", bg=BG_COLOR, fg=FG_COLOR).pack(pady=5)
    output_entry = tk.Entry(window, width=40, justify='center', font=("Courier", 12),
                            state='readonly', bg=ENTRY_BG, fg=FG_COLOR, insertbackground=FG_COLOR)
    output_entry.pack(pady=5)

    # Show/hide password toggle
    show_password = BooleanVar(value=False)

    def toggle_password_visibility():
        if show_password.get():
            output_entry.config(show="", fg="black")
        else:
            output_entry.config(show="•", fg="black")

    # Default: password hidden
    output_entry.config(show="•", fg="black")

    tk.Checkbutton(window, text="Show Password", variable=show_password, command=toggle_password_visibility,
                   bg=BG_COLOR, fg=FG_COLOR, selectcolor=CHECKBOX_SELECT_BG).pack(pady=2)

    # Strength Label
    strength_label = tk.Label(window, text="", bg=BG_COLOR, fg=FG_COLOR)
    strength_label.pack(pady=5)

    # Strength Bar
    strength_bar = ttk.Progressbar(window, orient='horizontal', length=200, mode='determinate', maximum=100)
    strength_bar.pack(pady=5)

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
            return

        password = generate_strong_password(length, use_upper.get(), use_lower.get(), use_digits.get(), use_punct.get())
        if password:
            output_entry.config(state='normal')
            output_entry.delete(0, tk.END)
            output_entry.insert(0, password)
            output_entry.config(state='readonly')

            strength = classify_password_strength(password)
            colors = {"Weak": "#e74c3c", "Medium": "#f39c12", "Strong": "#2ecc71"}
            levels = {"Weak": 33, "Medium": 66, "Strong": 100}

            strength_label.config(text=f"Strength: {strength}", fg=colors.get(strength, FG_COLOR))
            strength_bar['value'] = levels.get(strength, 0)

            style = ttk.Style()
            style.theme_use('default')
            style.configure("Custom.Horizontal.TProgressbar", troughcolor=BG_COLOR, background=colors.get(strength, "#3498db"))
            strength_bar.config(style="Custom.Horizontal.TProgressbar")
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
    tk.Button(window, text="Generate", command=generate_and_show, bg=BUTTON_BG, fg=FG_COLOR).pack(pady=5)
    tk.Button(window, text="Save", command=save_password_handler, bg=BUTTON_BG, fg=FG_COLOR).pack()

    # Hotkey: Enter per generare
    window.bind('<Return>', lambda event: generate_and_show())

    window.mainloop()


if __name__ == "__main__":
    create_gui()


