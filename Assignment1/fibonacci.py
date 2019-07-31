#I used https://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-sequence for assistance in creating this code 
from math import sqrt
def fib():
	'''
	I don't understand what the purpose of the range is here?
	The syntax is incorrect regardless, please check the documentation for range() 
    '''
    answer=range[0:n]

'''
Everything should be in the same indentation and 'inside' function
'''
n=int(input("Please Enter a number: "))

'''
This fails if n == 0, can you figure out why?
'''
if n<1:
    print("Fibonacci starts with value 1. Try again.")
elif n==1:
    print(1)       
else:                      
      answer=((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))
print("The number is",answer)
    
'''
After you fix the indentations, don't forget to call your function!
'''