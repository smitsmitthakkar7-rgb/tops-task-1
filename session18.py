# 1 


import re

text = "Call 9876543210 or 8765432109. Price 500, number 6123456789"

pattern = r'\b[789]\d{9}\b'

numbers = re.findall(pattern, text)

print(numbers)


# 2 


import re

def check_date(text):
    pattern = r'\b\d{2}/\d{2}/\d{4}\b'
    if re.search(pattern, text):
        return True
    else:
        return False

print(check_date("Date is 25/06/2024"))
print(check_date("Date is 2024-06-25"))



# 3 


import re

text = "Contact abc@gmail.com and xyz@yahoo.com for help"

pattern = r'[\w.-]+@[\w.-]+\.\w+'

emails = re.findall(pattern, text)

print(emails)


# 4 


import re

text = "My phone number is 9876543210"

result = re.sub(r'\d(?=\d{4})', '*', text)

print(result)


# 5 


import re

text = "Your order ID is OD123456789012345000"

pattern = r'\bOD\d{18}\b'

if re.search(pattern, text):
    print("Valid Order ID")
else:
    print("Invalid Order ID")
