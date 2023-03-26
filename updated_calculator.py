#simple python calculator
import random

number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special_char = ["@", "#", "$", "_", "&", "-", "+", "/", "*", "!", "?", "%"]
letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


while True:
    print()
    print("|______________________|")
    print("|  Simple Calculator!  |")
    print("|______________________|")
    print()
    
    what = input("What you want to do?\n1. 'Add'\n2. 'Subtract'\n3. 'Multiply'\n4. 'Division'\n5. 'Password generator' (hot)\n6. 'Decimal to Binary'\n7. 'Others'\n8. 'Exit'\n|")
    print()
    
    
    if what == "1" or what == "add":
        try:
            a = int(input("Enter 1st Value: "))
            b = int(input("Enter 2nd Value: "))
            sum = a+b
            print("The sum is:",sum)
        except Exception as e:
        	print("Please input valid number!\n")
       
       
        
    elif what == "2" or what == "subtract":
        try:
            a = int(input("Enter 1st Value: "))
            b = int(input("Enter 2nd Value: "))
            sub = a-b
            print("The Subtract is:", sub)
        except Exception as e:
        	print("Please input valid number!\n")
        
        
    elif what == "3" or what == "multiply":
        try:
            a = int(input("Enter 1st Value: "))
            b = int(input("Enter 2nd Value: "))
            multiply = a*b
            print("The multiply is:", multiply)
        except Exception as e:
        	print("Please input valid number!\n")
        
        
    elif what == "4" or what == "division":
        try:
            a = int(input("Enter 1st Value: "))        
            b = int(input("Enter 2nd Value: "))
            if b == 0:
                print("Cannot divided by '0'. Please input a valid number!")
            else:
                division = a/b
                print(f"The Division is: {division:.2f}")
        except Exception as e:
        	print("Please input valid number!\n")
        
    
    elif what == "5":
        print("\nGenerate any type of password!")
        is_generate = input("\n1. Randomly generate a password.\n2. To generate the password as you want.\n3. Exit\n\n|")

        gen_list = []
        password = ""
        if is_generate == "1":
            try:
                length = int(input("\nEnter the desired length of the password: "))
        
                for num in range(1, length//4+1):
                    gen_list += random.choice(number)
                for sp_char in range(1, length//4+1):
                    gen_list += random.choice(special_char)
                for char in range(1, length//2+1):
                    gen_list += random.choice(letter)
            
                random.shuffle(gen_list)
                password = "".join(gen_list[:length])
                print("\nGenerated password: ", password)
            except Exception as e:
            	print("Please input valid number.\n")



        elif is_generate == "2":
            try:
                n = int(input("\nHow many number do you want on your password: "))
                sp_ch = int(input("How many special character do you want on your password: "))
                lett = int(input("How many letter do you want on your password: "))
        
                for num in range(1, n+1):
                    gen_list += random.choice(number)
                for sp_char in range(1, sp_ch+1):
                    gen_list += random.choice(special_char)
                for char in range(1, lett+1):
                    gen_list += random.choice(letter)
            
                random.shuffle(gen_list)
                password = "".join(gen_list)
                print("\nGenerated password: ", password)
            except Exception as e:
            	print("Please input valid number.\n")


        elif is_generate == "3":
            print("\nExiting...\n\n[exited]")
            break
        
        else:
            print("\nPlease type 1, 2, or 3\n")
    
    
    
    
    elif what == "6":
    	def dec_to_binary(n):
    		bits = []
    		
    		while n > 0:
    			bits.append(n%2)
    			n = n//2
    		bits.reverse()
    		
    		binary = ""
    		for bit in bits:
    			binary += str(bit)
    		return binary
    		
    	
    		
    	num = int(input("Enter Decimal Number: "))
    	binary = dec_to_binary(num)
    	print("The binary is: ", binary)
    
    
    
                            
        
    elif what == "7" or what == "others":
        others = input("You want to calculate--\n1. 'temperature'\n2. 'area of circle'\n3. 'area of  triangle'\n4. 'area of square'\n5. 'Convert currency'\n6. 'Average'\n9. 'exit'\n|")
        
        
        
        if others == "1":
            try:
                f = int(input("Enter farenheit temperature: ")) 
                c = ((f-32)*5)/9
                print(f"The Celcious Temperature is: {c:.2f}°C")
            except Exception as e:
            	print("Please input valid number.\n")
            
            
        elif others == "2":
            try:
                pi = 3.14159
                r = int(input("Enter The radius: "))
                circle = pi*r*r
                print(f"The area of circle: {circle:.2f}")
            except Exception as e:
            	print("Please input valid number.\n")
            
            
            
        elif others == "3":
            try:
                base = int(input("Enter the value of base: "))
                height = int(input("Enter the value of height: "))
                area = 0.5*base*height
                print(f"The Area Of Triangle: {area:.2f}")
            except Exception as e:
            	print("Please input valid number.\n")
            
            
            
        elif others == "4":
            try:
                side = int(input("Enter A Side Of Square: "))
                area = side**2
                print(f"Area Of Square: {area:.2f}")
            except Exception as e:
            	print("Please input valid number.\n")
            
            
            
            
        elif others == "5":
            print("I am learning more!\nNow i convert just 'Taka to Dollar' & 'Dollar to Taka'.")
            ex = input("You Want To Covert--\n1. Dollar'$' to Taka'৳'\n2. Taka'৳' to Dollar'$'\n|")
            
            if ex == "1":
                try:
                    dollar = int(input("Enter amount of Dollars: "))
                    taka = dollar*106
                    print(f"{dollar}$ equal {taka:.3f}৳")
                except Exception as e:
                	print("Please input valid number.\n")
                	
            elif ex == "2":
                try:
                    taka = int(input("Enter amount of taka: "))
                    dollar = taka/106
                    print(f"{taka}৳ equal {dollar:.3f}$")   
                except Exception as e:
                	print("Please input valid number.\n")
                	         
            else:
                print("\nEnter Number(1,2) What You Want!\n")
        
        
        
        elif others == "6":
        	
            def avg(lst):
                s = sum(lst)
                n = len(lst)
                if n > 0:
                    return s / n
                else:
                    return 0

            try:
                nums = input("Enter numbers separated by commas: ")
                lst = [int(x) for x in nums.split(",")]
                average = avg(lst)
                print(f"The average is: {average:.2f}")
            except ValueError:
                print("Invalid input. Please enter numbers separated by commas!")
    
    

        
        elif others == "9":
            print("\nExiting...\n")
            print("[Exited]")
            exit()
        
        else:
            print("\nEnter Valid Number (1,2,3,4,5) what you want!\n")
    
    
    
    
    elif what == "8" or what == "exit":
        print("\nExiting...\n")
        print("[Exited]")
        exit()
    
    else:
        print("\nEnter Valid Number (1,2,3,4,5) what you want!\n")    