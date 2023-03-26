#rock paper scissor

from random import randint

while True:
    score = 0
    computer_scr = 0
    draw = 0
    print("_______________________")
    isplay = input("1. Start Game\n2. Exit\n|")
    
    print("_______________________")
    if isplay == "1":
        name = input("Enter your name: ")
        print(f"Welcome, {name}! here you will get 10 chance to beat me!\n")
        for i in range(1,11):
            print("Your choice?\n1. rock\n2. paper\n3. scissor\n")
            your_guess = input("|")
            print()
            computer_guess = randint(1,3)

            if your_guess == "1" and computer_guess == 1:
                print("⚠️You And Computer Chose Same One!")
                draw+=1
      
            elif your_guess == "1" and computer_guess == 2:
                print("Computer Chose Paper🖐️")
                print("You Chose Rock✊")
                print("You Lost!😵")
                computer_scr+=1
            

            elif your_guess == "1" and computer_guess == 3:
                print("Computer Chose Scissor✌️")
                print("You Chose Rock✊")
                print("You Win!🏆")
                score+=1
        
            elif your_guess == "2" and computer_guess == 1:
                print("Computer Chose Rock✊")
                print("You Chose Paper🖐️")
                print("You Win!🏆")
                score+=1
        
            elif your_guess == "2" and computer_guess == 2:
                print("⚠️You And Computer Chose Same One!")
                draw+=1

            elif your_guess == "2" and computer_guess == 3:
                print("Computer Chose Scissor✌️")
                print("You Chose Paper🖐️")
                print("You Lost!😵")   
                computer_scr+=1 

            elif your_guess == "3" and computer_guess == 1:
                print("Computer Chose Rock✊")
                print("You Chose Scissor✌️")
                print("You Lost!😵") 
                computer_scr+=1
    
            elif your_guess == "3" and computer_guess == 2:
                print("Computer Chose Paper🖐️")
                print("You Chose Scissor✌️")
                print("You Win!🏆")
                score+=1
        
            elif your_guess == "3" and computer_guess == 3:
                print("⚠️You And Computer Chose Same One!")
                draw+=1
    
            else:
                print("Invalid input! You Can Just Type- 1, 2, 3")
            print()

        #updated score
        up_score = 100/10*score
        up_computer_scr = 100/10*computer_scr

        #user info
        print(f"{name}'s Score Is",score)
        print("Computer's Score Is",computer_scr)
        
        print(f"{draw} draws!\n")
        
        print(f"{name}'s win Rate is {up_score}%")
        print(f"Computer's win Rate is {up_computer_scr}%")

        
        if computer_scr > score:
        	print("_____________________")
        	print("\nComputer is win!")
        	print("_____________________")
	
        elif computer_scr == score:
        	print("_____________________")
        	print(f"\n{name}, Our score is same! Let's play again!")
        	print("_____________________")

        elif computer_scr < score:
        	print("_____________________")
        	print(f"\n{name} is win!")
        	print("_____________________")
        	
       
    elif isplay == "2":
    	print("Exiting...\n")
    	print("[Exited]")
    	exit()
    	
    	
    else:
    	print("Valid input 1 or 2. \n")
    print("\n\n\n\n\n\n\n\n")
    
    
#end