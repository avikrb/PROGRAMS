class Animal:
    def __init__(self, name):
        self.name = name

    def guess_who_am_i(self):
        i = 1
        for hint in (hint_dictionary[self.name]):
            print ("\tHint "+str(i)+". "+hint)
            answer = input ("\tWho am I?")
            if answer.lower()== self.name:
                print ("\tYou got it! I am a "+self.name)
                break
            else:
                print ("\tNope, try again with the next hint")
                i +=1
            if i > 3:
                print("\tOops, sorry I am out of hints")
                print ("\tThe answer was "+self.name)
            
        


hint_dictionary = {"elephant": ["I have exceptional memory", "I am the largest land-living mammal in the world", "I have a trunk"],"tiger":["I am the biggest cat", "I come in black and white or orange and black", "I am a carnivore"],"bat":["I use echo-location", "I can fly", "I see well in dark"]}
t = Animal("tiger")
e = Animal("elephant")
b = Animal("bat")

print ("\n\n\t"+"="*6+"Lets play a game"+ "="*6+"\n\n")
print ("\tI will give you 3 hints, guess what animal I am")


print ("\n\n\tRound 1")
e.guess_who_am_i()
print ("\n\n\tRound 2")
t.guess_who_am_i()
print ("\n\n\tRound 3")
b.guess_who_am_i()


