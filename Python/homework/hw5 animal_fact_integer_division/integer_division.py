from random import randrange


def print_result(answer1,answer2):
    if answer1 == int(answer2):
        print("CORRECT!!")
    else:
        print ("INCORRECT!! The correct answer is",int(answer2))

    
choice = "Y"
while choice.upper()=="Y":#everytime program loops, two random numbers are generated
    a = randrange(10)
    b = randrange(10)
    try:
        answer = (a/b)
    except ZeroDivisionError: #if zerodivisionError occurs the program assigns answer as 0, eg: 0/0 = 0, 4/0 = 0 
        pass
    try:
        if int(answer)==float(answer):#we perform further only for whole numbers example:(3==3.0). We want to avoid decimals and fractions
            user_answer = input (str(a)+"/"+str(b)+"=")
            user_answer = int(user_answer)
            print_result(user_answer, answer)
            choice =input("Play again?")

    except ValueError:#if user enters strings or float
        print("Please enter integers only!")
