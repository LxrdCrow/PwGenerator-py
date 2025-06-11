# PWGenerator-py

**PWGenerator-py** is a secure password generator built with Python, featuring a graphical user interface (GUI) made with Tkinter.  
It allows you to create customized passwords, visualize their strength with color feedback, and save them locally in a simple and user-friendly way.

---

## Key Features

- Generate strong passwords with customizable options:
  - Password length (default: 12)
  - Include uppercase, lowercase, digits, and punctuation
- Password strength evaluation with color-coded feedback
- User-friendly and responsive GUI built with Tkinter
- Read-only output field to prevent accidental password modification
- Save generated passwords securely to a local `passwords.txt` file
- Standalone executable (`.exe`) support via PyInstaller for easy sharing and use

---

## Installation and Usage

### Requirements

- Python 3.8 or higher  
- Tkinter (usually included in standard Python distributions)

### Running from source

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/PWGenerator-py.git
   cd PWGenerator-py/Gui
````

2. Install any dependencies (if applicable):

   ```bash
   pip install -r requirements.txt
   ```

3. Run the GUI:

   ```bash
   python interface.py
   ```

### Standalone Executable

The standalone executable `PWGenerator.exe` is located in the `dist/` folder and can be shared or run without requiring a Python installation.

---

## Usage Example

```plaintext
- Set desired password length (e.g., 16)
- Select character sets to include (uppercase, lowercase, digits, punctuation)
- Click "Generate" or Enter to create the password
- View password strength with color feedback: green (strong), orange (medium), red (weak)
- Click "Save" to store the password locally
```







