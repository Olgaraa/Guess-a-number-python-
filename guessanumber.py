import random 

def guess_my_number (guessed): 
    chosen=random.randint(1,10) 
    print("The generated number is " +str(chosen) + ".Your guess (" +str(guessed) +") ", end = '') 
    if (guessed>chosen) or (guessed<chosen): 
        print ("is not correct.") 
    else: print ("is correct.") 

while (True):
    try: 
        inp = int(input("Guess a number in range 1 to 10: ")) 
    except: 
       print ("This is not a number!") 
    else: 
        if inp>10 or inp<1: 
            print ("You can only use a number from 1 to 10!") 
        else: 
            break 
guess_my_number(int(inp)) 
