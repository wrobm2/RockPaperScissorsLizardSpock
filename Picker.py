

print("""

Which implementation would you like to pick?
    1) My first try, (implementation_one.py), easily my worst.
       Just an absolute ton of if statements
    2) My second try, (implemetation_two.py), the one i am
       most likely to submit, and the most well commented /
       easy to understand one that i wrote myself without 
       the help of an "advanced language model". also most 
       fully featured.
    3) My third try, (implementation_three.py). uses 
       modulo instead of a bunch of arrays or if statements
       or rules to find out who won the game.
       Probably the best implementation, but is confusing
       and i didnt want to make this assignment more confusing
       than necessary.
    4) ChatGPT created rules based version (implementation_four.py).
       Hasnt been built out for cool features
       But is definitely the easiest to understand
       I am including it purely to show you how cool
       ChatGPT is.

""")

one = ["one", "first", "1"]
two = ["two", "second" "2"]
three = ["three", "third", "3"]
four = ["four", "fourth", "4"]

userinput = input(" ")
def isAnyArrayItemInString(string, array):
  lowered = string.lower()
  return any(string in lowered for string in array)




if isAnyArrayItemInString(userinput, one):
    print("hello")
    print(userinput)
    # exec(open('Implementation_one.py').read())
    import Implementation_one
if isAnyArrayItemInString(userinput, two):
    print("hello2")
    import Implementation_two
    # exec(open('Implementation_two.py').read())
if isAnyArrayItemInString(userinput, three):
    import Implementation_three
    # exec(open('Implementation_three.py').read())
if isAnyArrayItemInString(userinput, four):
    import Implementation_four
    # exec(open('Implementation_four.py').read())
