#For this specific task, I used https://stackoverflow.com/questions/26218010/how-do-you-get-python-to-ask-the-user-for-an-input-x-amount-of-times in order to do lines 5-7
def main():
    print("This program is meant to sum a series of numbers entered by you! Begin!")
    x= int(input("How many numbers are to be summed?"))
    values= []
    for i in range (x):
        values.append(int(input("Enter a value")))
    Sum=sum(values)
    print(Sum)
main()