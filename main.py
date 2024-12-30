karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
import random

def generate_password(numOfChars) :
    password = ""
    for i in range(numOfChars) :
        password += random.choice(karakterler)
    return password

num_of_letters = int(input("Kaç karakterli bir şifre istiyorsunuz?"))
password = generate_password(num_of_letters)
print(password)