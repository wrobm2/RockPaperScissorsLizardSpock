import random
list = ["rock", "paper", "scissors", "lizard", "spock"]
computercount = 0
usercount = 0 
tie = 0 
flag = "Results"
isthere = False
def is_it_there():
	for i in list:
		if i in answer:
			isthere = True
			return isthere
def ascii(fname):
	if fname == "rock":
		print("""⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠈⠈⠉⠉⠈⠈⠈⠉⠉⠉⠉⠉⠉⠉⠉⠙⠻⣄⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⣄⠀⠀⢀⠀⢀⣀⣤⠄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⣉⣩⣤⠴⠶⠶⠒⠛⠛⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⠤⠶⠒⠚⠋⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣾⡍⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣫⣭⣷⠶⢶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠶⠶⠖⠚⠛⠛⣹⠏⠀⠀⠀⠀⠀⠀⠀⠀⠴⠛⠛⠉⡁⠀⠀⠙⠻⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡷⠷⢿⣦⣤⣈⡙⢿⣿⢆⣴⣤⡄⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⣤⡀⣸⡄⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣿⣟⣩⣤⣴⣤⣌⣿⣿⣿⣦⣹⣿⢁⣿⣿⣄⣀⡀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣿⠋⠻⢿⡁⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠿⠛⢦⣽⣿⣿⢻⣿⣿⣿⣿⠋⠁⠘⣿⣿⣿⣿⣿⣿⣼⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⠁⠀⠀⠙⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠿⣿⣯⣼⣿⡿⠟⠃⠀⠀⠀⣿⣿⣿⣿⣿⡛⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣧⣴⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣺⠟⠃⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⢁⣀⣀⣀⣀⣀⣠⣀⣀⢀⢀⢀
⠀⠀⢿⠿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠙⠛⠛⠙⢻⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡇⠀⠘⠃⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡟⢿⣿⣆⠀⣸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢄⡼⠁⢀⣀⡀⠀⠀⠀⣦⣄⠀⣠⡄⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣷⣬⢻⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⣰⣿⡿⠿⠦⢤⣴⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠒⣿⣿⣿⡿⠟⠹⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⠸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡖⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡿⣾⣿⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣆⣀⣀⣤⣴⣶⣶⣾⣿⣷⣦⣴⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡇⣿⣿⡛⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢾⡟⠛⠛⠻⠛⠛⠛⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠓⢁⣬⣿⠇⠀⠀⠀⠀⠀⢠⡀⠀⠀⠀⠀⠀⢰⡿⣻⠇⠀⠀⠀⠀⠀⣠⣶⣶⣶⣶⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢐⣯⠞⠁⠀⠀⠀⠀⠀⠀⣄⠱⣄⠀⠀⠀⠀⠸⡧⠟⠆⠀⠀⠀⠀⠘⠿⢿⠿⠿⣿⡿⣿⠃⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⡈⠂⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢠⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠒⡄⠀⠀⠑⠄⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣦⣦⣼⡏⠳⣜⢿⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⢠⣷⣦⣤⣀⣀⣀⣴⣿⣿⣿⣿⣿⡿⠻⠆⠸⣎⣧⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⣠⡄⠀⣿⢹⡇⢸⡀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿""")

	if fname == "lizard":
		print("""
		
                       )/_
             _.--..---"-,--c_
        \L..'           ._O__)_
,-.     _.+  _  \..--( /           a:f
  `\.-''__.-' \ (     \_      
    `'''       `\__   /\
                ')
		""")
	if fname == "spock":
		print("""
		
                     .......................... 
                 ................................... 
              ......................................... 
            ............................................. 
           ................................................ 
          .................................................. 
         .................................................... 
         ......;%;%%%%%%%%%%%%%%%%%%%%%%%%%%%;%%.............. 
         .....;%%%;;;;%%%%%%%%%%%%%%%%%%;;;;%%%%..............% 
         .....%%%%%%%%;;;%%%%%%%%%%%%;;;%%%%%%%%%............%%% 
         /....%%%%%%%%%%%%;%%%%%%%%;%%%%%%%%%%%%%%..........;%%% 
         //...%%%a@@`  '@%%//%%%%%%%%@`  '@@a%%%%%%........;%/%% 
         //...%@@@@@aaa@@@%//%%%%%%@@@@aaa@@@@@%%%%%......%%/%% 
         //...%%%%%%%%%%%%%//%%%%%%%%%%%%%%%%%%%%%%%%....%%/%%% 
          //..%%%%%%%%%%%%//%%%%%%%%%%%%%%%%%%%%%%%%%...%%/%%% 
           //.%%%%%%%%%%%%//%%%%%%%%%%%%%%%%%%%%%%%%%..%%/%%% 
            //%%%%%%%%%%%//%%%%%%%%%%%%%%%%%%%%%%%%%%..%/%%% 
             ;%%%%%%%%%%%//%%%%%%%%%;/%%%%%%%%%%%%%%%.%%% 
               %%%%%%%%%//%%%%%%%%%%%;/%%%%%%%%%%%%%%%% 
                %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%/ 
                 ;%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%// 
                   %%%%%<<<<<<<<<<<<<<<<<%%%%%%%%%%;// 
                    %%%%%<<<<<<<<<<<<<<<%%%%%%%%%%;/// 
                     %%%%%%%%%%%%%%%%%%%%%%%%%%%;///// 
                      %%%%%%%%%%%%%%%%%%%%%%%%;///////. 
                      /;%%%%%%%%%%%%%%%%%%%;////////.... 
                      ///;%%%%%%%%%%%%%%;////////......... 
                    ...///////////////////////.............. 
                  ........////////////////................,;;, 
               ,;............/////////.................,;;;;;;;;, 
           ,;;;;;;,................................,;;;;;;;;;;;;;;, 
       ,;;;;;;;;;;;;;,........................,;;;;;;;;;;;;;;;;;;;; 
   ,;;;;;;;;;;;;;;;;;;;;;,................,;;;;;;;;;;;;;;;;;;;;;;;; 
 ,;;;;;;;;;;;;;;;;;;;;;;;;;;,.........,;;;;;;;;;;;;;;;;;;;;;;;;;;;; 
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;/#\;;;;;;;;;;; 
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;/####\;;;;;;;;; 
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;/#######\;;;;;;;		""")
	if fname == "scissors":
		print("""
    _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.		""")
	if fname == "paper":
		print("""
		
                                                        ██████          
                                                      ██░░░░░░██        
                                ██████              ██░░░░░░░░░░██      
                          ██████      ██          ██░░░░░░░░░░░░░░██    
                        ██    ██      ██        ██░░░░░░░░░░░░░░░░██    
                        ██    ████    ██    ████░░░░░░░░░░░░░░░░░░░░██  
                          ██  ██  ████  ████░░░░░░░░░░░░░░░░░░░░░░░░██  
                            ██  ████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░██  
                              ████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
                        ██████░░████░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
                ████████░░░░░░░░░░██░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
    ████████████░░░░░░░░░░░░░░░░░░████░░██░░░░░░░░░░░░░░░░░░░░░░░░░░██  
  ██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░████░░░░░░░░░░░░░░░░░░░░████    
██░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░████░░██░░░░░░░░░░██████████        
████████████░░░░░░░░░░░░░░░░░░░░░░░░░░██░░██░░████████                  
    ████░░░░██░░░░░░░░░░░░░░░░░░░░░░░░██░░████                          
  ██░░░░██░░██░░░░░░░░░░░░░░░░░░░░░░██████                              
  ██░░░░░░██░░██░░░░░░░░░░░░░░░░████                                    
  ██░░██████░░██░░░░░░░░░░░░████                                        
  ██░░██░░██████░░░░░░░░████                                            
  ██░░░░████████░░░░░░██                                                
    ██░░░░░░░░██░░░░██                                                  
    ██░░░░░░░░██░░██                                                    
      ████░░░░████                                                      
          ████                                                          
		""")
	if fname == "tie":
		print("""
            ,a_a
           {/ ''\_
           {\ ,_oo)
           {/  (_^_____________________
 .=.      {/ \___)))*)----------;=====;`
(.=.`\   {/   /=;  ~~           |||::::
    \ `\{/(   \/\               |||::::
     \  `. `\  ) )              |||||||
      \    // /_/_              |||||||
       '==''---))))             |||||||		
		""")

