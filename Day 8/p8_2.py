#Write your code below this line ๐
import math

def prime_checker(number):
    flag = 1
    for i in range(2, math.floor(number / 2) + 1 ):
        if number % i == 0:
            flag = 0
            break
        
    if flag == 0:
        print(f"{number} is not a prime number.")
    else:
        print(f"{number} is a prime number.")



#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)