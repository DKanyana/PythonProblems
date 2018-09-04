def unique_firstname(names):
    first={}
    
    for fullname in names:
        if ' ' in fullname:
            firstname = fullname.split()[0]
        else:
            firstname=fullname
        if firstname not in first:
            first[firstname] = True
    return first.keys()

names =['Tom Hardy', 'Jack Daniel','Kate Muffet','Tom Lordy','YUi']
print(unique_firstname(names))