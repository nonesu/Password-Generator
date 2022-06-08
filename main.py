import random

# *-*-*-* Chars(random generated characters) *-*-*-*
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!:;,²&é"(-è_àç)=$^*ù0123456789@~#{[|`}'
number = input("Entre amount of generated password : ")
number = int(number)

length = input("Entre your generated password length : ")
length = int(length)

print("here are your generated password! :")
for pwd in range(number):
    passwords =""
    for i in range(length):
        passwords += random.choice(chars)
    print(passwords)
