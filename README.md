# 🔐 Password Strength Checker

A beginner-friendly Python project that checks the strength of a password based on different characteristics such as **length, uppercase letters, lowercase letters, numbers, and special characters**.

The project is being developed step-by-step while learning Python and Regular Expressions (Regex).

## 📌 About the Project

The Password Strength Checker takes a password as input from the user and evaluates it using different criteria.

Each satisfied criterion contributes to the overall password strength score. The final score is used to classify the password as:

* 🔴 **Very Weak**
* 🟠 **Weak**
* 🟡 **Moderate**
* 🟢 **Strong**
* 🟢 **Very Strong**

The purpose of this project is to understand how Python can be used with **conditional statements and regular expressions** to analyze user input.

## ⚙️ Features

* Checks the length of the password
* Checks for uppercase letters
* Checks for lowercase letters
* Checks for numbers
* Checks for special characters
* Calculates a password strength score
* Displays the strength of the password
* Uses Python Regular Expressions (`re`) for character checking

## 🧠 Concepts Used

This project helps in practicing:

* Python variables
* User input
* `if`, `elif`, and `else`
* Conditional statements
* Strings and string methods
* Regular Expressions (Regex)
* Python `re` module
* Basic project development and GitHub

## 📊 Password Strength

The strength is determined using a scoring system based on the characteristics of the entered password.

| Score | Strength    |
| ----- | ----------- |
| 1–2   | Very Weak   |
| 3     | Moderate    |
| 4     | Strong      |
| 5–6   | Very Strong |

The scoring system may be improved as the project develops.

## 🔎 Role of Regex

Regular Expressions are used to check whether the password contains specific types of characters.

For example, the project can use Regex to identify:

* Uppercase letters → `A-Z`
* Lowercase letters → `a-z`
* Numbers → `0-9`
* Special characters → symbols such as `@`, `#`, `$`, `%`, etc.

Regex is used for **checking password characteristics**, while conditional statements are used to determine the final score and strength.

## 🚀 How to Run

1. Make sure Python is installed on your computer.
2. Clone this repository.
3. Open the project folder.
4. Run the Python file.
5. Enter a password when prompted.
6. The program will display the password strength.

## 📁 Project Files

* `password_strength_checker.py` — Initial version of the project
* `password_strength_checker_02.py` — Extended version with additional functionality
* `README.md` — Project documentation

## 🔮 Future Improvements

Some features I plan to add in future versions:

* Better password strength scoring
* Common-password detection
* Feedback explaining **why** a password is weak or strong
* Improved Regex-based validation
* A simple graphical user interface (GUI)
* More detailed password security analysis

## 👩‍💻 Author

**Nandini Rana**

This project is created as a learning project while developing Python and Regex skills.

