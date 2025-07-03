# PWGenerator-py

**PWGenerator-py** is a secure and user-friendly password generator built with Python, featuring a modern GUI created with Tkinter.
It allows you to generate customized strong passwords, see their strength with intuitive color feedback, save them securely, and run the app easily via a standalone executable with a custom icon.

---

## Key Features

* Generate strong passwords with flexible options:

  * Set password length (default: 12)
  * Include uppercase letters, lowercase letters, digits, and punctuation
* Visual password strength evaluation with clear color-coded feedback (red, orange, green)
* Responsive and clean GUI using Tkinter, including a read-only output field to prevent accidental edits
* Save generated passwords safely to a local `passwords.txt` file
* Ready-to-use standalone Windows executable (`.exe`) with a custom icon — no Python installation required

---

## Requirements

* For running from source:

  * Python 3.8 or higher
  * Tkinter (usually pre-installed with Python)
* For running the standalone executable:

  * Windows OS (no Python or dependencies needed)

---

## Installation and Usage

### Running from source

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/PWGenerator-py.git
   cd PWGenerator-py/Gui
   ```

2. (Optional) Install dependencies if you add any later:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python interface.py
   ```

### Running the standalone executable

1. Navigate to the `dist` folder inside the project directory.
2. Double-click the `interface.exe` file (or your renamed executable) to launch the app.
3. Enjoy the password generator with its custom icon and without needing Python installed.

---

## Usage Example

```plaintext
- Set desired password length (e.g., 16)
- Select which character sets to include (uppercase, lowercase, digits, punctuation)
- Click "Generate" or press Enter to create a password
- View the password strength displayed with color feedback:
    * Green = Strong
    * Orange = Medium
    * Red = Weak
- Click "Save" to append the generated password to the local passwords.txt file
```










