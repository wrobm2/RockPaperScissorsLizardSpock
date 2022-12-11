
import random
# ascii file has to be in the same directory, make sure that is true on repl
from ascii import ascii
# bank of possible words in relation to possible numbers
numbank = {"rock" : 0, "spock" : 1, "paper" : 2, "lizard" : 3, "scissors" : 4}
# bank of possible numbers in relation to possible words 
wordbank = {0 : "rock", 1 : "spock", 2 : "paper", 3 : "lizard", 4 : "scissors"}
# bank of possible options as a normal list
listpossible = ("rock", "paper", "scissors", "lizard", "spock", "shoot", "results")
# initializing variables
# number of times computer has won
computerwins = 0
# number of times you have tied 
ties = 0
# number of times you have won
userwins = 0

f = False
# whether or not user has shot
shot = False

def istwooneword(x):
    for i in x:
        counter = 0 
        for j in listpossible:
            if j in x:
                counter += 1
        if counter > 1:
            return True
        else:
            return False
        
def whatisit(x):
    for i in listpossible:
        if i in x:
            return str(i), True
    return False, False
        
def cleardupes(x):
    return list(dict.fromkeys(x))
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
    
ascii("start")
while True:
    input1 = input(" Pick one of the following: Rock, Paper, Scissors, Lizard Spock!\n Or type Results to see the stats on games played already\n ")
    input1 = input1.lower()
    if checkmultiple(input1) == True:
        print("There are multiple options in your answer, please try again")
        continue
    inputparsed, itsThere = whatisit(input1)
    if istwooneword(input1) == True:
        print("You have two valid answers within one word, please only select one choice.")
        continue
    if inputparsed == "shoot" and shot == False:
        print(" Bam bam bam bam bam")
        print(" you found the secret phrase ")
        print(" you get 10 wins ")
        print(" (you cant do this again for the duration of the game)")
        ascii("explosion")
        userwins += 10
        shot = True
        continue
    elif inputparsed == "shoot":
        print("I told you you cant do it again")
        print("im taking a win away")
        userwins -= 1
        continue
    elif inputparsed == "results":
        print("The computer has won", computerwins, "times")
        print("you have tied", ties, "times")
        print("You have won", userwins, "times")
        continue
    if itsThere:
        user = (numbank[inputparsed])
        computer = random.randrange(0,5)
        print ("You picked", wordbank[user])
        print ("The computer picked", wordbank[computer])
        winner = (user-computer) % 5
        # use if/elif/else to determine winner
        if computer == user:
            print("You Tied!")
            ties += 1
            ascii("tie")
        elif winner < 3:
            print("You win!")
            userwins += 1
            ascii(wordbank[user])
        else:
            print("You lose!")
            computerwins += 1
            ascii(wordbank[computer])    
    else: 
        print("please type a valid answer please i beg please i just wanna play rock paper scissors lizard spock please man ill do anything ill do anything please dude i beg please please please please please")
