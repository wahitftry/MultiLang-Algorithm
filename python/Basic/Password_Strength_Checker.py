import string
import getpass

def count_chars(password):
    upper_count = 0
    num_count = 0
    wspace_count = 0
    special_count = 0

    for char in password:
        if char.isupper():
            upper_count += 1
        elif char.isdigit():
            num_count += 1
        elif char.isspace():
            wspace_count += 1
        else:
            special_count += 1

    return upper_count, num_count, wspace_count, special_count

def check_strength(upper_count, num_count, wspace_count, special_count):
    strength = 0
    remarks = ''

    if upper_count > 0:
        strength += 1
    if num_count > 0:
        strength += 1
    if wspace_count > 0:
        strength += 1
    if special_count > 0:
        strength += 1

    if len(password) >= 8:
        strength += 1
    if len(password) >= 12:
        strength += 1

    if strength == 0:
        remarks = 'Very weak'
    elif strength == 1:
        remarks = 'Weak'
    elif strength == 2:
        remarks = 'Moderate'
    elif strength == 3:
        remarks = 'Strong'
    else:
        remarks = 'Very strong'

    return strength, remarks

def check_password_strength():
    password = input('Enter password: ')
    upper_count, num_count, wspace_count, special_count = count_chars(password)
    strength, remarks = check_strength(upper_count, num_count, wspace_count, special_count)

    print(f'{upper_count} uppercase letters')
    print(f'{num_count} digits')
    print(f'{wspace_count} whitespaces')
    print(f'{special_count} special characters')
    print(f'Password Score: {strength / 5}')
    print(f'Remarks: {remarks}')

def check_pwd(another_pw=False):
    valid = False
    if another_pw:
        choice = input('Do you want to check another password\'s strength (y/n) : ')
    else:
        choice = input('Do you want to check your password\'s strength (y/n) : ')

    while not valid:
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            print('Exiting...')
            return False
        else:
            print('Invalid input...please try again. \n')

if __name__ == '__main__':
    print('===== Welcome to Password Strength Checker =====')
    check_pw = check_pwd()
    while check_pw:
        check_password_strength()
        check_pw = check_pwd(True)
