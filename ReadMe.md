# Password Strength Checker

A command-line program that asks for your name and date of birth(but doesn't store it anywhere), then checks any password you enter against common security criteria like length, uppercase/lowercase letters, numbers, special characters or whether it's one of the most commonly used or easily guessed passwords or even whether it's based on your own name or birth year. Gives a strength score out of 5 with suggestions for improvement.

## How to run
```bash
python password-strength-checker.py
```

# Features
- Asks for your name and date of birth up front without storing it anywhere for privacy.
- Scores a password out of 5 based on:
    - Minimum length (8+ characters)
    - Presence of uppercase and lowercase letters
    - Presence of at least one number
    - Presence of at least one special character
- Checks for commonly used unsecure passwords
- Checks for passwords that contain your own name or birth year(most unsecure)
- Gives actionable suggestions for each missing criterion.
- Loops so you can test multiple passwords in one session.
 

# What I learned building this
- Using Python's re (regular expressions) module to detect special characters and validate date input.
- Writing small, testable helper functions for each individual check.
- Using a set for fast lookup when checking against the list of common passwords.
- Checking user input against personal details to model a real-world weak-password pattern.
- Structuring feedback so it's specific and actionable, not just a pass/fail result.
- Not only identifying weak passwords but also listing some improvements
- Also checks for the user's name/birth year reversed.


# Improvement needed
- Add a GUI or web version so passwords aren't visible in the terminal history
