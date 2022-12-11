
import random
import os
# ascii file has to be in the same directory, make sure that is true on repl
from ascii import ascii
# bank of possible words in relation to possible numbers
numbank = {"rock" : 0, "spock" : 1, "paper" : 2, "lizard" : 3, "scissors" : 4, "shoot" : 5, "results" : 6}
# bank of possible numbers in relation to possible words 
# wordbank = {0 : "rock", 1 : "spock", 2 : "paper", 3 : "lizard", 4 : "scissors"}
# learned i can just reverse the list and do not need to assign a seperate list. i already had typed out the seperate list, but in the future i should do this. 
wordbank = dict(zip(numbank.values(), numbank.keys()))

os.system('cls' if os.name == 'nt' else 'clear')# bank of possible options as a normal list

listpossible = [key for key in numbank]
# arrays for win conditions
array0 = ["tie", "win", "win", "lose", "lose"] 
array1 = ["lose", "tie", "win", "win", "lose"]
array2 = ["lose", "lose", "tie", "win", "win"]
array3 = ["win", "lose", "lose", "tie", "win"]
array4 = ["win",  "win", "lose", "lose", "tie"]
arrayfinal = [array0,array1,array2,array3,array4]
# initializing variables
# number of times computer has won
computerwins = 0
# number of times you have tied 
ties = 0
# number of times you have won
userwins = 0

f = False
# whether or not the user has said shoot in this loop yet
shot = False
# Function to find out what answer the user has picked 
def whatisit(x):
    for i in listpossible:
        if i in x:
            return str(i), True
    return False, False
        
def cleardupes(x):
    return list(dict.fromkeys(x))
    
    
   
def checkmultiple(x):
    # split the input string into a list of words, using whitespace as the delimiter
    words = x.split(" ")

    # remove any duplicate words from the list
    words = list(set(words))

    # count the number of words in the list that are also in listpossible
    count = sum(1 for word in words if word in listpossible)

    # return True if there are more than one word in the list that is also in listpossible
    # otherwise, return False
    return count > 1





    """
def checkmultiple(x):
    x = x.split(" ")
    multilist = cleardupes(x)
    counter = 0 
    for i in multilist:
        for j in listpossible:
            if i == j:
                counter += 1
    if counter > 1:
        return True
    else:
        return False
    print(multilist)
    """
    
ascii("start")
while True:
    x = input(" Pick one of the following: Rock, Paper, Scissors, Lizard Spock!\n Or type Results to see the stats on games played already\n ")
    x = x.lower()
    if checkmultiple(x) == True:
        print("There are multiple options in your answer, please try again")
        continue
    x, f = whatisit(x)
    if x == "shoot" and shot == False:
        print(" Bam bam bam bam bam")
        print(" you found the secret phrase ")
        print(" you get 10 wins ")
        print(" (you cant do this again for the duration of the game)")
        ascii("explosion")
        userwins += 10
        shot = True
        continue
    elif x == "shoot":
        print("I told you you cant do it again")
        print("im taking a win away")
        userwins -= 1
        continue
    elif x == "results":
        print("The computer has won", computerwins, "times")
        print("you have tied", ties, "times")
        print("You have won", userwins, "times")
        continue
    if f:
        user = (numbank[x])

        computer = random.randrange(0,5)
        print ("You picked", wordbank[user])
        print ("The computer picked", wordbank[computer])
        arraycomputerguess = arrayfinal[computer]
        gameresult = arraycomputerguess[user]
        if gameresult == "tie":
            print("You Tied!")
            ties += 1
            ascii("tie")
        elif gameresult == "win":
            print("You win!")
            userwins += 1
            ascii(wordbank[user])
        elif gameresult == "lose":
            print("You lose!")
            computerwins += 1
            ascii(wordbank[computer])    
    else: 
        print("please type a valid answer please i beg please i just wanna play rock paper scissors lizard spock please man ill do anything ill do anything please dude i beg please please please please please")
