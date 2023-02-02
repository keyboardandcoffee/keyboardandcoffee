'''
Password Strength Checker
-------------------------------------------------------------
'''


import string
import getpass
import random
import string

# Generate a password using the ascii_letters variable which generates any combination of both upper and lower case letters, any digit
# any punctuation and some more random characters I decided to include based on the length you prefer your password to be
password_length = int(input("How long would you like your password to be? "))

password_chars = string.ascii_letters + string.digits + string.punctuation + '@#$%^&*{}[]_'

password = ''.join(random.choice(password_chars) for i in range(password_length))

while not (any(char.isdigit() for char in password)
        and any(char.isupper() for char in password)
        and any(char.islower() for char in password)
        and any(char in string.punctuation for char in password)):
    password = ''.join(random.choice(password_chars) for i in range(password_length))

print(password)


# Begin a password strength checker. This will evaluate your passoword and assign a strength score and make a suggestion to the end user

#NOTE: you can copy and paste the generated password, but I've hidden the visibility of the pasted password for extra protection from viewers

def check_password_strength():
   password = getpass.getpass('Enter the password: ')
   strength = 0
   remarks = ''
   lower_count = upper_count = num_count = wspace_count = special_count = 0

   for char in list(password):
       if char in string.ascii_lowercase:
           lower_count += 1
       elif char in string.ascii_uppercase:
           upper_count += 1
       elif char in string.digits:
           num_count += 1
       elif char == ' ':
           wspace_count += 1
       else:
           special_count += 1

   if lower_count >= 1:
       strength += 1
   if upper_count >= 1:
       strength += 1
   if num_count >= 1:
       strength += 1
   if wspace_count >= 1:
       strength += 1
   if special_count >= 1:
       strength += 1

   if strength == 1:
       remarks = ('That\'s a very bad password.'
           ' Change it as soon as possible.')
   elif strength == 2:
       remarks = ('That\'s a weak password.'
           ' You should consider using a tougher password.')
   elif strength == 3:
       remarks = 'Your password is okay, but it can be improved.'
   elif strength == 4:
       remarks = ('Your password is hard to guess.'
           ' But you could make it even more secure.')
   elif strength == 5:
       remarks = ('Now that\'s one exquisite of a strong password!!!'
           ' Hackers don\'t have a chance guessing that password!')

   print('Your password has:-')
   print(f'{lower_count} lowercase letters')
   print(f'{upper_count} uppercase letters')
   print(f'{num_count} digits')
   print(f'{wspace_count} whitespaces')
   print(f'{special_count} special characters')
   print(f'Password Score: {strength / 5}')
   print(f'Remarks: {remarks}')


def check_pwd(another_pw=False):
   valid = False
   if another_pw:
       choice = input(
           'Do you want to check another password\'s strength (y/n) : ')
   else:
       choice = input(
           'Do you want to check your password\'s strength (y/n) : ')

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
