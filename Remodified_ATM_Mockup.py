import random
n = random.randint(1000000000, 1999999999)

import time

named_tuple = time.localtime()
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

#Registration
print("Please follow the registeration process")

first_name = input("Enter your firstname:")
last_name = input("Enter your last name:")
username = input("Choose a unique username:")
password = input("Choose a password:")
print("Here is your account number:", n)
print("~~~Registration successful~~")


#Login and ATM operations
def log():
    print("Please login below using your unique username and password!")
    userId = input("Enter username: \n")
    if userId == username :
        pword = input("Enter password: \n")
        if pword == password :
            print("Login time:", time_string)
            print("Welcome", first_name, last_name)
            print("Account number:", n)
            print('''These are the available options:
                1. Withdrawal
                2. Cash Deposit
                3. Complaint
                4. Logout''')

            selectedOption = int(input('Please select an option:\n'))

            if (selectedOption == 1) :
                amount = int(input('How much would you like to withdraw?\n'))
                if amount > 0:
                    print('Take your cash')
                
            elif (selectedOption == 2) :
                deposit = int(input('How much would you like to deposit\n'))
                if deposit > 0 :
                    print('Your current balance is' , deposit)
            elif (selectedOption == 3) :
                input('What issue will you like to report?\n')
                print('Thank you for contacting us')
            elif (selectedOption == 4) :
                log()
            else :
                print('Invalid Option selected, please try again')
        else:
            print("You have entered a wrong password")

log()