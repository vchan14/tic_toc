import time
import random 
def printLayout(myList):
    print("   1  2  3")
    print("A {0} | {1} | {2}".format(myList[0][0], myList[0][1], myList[0][2])) 
    printLine()
    print("B {0} | {1} | {2}".format(myList[1][0], myList[1][1], myList[1][2])) 
    printLine()
    print("C {0} | {1} | {2}".format(myList[2][0], myList[2][1], myList[2][2])) 


def printLine(): 
    print("  --  -- --")


def check(signature, myList): 
    if ( (myList[0][0] == signature) &
         (myList[0][1] == signature) &
         (myList[0][2] == signature) ):
            return True
    
    if ( (myList[1][0] == signature) &
         (myList[1][1] == signature) &
         (myList[1][2] == signature) ):
            return True
    if ( (myList[2][0] == signature) &
         (myList[2][1] == signature) &
         (myList[2][2] == signature) ):
            return True

    if ( (myList[0][0] == signature) &
         (myList[1][0] == signature) &
         (myList[2][0] == signature) ):
            return True
    if ( (myList[0][1] == signature) &
         (myList[1][1] == signature) &
         (myList[2][1] == signature) ):
            return True

    if ( (myList[0][2] == signature) &
         (myList[1][2] == signature) &
         (myList[2][2] == signature) ):
            return True

    if ( (myList[2][2] == signature) &
         (myList[1][1] == signature) &
         (myList[0][0] == signature) ):
            return True
    if ( (myList[0][2] == signature) &
         (myList[1][1] == signature) &
         (myList[2][0] == signature) ):
            return True


#main 
myList = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]] 


printLayout(myList)

print("\nWelcome to Tic-Tac-Toc game\n")

while(True):
   user_input = input("Which cell do you want cross? i.e A3, B1 :  ")
   user_row = ord(user_input[0]) - ord("A")
   user_column = int(user_input[1]) - 1
   if(myList[user_row][user_column] != " "): 
       print("Bro you already cross this one out")
       continue; 
   myList[user_row][user_column] = "x" 
   printLayout(myList)
   if(check("x", myList)):
       print("Good job Bro, Love you") 
       break
   print("Computer is thinking.")
   time.sleep(0.7)
   print("Computer is thinking..")
   time.sleep(0.7)
   print("Computer is thinking...")
   time.sleep(0.3)


   while(True):
        pc_row = random.randint(0,2)
        pc_column = random.randint(0,2)
        if(myList[pc_row][pc_column] != " "):
            continue
        myList[pc_row][pc_column] = "O"
        printLayout(myList)
        if(check("O", myList)): 
            print("FFFFF pho the PC wins")
        break



   

   
    


    




    

