    #"Password Security Checker"

#This is a simple command-line application that allows users to check the security level of their passwords. The program classifies passwords into three categories: low, medium, and high security.
#The key features of this project include:
#1. Password Length Check: The program checks the length of the entered password and provides recommendations based on the length.
#2. Special Character Check: The program checks if the password contains any special characters (such as !, @, #, etc.) and provides feedback on the security level.
#3. Interactive User Interface: The program prompts the user to enter a password and displays the security level along with recommendations for improving the password strength.


print("Hello! You have entered an application to check the security level of a password.")
print("Passwords can be classified into 3 security levels: low, medium, and high.")
print("Enter 0 to exit the program.")

while True:
    password = str(input("Enter a password, and I will check its security level: "))
    spec = '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', ';', ':', ','

    if password == '0':
        print("")
        break

    if len(password)<8:
        print('------------------------------------------------------------------------------------------')
        print("Password security level - low")
        print("I recommend increasing the password length to 12 characters and adding a few special characters.")
        print('------------------------------------------------------------------------------------------')


    elif len(password) > 8 and len(password)<12:
        print('------------------------------------------------------------------------------------------')
        print("Password security level - medium")
        print("I recommend increasing the password length to 12 characters and adding a few special characters.")
        print('------------------------------------------------------------------------------------------')


    elif len(password)>=12:
        x = 0
        for i in spec:
            if i in password:
                x += 1
                if x == 1:
                    print('------------------------------------------------------------------------------------------')
                    print("Password security level - high")
                    print("You have an excellent password!")
                    print('------------------------------------------------------------------------------------------')

    else:
        print('------------------------------------------------------------------------------------------')
        print("Password security level - medium")
        print("I recommend adding a few special characters.")
        print('------------------------------------------------------------------------------------------')
