import os

#idades criança,adolescente e adulto
age = int(input("enter your age: "))
if age <= 12:
    print("you're a child")
elif age > 12 and age <= 18:
    print("you're teen")
else:
    print("you're an adult")
os.system('cls')

#par ou impar

number = int(input("enter a number int: "))
if number % 2 == 0:
    print("this number's even!")
else:
    print("This number's Odd!")

os.system('cls')
#Solicitar um nome de usuário e uma senha
#verificar se o nome de usuário e a senha 
#fornecidos correspondem aos valores esperados

user = input("enter a username: ")
password = input("enter a password with five digits: ")

if user == "Pereira" and password != "12345":
    print("User correct but password incorrect!")
elif user != "Pereira" and password == "12345":
    print("User incorrect but password correct")
elif user != "Pereira" and password != "12345":
    print("username and password are incorrect")
else:
    print(f"open")
print(f"Username {user} password {password}")






