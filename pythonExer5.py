import datetime

def getTime() :
    return datetime.datetime.now()

print("Welcome to health management")
person=input("Enter any person 'Harry', 'Rohan' or 'Hammad' : \n")
data1=input("Enter your datatype 'Add' or 'retrieve' : \n")
data2=input("Enter Data type 'exercise' or 'food' :\n")

def harry():
    if data1=="Add":
        if data2=="exercise" :
            value=input("Type here ..... \n")
            with open("harryExer.txt", "a") as harryExer:
                harryExer.write(str([str(getTime())])+value+"\n")
            print("Sucessfully written")
        elif data2 == "food":
            value = input("Type here ..... \n")
            with open("harryFood.txt", "a") as harryFood:
                harryFood.write(str([str(getTime())])+value+"\n")
            print("Sucessfully written")

    elif data1 == "retrieve":
        if data2 == "exercise":
            with open("harryExer.txt") as exer:
                for i in exer:
                    print(i, end=" ")
        elif data2 == "food":
            with open("harryFood.txt") as food:
                for i in food:
                    print(i, end=" ")



def rohan():
    if data1=="Add":
        if data2=="exercise" :
            value=input("Type here ..... \n")
            with open("rohanExer.txt", "a") as rohanExer:
                rohanExer.write(str([str(getTime())])+value+"\n")
            print("Sucessfully written")
        elif data2 == "food":
            value = input("Type here ..... \n")
            with open("rohanFood.txt", "a") as rohanFood:
                rohanFood.write(str([str(getTime())])+value+"\n")
            print("Sucessfully written")

    elif data1 == "retrieve":
        if data2 == "exercise":
            with open("rohanExer.txt") as exer:
                for i in exer:
                    print(i, end=" ")
        elif data2 == "food":
            with open("rohanFood.txt") as food:
                for i in food:
                    print(i, end=" ")


def hammad():
    if data1=="Add":
        if data2=="exercise" :
            value=input("Type here ..... \n")
            with open("hammadExer.txt", "a") as hammadExer:
                hammadExer.write(str([str(getTime())])+value+"\n")
            print("Sucessfully written")
        elif data2 == "food":
            value = input("Type here ..... \n")
            with open("hammadFood.txt", "a") as hammadFood:
                hammadFood.write(str([str(getTime())])+value+"\n")
            print("Sucessfully written")

    elif data1 == "retrieve":
        if data2 == "exercise":
            with open("hammadExer.txt") as exer:
                for i in exer:
                    print(i, end=" ")
        elif data2 == "food":
            with open("hammadFood.txt") as food:
                for i in food:
                    print(i, end=" ")


if person=="Harry":
    harry()
elif person=="Rohan" :
    rohan()
else:
    hammad()

