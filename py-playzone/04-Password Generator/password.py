letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#LEVEL 1
'''
#my method
pwd=[]
import random
for i in range(nr_letters):
    c=random.choice(letters)    # c=random.randint(0,len(letters)-1)
    pwd.append(c)               # pwd.append(letters[c])
for i in range(nr_symbols):
    c=random.choice(symbols)
    pwd.append(c)
for i in range(nr_numbers):
    c=random.choice(numbers)
    pwd.append(c)  
print("".join(pwd))


#diff approach
pwd = ''
import random
for i in range(nr_letters):
    c=random.choice(letters)     # pwd+=random.choice(letters)
    pwd+=c
for i in range(nr_symbols):
    c=random.choice(symbols)
    pwd+=c
for i in range(nr_numbers):
    c=random.choice(numbers)
    pwd+=c
print(pwd)
'''

#LEVEL 2

pwd=[]
import random
for i in range(nr_letters):
    c=random.choice(letters)
    pwd.append(c)
for i in range(nr_symbols):
    c=random.choice(symbols)
    pwd.append(c)
for i in range(nr_numbers):
    c=random.choice(numbers)
    pwd.append(c)
print(pwd)
random.shuffle(pwd)
print(pwd)
print(f"Your Password is : {"".join(pwd)}")



