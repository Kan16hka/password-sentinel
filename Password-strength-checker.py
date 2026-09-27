"""
Password Strength Checker
---------------------------
Checks a password against several security criteria and gives
feedback on how strong it is.
This also checks whether the password is based on the user's own name
or date of birth, since these are very commonly (and weak) used
password patterns.
"""
 
import re
 
def check_length(password):
    return len(password) >= 8
 
def has_uppercase(password):
    return any(char.isupper() for char in password)
 
def has_lowercase(password):
    return any(char.islower() for char in password)
 
def has_digit(password):
    return any(char.isdigit() for char in password)
 
def has_special_char(password):
    special_characters = r"!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?"
    return bool(re.search(f"[{re.escape(special_characters)}]", password))
 
def check_common_password(password):

    common_passwords = {
        "password", "123456", "12345678", "qwerty", "abc123",
        "password1", "111111", "67", "Password", "admin"
    }
    return password.lower() in common_passwords
 
 
def check_personal_info(password, name, birth_year):
    """
    Checks if the password is based on the user's own name or
    birth year — a very common (and weak) pattern'.
    """
    password_lower = password.lower()
    name_lower = name.lower().strip()
 
    patterns_found = []
 
    if name_lower and name_lower in password_lower:
        patterns_found.append(f"your name ('{name}')")
 
    if birth_year and birth_year in password:
        patterns_found.append(f"your birth year ('{birth_year}')")
 

    combos = [
        f"{name_lower}{birth_year}",
        f"{name_lower}@{birth_year}",
        f"{name_lower}_{birth_year}",
    ]
    if any(combo == password_lower for combo in combos):
        return True, [f"your name combined with your birth year"]
 
    return bool(patterns_found), patterns_found
 
 
def get_date_of_birth(prompt):
    """Keep asking until the user gives a date in DD-MM-YYYY or DD/MM/YYYY format."""
    while True:
        dob = input(prompt).strip()
        match = re.match(r"^(\d{1,2})[-/](\d{1,2})[-/](\d{4})$", dob)
        if match:
            return dob, match.group(3)  # full date string, birth year
        print("Please enter your date of birth as DD-MM-YYYY (e.g. 15-08-2008).\n")
 
 
def rate_password(password, name, birth_year):
    """Returns a score out of 5 and a list of feedback messages."""
    score = 0
    feedback = []
 
    if check_common_password(password):
        return 0, ["This is one of the most commonly used passwords. Avoid it entirely."]
 
    is_personal, found = check_personal_info(password, name, birth_year)
    if is_personal:
        found_str = " and ".join(found)
        return 0, [
            f"Your password is based on {found_str}. Forbid using passwords built from personal "
            f"details (name, birth year) entirely for security purposes "
        ]
 
    if check_length(password):
        score += 1
    else:
        feedback.append("Make it at least 8 characters long.")
 
    if has_uppercase(password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")
 
    if has_lowercase(password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")
 
    if has_digit(password):
        score += 1
    else:
        feedback.append("Add at least one number.")
 
    if has_special_char(password):
        score += 1
    else:
        feedback.append("Add at least one special character (e.g. !, @, #, $, _, -, ~).")
 
    score = max(0, score) 
    return score, feedback
 
 
def score_label(score):
    labels = {
        0: "Very Weak",
        1: "Weak",
        2: "Fair",
        3: "Good",
        4: "Strong",
        5: "Very Strong",
    }
    return labels.get(score, "Unknown")
 
 
def main():
    print("===== Password Strength Checker =====\n")
    print("Note: Your name and date of birth are only used to check if your")
    print("password is based on them. Nothing you enter is saved, stored,")
    print("or shared anywhere. It only exists while this program is running.\n")
 
    name = input("Enter your name(No spaces): ").strip()
    _, birth_year = get_date_of_birth("Enter your date of birth (DD-MM-YYYY): ")
 
    print(f"\nThanks, {name}! Now let's check some passwords.\n")
 
    while True:
        password = input("Enter a password to check(or 'q' to quit): ")
 
        if password.lower() == "q":
            print("Buh-Bye!")
            break
 
        score, feedback = rate_password(password, name, birth_year)
        label = score_label(score)
 
        print(f"\nStrength: {label} ({score}/5)")
 
        if feedback:
            print("Suggestions to improve:")
            for tip in feedback:
                print(f"  - {tip}")
        else:
            print("Great password! No suggestions.")
 
        print()
 
 
if __name__ == "__main__":
    main()
 