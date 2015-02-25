#!/usr/bin/local/python3

''' =======AUTHOR - AVIK RANJAN BHATTARAI =====
    |            Python Assignment            |
    |      DATE OF SUBMISSION: 09/12/14       |
    |         Guessing a number game          |
    ===========================================
'''
import time#I am importing time so I could use the sleep function to make my output a bit attractive 
name = input("\n\n\tEnter your name - ")
name = name.title()
print ("\t=========================")
print("\tWelcome ",name,"!!! ")
choice =input("\tDo you want to play a game??  (Yes/No)  ")
choice = choice.upper()#user can input lower case or upper case

if choice == "YES" or choice == "Y":#user might input just "Y" or "YES"
    while True:
        print ("\n\t****Think of a number between 0 and 100****")
        for dot in range (0,6):#I wanted to make it look more real, so I added the time sleep, 
            print ("\t*", end=" ",flush=True)#also I was having problem with buffer thats why I put a flush
            time.sleep(0.5)
            
        print ("\n\t***** Stay relaxed and Enjoy the ride!! ****\n\n")
        time.sleep(1)
        
        num = 50 #divide and rule strategy, halfway of 0 and 100
        x = 50 #increment which I will be adding or substracting from num
        count = 1
        while True: #infinite loop until correct number is guessed
            print("\tIs it ",num,"?", end="",flush=True)
            answer = input( "  (yes/no)  ")
            answer = answer.upper()
            if answer == "YES":
                print ("\n\n\t****************************************")
                print ("\tYay I found your number",num,"in",count,"attempt(s)\n\n")
                
                break
            else:
                print("\tIs it larger than",num,"?", end="",flush=True)
                answer2 = input( "  (yes/no)  ")
                answer2 = answer2.upper()
                if answer2 == "YES" or answer2 == "Y":
                    count = count + 1
                    x = int((x+1)/2)#could have done just x/2 but I would not get to either 0 or 100
                    num = int(num + x)
                    if num>100:
                        num =100
                    
                elif answer2 == "NO" or answer2 == "N":
                    count = count + 1
                    x = int((x+1)/2)
                    num = int (num - x)
                    if num <0:
                        num = 0
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

