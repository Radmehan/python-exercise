firstNum = int(input("Enter the number : "))
secNum=int(input("Enter the second number : "))
operator = input("Enter Operator : ")
if firstNum==45 and secNum==3 and operator=="*":
    print(555)
elif firstNum==56 and secNum==9 and operator=="+":
    print(77)
elif firstNum==56 and secNum==4 and operator=="/":
    print(4)
elif operator=="+":
    print(firstNum+secNum)
elif operator=="*":
    print(firstNum*secNum)
elif operator=="-":
    print(firstNum-secNum)
elif operator=="/":
    print(firstNum/secNum)
else:
    print("Math error")

