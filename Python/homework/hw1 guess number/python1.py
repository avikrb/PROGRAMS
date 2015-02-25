name = input("\n\n\tEnter your name - ")
name = name.title()
print("\tWelcome ",name,"!!! ")
choice =input("\tDo you want to play a game??  (Yes/No)  ")
choice = choice.upper()#user can input lower case or upper case
if choice == "YES" or choice == "Y":#user might input just "Y" or "YES"
    while True:
        print ("\n\t****Think of a number between 0 and 100****")            
        print ("\n\t***** Stay relaxed and Enjoy the ride!! ****\n\n")
        num1 = 0 #num1 is the lower number
        num2 = 100 #num2 is the higher number
        num3 = int(num1 + num2 /2)#divide and rule strategy
        count = 1
        while True: #infinite loop until correct number is guessed
            print("\tIs it ",num3,"?", end="")
            answer = input( "  (yes/no)  ")
            answer = answer.upper()
            if answer == "YES":
                print ("\tYay I found your number",num3,"in",count,"attempt(s)\n\n")
                break
            else:
                print("\tIs it larger than",num3,"?", end="")
                answer2 = input( "  (yes/no)  ")
                answer2 = answer2.upper()
                if answer2 == "YES" or answer2 == "Y":
                    count = count + 1
                    num1 = num3 + 1#lower number is changed from previous to a new value
                    num3 = int((num2+num1)/2)#continuation of the divide and rule strategy
                elif answer2 == "NO" or answer2 == "N":
                    count = count + 1
                    num2 = num3 - 1#higher number is changed from previous to a new value
                    num3 = int((num2+num1)/2)
                else:#just for validation, if user inputs wrong choice, the program loops
                    continue
        play_again = input("\tDo you want to play again?? ")
        play_again = play_again.upper()
        if play_again == "YES" or play_again == "Y":
            print ("\n\n\tGood to know you are having fun", name,"!! Lets do this again")
        else:
            print ("\n\n\tThank You", name, "!!  Come back again!!\n\n")
            break
elif choice == "NO" or choice == "N":
    print ("\n\nThank you! See you again", name, "!!!\n\n")
else: #just for input validation
    print ("\n\n\t---->>>>>>Wrong input<<<<<<-----")
    print ("\t",name,"you have to start over again!!!\n\n")


