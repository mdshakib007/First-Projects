#mcq of physics

name = input("Entrer Your Name: ")
print("\nWelcome To The Quiz Game," ,name)

isPlay = input("\nWould you like to play?\n('yes' or 'no') >>> ")

if isPlay == "yes":
    print("\nQuiz Starting...\n")
    
    
    score = 0
    
    
    
    q1 = input("1)  Which of the following is a scalar equation?\n1. Velocity\n2. Speed\n3. Acceleration\n")
    
    if q1 == "2":
        print("Correct Answer!\n")
        score+=5
        
    else:
        print("Wrong Answer!\nCorrect Answer Is -2\n")
        
        
        
    q2 = input("2)  Which of the following has higher conductivity?\n1. Air\n2. Diamond\n3. Gold\n")
    
    if q2 == "3": 
        print("Correct Answer!\n")
        score+=5
        
    else:
        print("Wrong Answer!\nCorrect Answer Is -3\n")
        
        
    
    q3 =  input("3)  Eye sensitivity to any light The most?\n1. Blue\n2. Green\n3. Red\n") 
    
    if q3 == "2": 
        print("Correct Answer!\n")
        score+=5
        
    else: 
        print("Wrong Answer!\nCorrect Answer Is -2\n")
        
        
        
    q4 = input("4)  Who is the discoverer of radium?\n1. Roentgen\n2. Max Planck\n3. Pier Currie\n")
    
    if q4 == "3": 
        print("Correct Answer!\n")
        score+=5
        
    else:
        print("Wrong Answer!\nCorrect Answer Is -3\n")
        
    
    
    q5 = input("5)  Which is the unit of luminous intensity?\n1. Cd\n2. K\n3. A\n")
    
    if q5 == "1": 
        print("Correct Answer!\n")
        score+=5
        
    else: 
        print("Wrong Answer!\nCorrect Answer Is -1\n")
        
        
        
    q6 = input("6)  Acceleration is—\n1. Scalar Number\n2. Vector Number\n3. None of them\n")
    
    if q6 == "2": 
        print("Correct Answer!\n")
        score+=5
        
    else: 
        print("Wrong Answer!\nCorrect Answer Is -2\n")
        
        
        
    q7 = input("7)  Concave mirror has focal plane and principal axis What is the value of the intermediate angle?\n1. 90°\n2. 180°\n3. 270°\n")
    
    if q7 == "1": 
        print("Correct Answer!\n")
        score+=5
        
    else: 
        print("Wrong Answer!\nCorrect Answer Is -1\n")
        
    
    
    q8 = input("8)  Who gave the quantum theory?\n1. Newton\n2. Einstein\n3. Max Planck\n")
    
    if q8 == "3":
        print("Correct Answer!\n")
        score+=5
        
    else: 
        print("Wrong Answer!\nCorrect Answer Is -3\n")
        
    
    
    q9 = input("9)  Which of the following is a semi-conductor?\n1. Metal\n2. Rubber\n3. Germanium\n")
    
    if q9 == "3": 
        print("Correct Answer!\n")
        score+=5
    
    else: 
        print("Wrong Answer!\nCorrect Answer Is -3\n")
    
    
    
    q10 = input("10)  How do green flowers look in red light?\n1. Black\n2. Yellow\n3. Colorless\n")
    
    if q10 == "1": 
        print("Correct Answer!\n")
        score+=5
        
    else: 
        print("Wrong Answer!\nCorrect Answer Is -1\n")

   
      
    print("Your Total Score Is:", score)   
    print("Correct Answer ",(score/50)*100 ,"%")
   
    if score == 50:
        print("\nCONGRATULATIONS! You Have Unlocked Level 2")
        
    else:
        print("\nNOTE: <<<You Need 50 Points To Unlock Level 2>>>")
    
else:
    print("     Quit Game!\n<<<Give Feedback>>>")  
