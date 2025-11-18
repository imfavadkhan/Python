num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))

choice = input("+ , - , * , / :")
if(choice == "+"):
    print(f"{num1} + {num2} = {num1+num2}")
elif(choice == "-"):
    print(f"{num1} - {num2} = {num1-num2}")
elif(choice == "*"):
    print(f"{num1} * {num2} = {num1*num2}")
elif(choice == "/"):
    print(f"{num1} / {num2} = {num1//num2}")

