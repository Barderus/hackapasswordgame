check = inputValidation(password)

    # if invalid, ask the user for valid password
    while check:
        password = input("Invalid Password. Try another one: ")
        check = inputValidation(password)

# INPUT VALIDATION
# ----------------

def inputValidation(password):
    # make sure there is no space at the front,
    # the back or in the middle of the string
    if " " in password:
        return True
    
    # make sure the string has at least 1 character 
    # and at most 16 characters
    elif len(password) < 1 or len(password) > 16:
        return True
    
    else:
        return False
