def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    
    passet = set(str(password))
    numbers = set("0123456789")
    lower_case = set("abcdefghijklmnopqrstuvwxyz")
    upper_case = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    special_characters = set("!@#$%^&*()-+")
    
    num_missing = 0
    lowercase_missing = 0
    uppercase_missing = 0
    splchar_missing = 0
    
    if not passet & numbers:
        num_missing = 1
    if not passet & lower_case:
        lowercase_missing = 1
    if not passet & upper_case:
        uppercase_missing = 1
    if not passet & special_characters:
        splchar_missing = 1
        
    nos = (num_missing+lowercase_missing+uppercase_missing+splchar_missing)
        
    if n+nos <6:
        return 6-n
    else:
        return nos
        

print(minimumNumber(4, 4700))