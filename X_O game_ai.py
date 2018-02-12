from random import randint
from time import sleep
from copy import deepcopy
#------------------------------------
#player round name
print("Please enter your name: ")
P1_name=str(input())
def main():
    #main function that operate game
    global board
    board = [[0, " 0 "], [1, " 1 "], [2," 2 "], [3," 3 "], [4," 4 "], [5," 5 "], [6," 6 "], [7," 7 "], [8," 8 "]]
    global counter
    counter =0
    draw_board()
    #call that function to draw board of game
def draw_board():
    # function to draw game board
    print(board[0][1] + "|"+ board[1][1] +"|" + board[2][1] + "\n---+---+--- \n" + board[3][1] +"|" + board[4][1] + "|"+ board[5][1] + "\n---+---+--- \n" + board[6][1] + "|" + board[7][1] + "|" +  board[8][1] + "\n")
    next_turn(counter)
def next_turn(count):
    if(count%2==0):
        global counter
        counter+=1
        player_turn()
        #increment counter +1 in order to to make game continue in looped game turns if count is even ----> player_turn , if it is odd ----> computer_turn 
    else:
        counter+=1
        computer_turn()
def player_turn():
# make try except continue to ignore error and make user input number and if it is right continue else go back in loop and ask user to input another one
    try:
        space_in_board= int(input("It's your turn! Please select an empty space on the board by typing a number 1-9\n"))
    except ValueError:
        player_turn()
    #empty space
    if((board[space_in_board][1]!=" X ") and (board[space_in_board][1]!=" O ")):
        board[space_in_board][1]=" X "
        if((check_winner(board," X ")==True)):
            print("You have won ! ")
            end_of_game()
        check_tie(board)
        draw_board()
    else:
        player_turn()
def computer_turn():
    print("It's computer turn")
    sleep(1.5)
    print("Wait!,Let me think..,Please.....")
    sleep(1.5)
    # sleep for reality in game
    for space_in_board in range(0,3):
        board_copy=deepcopy(board)
        if(board_copy[space_in_board][1] != " X ") and (board_copy[space_in_board][1] != " O "):
            board_copy[space_in_board][1] = " O "
            if(check_winner(board_copy, " O ")):
                board[space_in_board][1] = " O "
                print("You have lost to the bot! \n")
                end_of_game()
                draw_board()
                return
#-------------------------------------------------------------
    for space_in_board in range(0,9):
        board_copy = deepcopy(board)
        if board_copy[space_in_board][1] != " X " and board_copy[space_in_board][1] != " O ":
            board_copy[space_in_board][1] = " X "
            if check_winner(board_copy, " X "):
                board[space_in_board][1] = " O "
                draw_board()
                return
    randomMove = True
    while(randomMove):
        space_in_board=randint(0,8)
        if (board[space_in_board][1] != " X " and board[space_in_board][1] != " O "):
            board[space_in_board][1] = " O "
            randomMove = False
            draw_board()
def check_winner(brd, lttr):
    return ((brd[6][1] == lttr and brd[7][1] == lttr and brd[8][1] == lttr) or\
            (brd[3][1] == lttr and brd[4][1] == lttr and brd[5][1] == lttr) or\
            (brd[0][1] == lttr and brd[1][1] == lttr and brd[2][1] == lttr) or\
            (brd[6][1] == lttr and brd[3][1] == lttr and brd[0][1] == lttr) or \
            (brd[7][1] == lttr and brd[4][1] == lttr and brd[1][1] == lttr) or \
            (brd[8][1] == lttr and brd[5][1] == lttr and brd[2][1] == lttr) or \
            (brd[6][1] == lttr and brd[4][1] == lttr and brd[2][1] == lttr) or \
            (brd[8][1] == lttr and brd[4][1] == lttr and brd[0][1] == lttr))
def check_tie(brd):
    emptySpaces = 0
    for x in brd:
        if x[1] != " O " and x[1] != " X ":
            emptySpaces += 1
    if emptySpaces == 0:
        print("The board is full!  You have tied! \n")
        end_of_game()
def end_of_game():
    response =str(input("Would you like to play again? Y/N \n"))
    if ((response == "Y") or (response == "y")):
        print("Starting new game...")
        sleep(6)
        main()
    elif ((response == "N") or (response == "n")):
        print("Thanks for playing!")
        sleep(6)
        quit()
    else:
        print("You did not input a valid response!")   

if (__name__ == "__main__"):
    main()


          

          
          
        

    
