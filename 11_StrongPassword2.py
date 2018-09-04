def minimumNumbe(n, password):
    # Return the minimum number of characters to make the password strong

    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    add = 0
    
    if isinstance(password,int):
        password = str(password)
    
    if all(n not in password for n in numbers):
        add += 1

    if all(l not in password for l in lower_case):
        add += 1

    if all(u not in password for u in upper_case):
        add += 1
    if all(s not in password for s in special_characters):
        add += 1

        
    if n+add <6:
        return 6-n
    else:
        return add
    
print(minimumNumbe(4, 'adeek'))