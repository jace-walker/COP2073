# Jace Walker      Programming Exercise 6
#       This program asks the user if they would like to validate a phone number, ssn, or zip code and will then
#           check to see if the number is valid according to its format.



# import regular expressions
import re

# phone number validation
# used pattern variable from textbook

def check_phone_number(phone_num):
    pattern = r'\d\d\d\-\d\d\d\-\d\d\d\d$'
    if re.match(pattern, phone_num):
        print('Valid Phone Number')

    else:
        print('Invalid Phone Number')

# ssn validation

def check_ssn(ssn):
    pattern = r'\d\d\d\-\d\d\-\d\d\d\d$'
    if re.match(pattern, ssn):
        print('Valid SSN')

    else:
        print('Invalid SSN')

# zip code validation

def check_zip_code(zip_code):
    pattern = r'\d\d\d\d\d\-\d\d\d\d$'
    if re.match(pattern, zip_code):
        print('Valid Zip Code')

    else:
        print('Invalid Zip Code')

# asks user which number they'd like to validate and requests input
# if statements checking which option user selected and then calling appropriate validation function

def main():
    print()
    print('Which would you like to validate?')
    print('1. Phone Number: (xxx-xxx-xxxx)')
    print('2. Social Security Number: (xxx-xx-xxxx)')
    print('3. Zip Code: (xxxxx-xxxx)')
    choice = input('Which would you like to validate?: ')
    user = input('Please enter the number you want to validate WITH hyphens: ')

    if choice == '1':
        check_phone_number(user)

    if choice == '2':
        check_ssn(user)

    if choice == '3':
        check_zip_code(user)


main()