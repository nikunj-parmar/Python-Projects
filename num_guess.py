import random

print("\tWelcome to Guess Number!")

orginal_num = random.randrange(1, 100)
count = 3
check = False
while check == False:
    guess_num = int(input("Enter The number"))
    if guess_num < 1 or guess_num > 100:
        print("You are out of range\n Please Select between 1 to 100")
        pass
    elif orginal_num > guess_num:
        print("You guessed too low!")
        count = count-1
        print("Chances left = ", count)
        pass
    elif orginal_num < guess_num:
        print("You guessed too high!")
        count = count-1
        print("Chances left = ", count)
        pass
    else:
        print("Congratulation! You gueesed the right number")
        check == True
        break
    if count == 0:
        print("Better Luck Next time!")
        print("Gueesed Number was: ", guess_num)
        break
