print("guess the correct number under 1 to 25")
n=18
i=1
print("Number of guessrs is limited to only 9 times")
while i<=9:
    userInput = int(input("Guess a Number:\n"))
    # guess_number = int(input("Guess the number :\n"))
    if userInput<18:
        print("You enter less number please think a greater number")
    # if guess_number < 18:
    #     print("you enter less number please input greater number.\n")
    elif userInput>18:
        print("You enter greater number please think a less number")
    # elif guess_number > 18:
    #     print("you enter greater number please input smaller number.\n ")
    else:
        print("Congrats!!You win\n")
        print(i, "No. of guess you took finish")
        break
    print(9-i, "No. of guess left")
    i += 1
if i>9:
    print("game over")


