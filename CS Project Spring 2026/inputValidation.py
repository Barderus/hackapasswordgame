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
    
#   # make sure the sting has at least a
#   # character and the length is at most 16 character more
    elif 1 > len(password) > 16:
        return True
    else:
        return False
