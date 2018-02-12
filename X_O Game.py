print("                                      welcome                                         ")
print("X_O Game , Try to win  -__-") 
#input two names of two players
print("Player one takes 'X'")
print("Player two takes 'O'")
P1_name=str(input("please enter player one name : "))
P2_name=str(input("Please enter player two name : "))
#Player one is "X"
#player two is "O"
# this variable is used to restart  the game 
playing = True

while( playing):
    list1=[] # this is used to avoid repeatation of user choice
#creating board divided into 3 columns and 3 rows 
    board = [[0, " 0 "], [1, " 1 "], [2," 2 "], [3," 3 "], [4," 4 "], [5," 5 "], [6," 6 "], [7," 7 "], [8," 8 "]]
    i=0
#Game loop 
    while(i<9):
        print("----+---+---- \n"+"|"+board[0][1]+"|"+board[1][1]+"|"+board[2][1]+"|"+"\n----+---+----\n"+"|"+board[3][1]+"|"+board[4][1]+"|"+board[5][1]+"|"+"\n----+---+---- \n"+"|"+board[6][1]+"|"+board[7][1]+"|"+board[8][1]+"|"+"\n----+---+---- \n")
        if(i%2==0):
            print(P1_name+"'s turn")
            print("Please enter number from board in front:")
        else:
            print(P2_name+"'s turn")
            print("Please enter number from board in front:")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#to fill board with x and o
        right_num = True # this variabe is used to detect Error of user input 
        x=None
        x=int()
        while(right_num):
            con =True #this variable used to avoid repeatation of user input number 
            while (con):
                x=int(input())
                if((x>=0)and(x<9)):
                    if (x in list1):
                       print("Error! , this number is chosen before ,choose another one ")
                    else :
                        if(i%2==0):
                            board[x][1]=" X "
                        else:
                            board[x][1]=" O "
                        con = False
                        list1.append(x)
                    right_num= False    
                else:
                    print("Error!, Please enter number from 0 to 8 ")
            
#-----------------------------------------------------------------------------------------------------------------------------------------
#conditions at which player one wins
        if((board[0][1]==" X " and board[1][1]==" X " and board[2][1]==" X ")or\
           (board[3][1]==" X " and board[4][1]==" X " and board[5][1]==" X ")or\
           (board[6][1]==" X " and board[7][1]==" X " and board[8][1]==" X ")or\
           (board[0][1]==" X " and board[3][1]==" X " and board[6][1]==" X ")or\
           (board[1][1]==" X " and board[4][1]==" X " and board[7][1]==" X ")or\
           (board[2][1]==" X " and board[5][1]==" X " and board[8][1]==" X ")or\
           (board[0][1]==" X " and board[4][1]==" X " and board[8][1]==" X ")or\
           (board[2][1]==" X " and board[4][1]==" X " and board[6][1]==" X ")):
            print(P1_name+" is winner ")
            print("Congratulation "+ P1_name +" !")
            break
#-----------------------------------------------------------------------------------------------------------------------------------------  
#conditions at which player two wins
        elif((board[0][1]==" O " and board[1][1]==" O " and board[2][1]==" O ")or\
             (board[3][1]==" O " and board[4][1]==" O " and board[5][1]==" O ")or\
             (board[6][1]==" O " and board[7][1]==" O " and board[8][1]==" O ")or\
             (board[0][1]==" O " and board[3][1]==" O " and board[6][1]==" O ")or\
             (board[1][1]==" O " and board[4][1]==" O " and board[7][1]==" O ")or\
             (board[2][1]==" O " and board[5][1]==" O " and board[8][1]==" O ")or\
             (board[0][1]==" O " and board[4][1]==" O " and board[8][1]==" O ")or\
             (board[2][1]==" O " and board[4][1]==" O " and board[6][1]==" O ")):
            print(P2_name+" is winner ")
            print("Congratulation "+P2_name+" !")
            break
#------------------------------------------------------------------------------------------------------------------------------------------
#increment of game loop
        i=i+1
#-----------------------------------------------------------------------------------------------------------------------------------------
#conditions at which no one win,draw state
    if(i==9):
        print("The Game is Draw , All the Board is Full ")
        print ("Game Over")
#------------------------------------------------------------------------------------------------------------------------------------------
    print("if you want to play again please press r")
    new = input()
    if (new=="r"):
        playing=True
    else:
        exit()
     


 
    
