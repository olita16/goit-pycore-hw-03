import re

def normalize_phone(phone_number):
    phone_number = re.sub(r'[^\d+]', '', phone_number.strip())
    if phone_number.startswith('+'):
        if not phone_number.startswith('+38'):
            phone_number = '+38' + phone_number[1:] 
    else:
        if phone_number.startswith('380'):
            phone_number = '+' + phone_number
        else:
            phone_number = '+38' + phone_number
    return phone_number

print(normalize_phone("    +38(050)123-32-34"))  
print(normalize_phone("     0503451234"))        
print(normalize_phone("(050)8889900"))          
print(normalize_phone("38050-111-22-22"))     
print(normalize_phone("38050 111 22 11   "))  
