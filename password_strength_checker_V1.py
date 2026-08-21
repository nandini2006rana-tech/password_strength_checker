from datetime import datetime
import re
import sys

print('-' * 50)
print('  Welcome to password strength checking tool')
print('             Author: Nandini Rana')
print(f'             Date  : {datetime.now().date()}')
print(f'             Time  : {datetime.now().strftime('%I:%M:%S %p')} ')
print('-' * 50)
while True:
    try:
        print('1. CHECK YOUR PASSWORD STRENGTH\n2. PRESS ANY KEY TO EXIT')
        a =input('ENTER YOUR CHOICE :')
        if a == '1':
            print('                 # INSTRUCTIONS #')
            print('''
            1. Enter your password in the password field.
            2. Click the "Check Strength" button to analyze your password.
            3. The application will evaluate your password based on:
               • Password length
               • Uppercase letters (A–Z)
               • Lowercase letters (a–z)
               • Numbers (0–9)
               • Special characters (!, @, #, $, %, *, &)
            4. The result will display your password strength:
                • Weak
                • Medium
                • Strong
                • Very Strong
            5. A checklist will show which security requirements are met.
            6. If your password is weak, suggestions will be provided to improve it.
            7. Use the "Clear" button to reset all fields and check another password.
            8. For security reasons, your password is not stored or shared.''')
            print('')
            b= input('ENTER YOUR PASSWORD :')
            print('')
            print('-' * 50)

            point= 0
            if 12<=len(b)<=64:
                print(f'Your password contains length of: {len(b)}')
                point += 1
                c = r"[A-Z]"
                if re.search(c, b):
                    print('Your password contain uppercase')
                    point += 1
                else:
                    print('Your password does not contain uppercase')

                d = r"[a-z]"
                if re.search(d, b):
                    print('Your password contain lowercase')
                    point += 1
                else:
                    print('Your password does not contain lowercase')
                e = r'[0-9]'
                if re.search(e, b):
                    print('Your password contain numbers')
                    point += 1
                else:
                    print('Your password does not contain numbers')
                f = r"[!@#$&*%]"
                if re.search(f, b):
                    print('Your password contain special characters')
                    point += 1
                    print('-' * 50)
                else:
                    print('Your password does not contain special characters')
                    print('-' * 50)
                if point == 1:
                    print('Your password is very weak')
                if point == 2:
                    print('Your password is weak')
                if point == 3:
                    print('Your password is moderate')
                if point == 4:
                    print('Your password is strong')
                if point == 5:
                    print('Your password is very strong')
                print(f'Total points for your password is: {point}/5')
                print('')


            elif 8 <= len(b) < 12:
                print(f'Your password contains length of : {len(b)}')
                point = 0
                c = r"[A-Z]"
                if re.search(c, b):
                    print('Your password contain uppercase')
                    point += 1
                else:
                    print('Your password does not contain uppercase')
                d = r"[a-z]"
                if re.search(d, b):
                    print('Your password contain lowercase')
                    point += 1
                else:
                    print('Your password does not contain lowercase')
                e = r'[0-9]'
                if re.search(e, b):
                    print('Your password contain numbers')
                    point += 1
                else:
                    print('Your password does not contain numbers')
                f = r"[!@#$&*%]"
                if re.search(f, b):
                    print('Your password contain special characters')
                    point += 1
                    print('-' * 50)
                else:
                    print('Your password does not contain special characters')
                    print('-' * 50)
                if point == 1:
                    print('Your password is very weak')
                if point == 2:
                    print('Your password is weak')
                if point == 3:
                    print('Your password is moderate')
                    print('')
                if point == 4:
                    print('Your password is strong')
                if point == 5:
                    print('Your password is very strong')

                print(f'Total points for your password is: {point}/5')
                print('')

            elif 0 < len(b) < 8:
                print('Your password contains less than 8 characters')
                print('Please re-enter your password again')
                print('')
                continue

        else:
            print('Thank you')
            sys.exit()

    except NameError:
        print('Thank you')
        sys.exit()