print("""                                                                         
                                                                         
                         ┌─────────────────────┐
                         │                     │
                         │                     │
                         │                     │
                         │                     │
                         │                     │
                         │      ROCK           │
                         │                     │
                         │                     │
                         │                     │             ▼
                         │                     │
               ┌───────► │                     │
               │         │                     │
               │         └─┬───────┬─────────┬─┘
               │           ├───────┘         │ ▲
               │           │                 │ │
┌──────────────┴──────┐    │                 │ │
│                     │    │                 │ │ ┌┬───────────────────┐
│                     │    │                 │ └─┼┘                   │
│                     │    │                 │   │                    │
│                     │    │                 │   │                    │
│                     │    │                 │   │                    │
│                     │    │                 │   │                    │
│      SPOCK          │◄───┼─────────────────┼───┼─   PAPER           │
│                     │    │                 │   │                    │
│                     │    │                 │   │                    │
│                     │    │                 │   │                    │
│                     ├────┼───┬───────────┐ │   │                    │
│                     │    │   ├───────────┼─┼──►│                    │
└─────────────────────┘    │   │           │ │   │                    │
              ▲            │   │           │ │   └────────────────────┘
              │            │   │           │ │              ▲
              │            │   │           ▼ │              │
              └─┬──────────▼───┴───┐        ┌▼──────────────┴───────┐
                │                  │        │                       │
                │                  │        │                       │
                │                  │        │                       │
                │                  │        │                       │
                │                  │        │                       │
                │                  │        │                       │
                │     LIZARD       │◄───────┤         SCISSORS      │
                │                  │        │                       │
                │                  │        │                       │
                │                  │        │                       │
                │                  │        │                       │
                │                  │        │                       │
                │                  │        └───────────────────────┘
                └──────────────────┘                                                                         
                                                                         
""")
while True:
	answer = input("Please choose one: Rock, Paper, Scissors, Lizard, or Spock: ")
	computer = random.choice(list)
	if answer == flag:
		print("The computer has won", computercount, "times")
		print("You have tied", tie, "times")
		print("You have won", usercount, "times")
		continue
	answer = answer.lower()
	print(answer)
	# next line commented out because its stupid but if i break the good way
	# i will use it
	# if answer in list or "rock" in answer or "paper" in answer or "scissors" in answer or "lizard" in answer or "spock" in answer:
	
	
	# This is really dumb, and i feel like there are better ways to do it, but i dont understand
	# any of the ways that are better
	if answer in list or is_it_there() == True:
		print(computer)
		if computer in answer:
			print("Tie")
			tie += 1
			ascii("tie")
		elif computer == "rock" and "scissors" in answer:
			print("Computer wins")
			print("Rock crushes Scissors")
			computercount += 1
			ascii("rock")
		elif computer == "rock" and "lizard" in answer:
			print("Computer wins")
			print("Rock crushes Lizard")
			computercount += 1
			ascii("rock")
		elif computer == "paper" and "rock" in answer:
			print("Computer wins")
			print("Paper Covers Rock")
			computercount += 1
			ascii("paper")
		elif computer == "paper" and "spock" in answer:
			print("Computer wins")
			print("Paper disproves Spock")
			computercount += 1
			ascii("paper")
		elif computer == "scissors" and "paper" in answer:
			print("Computer wins")
			print("Scissors cuts Paper")
			computercount += 1
			ascii("scissors")
		elif computer == "scissors" and "lizard" in answer:
			print("Computer wins")
			print("Scissors Decapitates Lizard")
			computercount += 1
			ascii("scissors")
		elif computer == "lizard" and "spock" in answer:
			print("Computer wins")
			print("Lizard poisons Spock")
			computercount += 1
			ascii("lizard")
		elif computer == "lizard" and "paper" in answer:
			print("Computer wins")
			print("Lizard eats Paper")
			computercount += 1
			ascii("lizard")
		elif computer == "spock" and "rock" in answer:
			print("Computer wins")
			print("Spock Vaporizes Rock")
			computercount += 1
			ascii("spock")
		elif computer == "spock" and "scissors" in answer:
			print("Computer wins")
			print("Spock Smashes Scissors")
			computercount += 1
			ascii("spock")
		elif "rock" in answer and "scissors" in computer:
			print("You won!")
			print("Rock crushes Scissors")
			usercount += 1
			ascii("rock")
		elif "rock" in answer and "lizard" in computer:
			print("You won!")
			print("Rock crushes Lizard")
			usercount += 1
			ascii("rock")
		elif "paper" in answer and "rock" in computer:
			print("You won!")
			print("Paper Covers Rock")
			usercount += 1
			ascii("paper")
		elif "paper" in answer and "spock" in computer:
			print("You won!")
			print("Paper disproves Spock")
			ascii("paper")
			usercount += 1
		elif "scissors" in answer and "paper" in computer:
			print("You won!")
			print("Scissors cuts Paper")
			ascii("scissors")
			usercount += 1
		elif "scissors" in answer and "lizard" in computer:
			print("You won!")
			print("Scissors Decapitates Lizard")
			ascii("scissors")
			usercount += 1
		elif "lizard" in answer and "spock" in computer:
			print("You won!")
			print("Lizard poisons Spock")
			ascii("lizard")
			usercount += 1
		elif "lizard" in answer and "paper" in computer:
			print("You won!")
			print("Lizard eats Paper")
			ascii("lizard")
			usercount += 1
		elif "spock" in answer and "rock" in computer:
			print("You won!")
			print("Spock Vaporizes Rock")
			ascii("spock")
			usercount += 1
		elif "spock" in answer and "scissors" in computer:
			print("You won!")
			print("Spock Smashes Scissors")
			ascii("spock")
			usercount += 1
	else:
		print("Invalid Choice! try again!")