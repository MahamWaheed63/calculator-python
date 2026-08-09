



while True:

    num1=int(input("Enter first number:"))
    num2=int(input("Enter secound number:"))
    print("Press 1 if you want to add two numbers:")
    print("Press 2 if you want to subtract two numbers:")
    print("Press 3 if you want to multiply two numbers:")
    print("Press 4 if you want to divide two numbers:")
    op=int(input("Tell your responce"))

    def add(num1, num2):
     return num1+num2
    def subtract(num1,num2):
     return num1-num2
    def multiply(num1,num2):
     return num1*num2
    def divide(num1,num2):
     return num1/num2
    
    if op==1:
     answer=add(num1,num2)
     print(f"{num1} + {num2} = {answer} " )
    elif op==2:
     answer=subtract(num1,num2)
     print(f"{num1} - {num2} = {answer} " )
    elif op==3:
     answer=multiply(num1,num2)
     print(f"{num1} * {num2} = {answer} " )
    elif op==4:
        if num2==0:
            print("Cannot divide by 0")
        else:           
         answer=divide(num1,num2)
         print(f"{num1} / {num2} = {answer} " )
    else:
     print("Invalid number")
    choice=input("cotinue? (y/n):")
    if choice=="n":
        break