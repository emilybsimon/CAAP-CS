#I used https://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-sequence for assistance in creating this code 
from math import sqrt
def fib():
    answer=range[0:n]
n=int(input("Please Enter a number: "))

if n<1:
    print("Fibonacci starts with value 1. Try again.")
elif n==1:
    print(1)       
else:                      
      answer=((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))
print("The number is",answer)
    