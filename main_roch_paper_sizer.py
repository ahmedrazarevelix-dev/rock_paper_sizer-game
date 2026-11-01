from random import choice
'''
-1 for rock
1 for paper
0 for sizer
'''
computer= choice([-1, 1, 0])
you=input("Enter your choice:")
youstr={'r':-1, 'p':1, 's':0}
reversestr={-1:"rock", 1:"paper", 0:"sizer"}
you=youstr[you]

print(f"you chose {reversestr[you]}\ncomputer chose {reversestr[computer]}")

if(computer==you):
    print("Its a draw")

else:
    if(computer==-1 and you==1):   
        print("you win")

    elif(computer==-1 and you==0):   
        print("you lose")

    elif(computer==1 and you==0):  
        print("you win")

    elif(computer==1 and you==-1): 
        print("you lose")

    elif(computer==0 and you==-1): 
        print("you win")

    elif(computer==0 and you==1): 
        print("you lose")
    
    else:
        print("something went wrong")
'''
else:
    if(computer==-1 and you==1):  -2 
        print("you win")

    elif(computer==-1 and you==0):   -1
        print("you lose")

    elif(computer==1 and you==0):   1
        print("you win")

    elif(computer==1 and you==-1):  2
        print("you lose")

    elif(computer==0 and you==-1):  1
        print("you win")

    elif(computer==0 and you==1): -1
        print("you lose")
    
    else:
        print("something went wrong")
'''

