#Easy Method :
# add 5 number using ython
print("Add 5 number using python method 1")
print("")
def add_number1():
    num1=float(input("Enter a number :"))
    num2=float(input("Enter an another number :"))
    num3=float(input("Enter an another number :"))
    num4=float(input("Enter an another number :"))
    num5=float(input("Enter an another number :"))
    total=num1+num2+num3+num4+num5
    print("")
    print('The addition of 5 number is :',total)
add_number1()        

#Another Method :
# add 5 number using ython
print("")
print("Add 5 number using python method 2")

def add_number2():
    numbers=[]
    for i in range(5):
        num=float(input(f'Enter a number {i+1} :'))
        #num=float(input(f'{i+1} | Enter a number :'))
        numbers.append(num)
        total=sum(numbers)
        print("")
    print(f'The addition of 5 number is : {total}')
    #print('The addition of 5 number is :',total)
    
add_number2()
