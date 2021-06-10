"""

# Health Management System
# 3 clients - Harry, Rohan and Hammad

def getdate():
    import datetime
    return datetime.datetime.now()

# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client

"""
def getdate():
    import datetime
    return datetime.datetime.now()
print("Welcome to health management")
person=input("Enter any person 'Harry', 'Rohan' or 'Hammad' : \n")
data=input("Enter your datatype 'lock' or 'retrieve' : \n")
choice=input("Enter Data type 'exercise' or 'food' :\n")
def harry():
    if data == "lock":
        if choice=="exercice":
            value=input("pls type..........\n")
            with open("harryExer.txt", "a") as harryExer:
                harryExer.write(str([str(getdate())])+value+"\n")
            print("successfully added")
        elif choice=="food":
            value = input("pls type..........\n")
            with open("harryFood.txt.txt", "a") as harryFood:
                harryFood.write(value + str([str(getdate())]) + "\n")
            print("successfully added")
    elif data=="retrieve":
        if choice=="exercice":
            with open("harryExer.txt",) as harryExer:
                print(harryExer.readlines(), end="")
            print("successfully printed")
        elif choice == "food":
            with open("harryFood.txt") as harryFood:
                for i in harryFood:
                    print(i, end="")
            print("successfully printed")

def hammad():
    if data == "lock":
        if choice=="exercice":
            value=input("pls type..........\n")
            with open("hammadExer.txt","a") as hammadExer:
                hammadExer.write(value+str([str(getdate())])+"\n")
            print("successfully added")
        elif choice == "food":
            value = input("pls type..........\n")
            with open("hammadFood.txt.txt", "a") as hammadFood:
                hammadFood.write(value + str([str(getdate())]) + "\n")
            print("successfully added")
    elif data == "retrieve":
        if choice=="exercice":
            with open("hammadExer.txt") as hammadExer:
                for i in hammadExer:
                    print(i, end="")
            print("successfully printed")
        elif choice == "food":
            with open("hammadFood.txt") as hammadFood:
                for i in hammadFood:
                    print(i, end="")
            print("successfully printed")

def rohan():
    if data == "lock":
        if choice=="exercice":
            value=input("pls type..........\n")
            with open("rohanExer.txt","a") as rohanExer:
                rohanExer.write(value+str([str(getdate())])+"\n")
            print("successfully added")
        elif choice == "food":
            value = input("pls type..........\n")
            with open("rohanFood.txt.txt", "a") as rohanFood:
                rohanFood.write(value + str([str(getdate())]) + "\n")
            print("successfully added")
    elif data == "retrieve":
        if choice=="exercice":
            with open("rohanExer.txt") as rohanExer:
                for i in rohanExer:
                    print(i, end="")
            print("successfully printed")
        elif choice == "food":
            with open("rohanFood.txt") as rohanFood:
                for i in rohanFood:
                    print(i, end="")
            print("successfully printed")

if person=="harry":
    harry()
elif person=="rohan":
    rohan()
else:
    hammad()


