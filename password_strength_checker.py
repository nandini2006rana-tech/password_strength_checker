from datetime import datetime
import re
print('*' * 50)
print('  Welcome to password strength checking tool')
print('             Author: Nandini Rana')
print(f'             Date  : {datetime.now().date()}')
print(f'             Time  : {datetime.now().strftime('%I:%M:%S %p')} ')
print('*' * 50)
while True:
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
           • Special characters (!, @, #, $, etc.)
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
        if 8<len(b)<=64:
            print('Condition 1 is satisfied')