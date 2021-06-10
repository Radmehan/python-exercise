# print("pattern printing")
# num = int(input("Enter the Number : "))
# print("Type 0 or 1")
# bool_var = input("Enter Boolean variable '1' for 'True' & '0' for 'False' :")
# if bool_var=="1" :
#     for i in range(num+1):
#         print("*" * i)
# if bool_var == "0":
#     for i in range(num,0,-1) :
#         print("*" * i)

num = int(input("Enter a number : "))
bool_var = bool(input("Enter 'True' or 'False' : "))

def star(num,bool_var) :
    if bool_var==True :
        c = 1
        while c<=num :
            print(c * "*")
            c+=1
    else:
        while c<num :
            print(num * "*")
            num-=1

star(num,bool_var)