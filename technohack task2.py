import random
print(" Rules of Rock paper scissor game \n"
+"Rock vs paper -----> paper wins \n"
+"Rock vs scissor ---> Rock wins \n"
+"paper vs scissor --> scissor wins \n")
while True:
    print("Now please enter your choice no. \n 1. Rock \n 2. paper \n 3. scissor \n")
 
    ch = int(input("Now Your turn: "))

    if ch == 1:
            choice_name = 'Rock'
    elif ch == 2:
            choice_name = 'paper'
    elif ch==3:
            choice_name = 'scissor'
    else:
           print("Wrong input")
           break
    
    print("Your choice is: " + choice_name)
    print("\ncomputer turn")
        
    comp_choice = random.randint(1, 3)
        
    while comp_choice == ch:
        comp_choice = random.randint(1, 3)
          
    if comp_choice == 1:
            comp_choice_name = 'Rock'
    elif comp_choice == 2:
            comp_choice_name = 'paper'
    else:
            comp_choice_name = 'scissor'
    print("So computer choice is: " + comp_choice_name)

    print("******----result----******")
            
    if((ch == 1 and comp_choice == 2) or (ch == 2 and comp_choice ==1 )):
                print("paper wins => ", end = "")
                final_result = "paper"
    elif((ch == 1 and comp_choice == 3) or (ch == 3 and comp_choice == 1)):
                print("Rock wins =>", end = "")
                final_result = "Rock"
    else:
                print("scissor wins =>", end = "")
                final_result = "scissor"
    if final_result == choice_name:
            print("<== You are the winner ==>")
    else:
        print("<== Computer wins ==>")
    print("Do you want to play again? (Y/N)")
    ans = input()
                
    if ans == 'n' or ans == 'N':
        break
           
print("\nThanks for playing")