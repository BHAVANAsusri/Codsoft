import random

l1=['rock','paper','scissors']
pq=1
player=input("Enter your name:")


def rock_paper_scissors():
    print("1.rock  2.paper  3.scissors")
    player1=input("Enter your choice:")
    comp=random.choice(l1)
    print("computer:",comp)

    if comp=='rock':
        if  player1=='paper':
            print("computer lost "+player+"  wins")
          
        elif player1=='scissors':
            print("Computer won "+player+ " lost")
           
        elif player1=='rock':
            print("Tie")
        else:
            print("Invalid")
            
    elif comp=='paper':
        if player1=='scissors':
            print("computer lost "+player+"  wins")
            
        
        elif player1=='rock':
            print("Computer won "+player+ " lost")
            
        elif player1=='paper':
            print("Tie")    
        else:
            print("invalid ")
        
    elif comp=='scissors':
        if player1=='rock':
            print("computer lost "+player+"  wins")
           
        
        elif player1=='paper':
            print("Computer won "+player+ " lost")
           
        
        elif player1=='scissors':
            print("Tie")
    
    else:
         print("Invalid ")
    
rock_paper_scissors()  

while True:
   
    
    pq=input("Would you like to continue(yes or not):")
   
    if pq=='yes':
        rock_paper_scissors()
     
    
    elif pq=='no':
        break
    else:
        print("Invalid")
