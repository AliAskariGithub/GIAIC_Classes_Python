# Project 02: Password Strength Meter

## 📌 Objective
Build a Password Strength Meter in Python that evaluates a user's password based on security rules. The program will:

- Analyze passwords based on length, character types, and patterns.
- Assign a strength score (Weak, Moderate, Strong).
- Provide feedback to improve weak passwords.
- Utilize control flow, type casting, strings, and functions.

## 🔹 Requirements
### 1. Password Strength Criteria
A strong password should:
- ✅ Be at least 8 characters long
- ✅ Contain uppercase & lowercase letters
- ✅ Include at least one digit (0-9)
- ✅ Have one special character (!@#$%^&*)

### 2. Scoring System
- **Weak (Score: 1-2)** → Short, missing key elements
- **Moderate (Score: 3-4)** → Good but missing some security features
- **Strong (Score: 5)** → Meets all criteria

### 3. Feedback System
- Suggest improvements for weak passwords.
- Display a success message for strong passwords.

## 🔹 Starter Code (Python)
```python
import re

def check_password_strength(password):
    score = 0
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        print("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        print("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        print("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        print("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        print("✅ Strong Password!")
    elif score == 3:
        print("⚠️ Moderate Password - Consider adding more security features.")
    else:
        print("❌ Weak Password - Improve it using the suggestions above.")

# Get user input
password = input("Enter your password: ")
check_password_strength(password)
```

## 🔹 Additional Challenges
- **Password Generator:** Add a feature to suggest a strong password.
- **User-Friendly Interface:** Use Streamlit for a GUI version.
- **Blacklist Common Passwords:** Reject weak passwords like "password123".
- **Custom Scoring Weights:** Give different weights to complexity factors.

## 🔹 Why This Assignment?
- ✅ Uses Control Flow & Conditions
- ✅ Applies String Manipulation & Regex
- ✅ Teaches Security Best Practices
- ✅ Prepares for Real-World Applications

💡 Challenge yourself to build a better, more secure password checker! 🚀

---

## 🔗 Submission
Once you are done, submit this form ASAP:
[Submission Form](https://docs.google.com/forms/d/e/1FAIpQLSfkeRuFVpEojUX4AcpdC6pwBPMxifFreCyR9--PCkqxHGNcDw/viewform)

You are required to innovate and improve the web app.

Share your published app in your section's Discord channel, but do **NOT** share your source code or GitHub repo link anywhere.

## 📚 Learning Resources
- [Streamlit Tutorial](https://github.com/panaversity/learn-modern-ai-python/tree/main/03_ui_streamlit)