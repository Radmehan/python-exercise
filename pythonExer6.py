import random
swg=["s","w","g"]
chance=10
no_of_chance=0
computer_point=0
human_point=0
print("\t\t\t Snake, Water, Gun\n\n\n")
print("s for Snake, g for Gun & w for Water")

while no_of_chance<chance:
    computer = random.choice(swg)
    user_input = input("s or w or g : ")

    if user_input==computer:
        print("Tie both 0 point to each\n")
    elif user_input=="s" and computer=="w" :
        computer_point+=1
        print("Computer wins 1 point" )
        print(f"Computer point is {computer_point} and your point is {human_point}")
    elif user_input=="w" and computer=="s" :
        human_point+=1
        print("You win 1 point")
        print(f"Your point is {human_point} and computer point is {computer_point}")
    elif user_input=="s" and computer=="g" :
        computer_point+=1
        print("Computer wins 1 point" )
        print(f"Computer point is {computer_point} and your point is {human_point}")
    elif user_input=="g" and computer=="s" :
        human_point+=1
        print("You win 1 point")
        print(f"Your point is {human_point} and computer point is {computer_point}")
    elif user_input=="g" and computer=="w" :
        computer_point+=1
        print("Computer wins 1 point" )
        print(f"Computer point is {computer_point} and your point is {human_point}")
    elif user_input=="w" and computer=="g" :
        human_point+=1
        print("You win 1 point")
        print(f"Your point is {human_point} and computer point is {computer_point}")
    else:
        print("You have input wrong")

    no_of_chance+=1
    print(f"{chance-no_of_chance} is left out of {chance}\n ")

print("gameover")

if computer_point==human_point :
    print("Tie")
elif computer_point>human_point :
    print("Computer wins")
else:
    print("You win")