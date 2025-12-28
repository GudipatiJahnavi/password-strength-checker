def password_checker(password):

    has_upper = False
    has_digit = False
    has_special = False
    special_charecters = "!@#$%^&*_-+="

    if len(password)<8:
        return "Weak"
    
    for ch in password:
        if ch.isupper() :
            has_upper = True
        elif ch.isdigit():
            has_digit = True
        elif ch in special_charecters:
            has_special = True
        
    if has_upper and has_digit and has_special :
        return "Strong"
    elif (has_upper and has_digit) or (has_digit and has_special) :
        return "medium"
    else :
        return "Weak"


password = input("Enter Your Password:")
strength = password_checker(password)
print("Your Password Strength is :",strength)