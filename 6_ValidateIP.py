def validate_ip(ip):
    len_ip =len(ip.strip())
    octet =[]
    
    if len_ip <=0 or len_ip>15:
        return False
    elif ip.strip().count('.') !=3:
        return False
    else:
        octets = ip.strip().split('.')
        for octet in octets:
            if not octet.isdigit() or int(octet) <0 or int(octet) >255:
                return False
    return True
            
ip='192:45.12.00a00'
print(validate_ip(ip))

#length check
#delimiter check
#space check
#count of delimiter check
#octet check

#Time complexity - O(1)
#Space complexity - O(n)