import pygame
from pygame.locals import *
#gaming library for displaying it
XO="X"
grid=[ [None,None,None],\
       [None,None,None],\
       [None,None,None] ]
#grid :to be able to draw lines on board 
winner= None
def table (x):
    background=pygame.Surface(x.get_size())#to get dimensions of surface 
    background=background.convert()
    #convert function to change pixels format on board
    background.fill((250, 250, 250))# to fill surface with solid colour
    pygame.draw.line(background, (0,0,0), (100,0), (100,300), 2)#vertical line 1
    pygame.draw.line(background, (0,0,0), (200,0), (200,300), 2)#vertical line 2
    pygame.draw.line(background, (0,0,0), (0,200), (300,200), 2)# horizonital line 1
    pygame.draw.line(background, (0,0,0), (0,100), (300,100), 2)#horizontal line 2
    return background

def result_is_draw (board): #this function used for draw status 
    global XO , winner # calling them from up lines with same values
    if(winner is None):
        message= XO +"'s turn" #if it is draw
    else:
        message= winner + "won!"
    font=pygame.font.Font(None, 24)#determine font of writing on screen by creating new font object from a file  
    text=font.render(message, 1, (10, 10, 10))#draw text on new surface
    board.fill ((250, 250, 250), (0, 300, 300, 25)) #fill with solid colour
    board.blit(text, (10, 300))#to draw one image on another one
     
#----------------------------------------------------------------------
def scr_brd (x, board):           
    result_is_draw (board)
    x.blit(board, (0 , 0))#to draw on screen
    pygame.display.flip()#flip horizontially and vertically
    
#---------------------------------------------------------------------
def board_position (mouseX, mouseY):#to determine the x-o board position on general screen after convert and fill it with new size
               #mouseY ------> y coordinate the user clicked
               #mouseX-------> x coordinate the user clicked
    if(mouseY<100):
        row=0                       #determine row that user clicked 
    elif(mouseY<200):
        row=1
    else:
        row=2
        #--------------------------------------------------------------#
    if(mouseX<100):
        col=0                #determine column that user clicked 
    elif(mouseX<200):
        col=1
    else:
        col=2
    return(row,col)            #return col and row the user clicked
def draw_move (board, boardrow, boardcol, piece):
               #piece------>x or o
               #boardrow and boardcol------>row & col in which to draw th piece
  #table is in shape of square so we want to get it's center
    global centerX , centerY
    centerX=((boardcol)*100)+50
    centerY=((boardrow)*100)+50
               #as parameters on x-axis and y-axis(from 0 to 300)
               
    if(piece== "O"):
        pygame.draw.circle(board, (0,0,0), (centerX,centerY), 34, 2)
    else:
        pygame.draw.line(board, (0,0,0), (centerX-17,centerY-17), (centerX+17,centerY+17), 2)
        pygame.draw.line(board, (0,0,0), (centerX+17,centerY-17), (centerX-17,centerY+17), 2)
               #this condition statment and function used to draw either lines(x)or circles (o)
               #with fixed center of square and draw on board represented on screen
    grid[boardrow][boardcol]=piece #mark for space as used
def click_board (board):
    global grid, XO
    (mouseX, mouseY)=pygame.mouse.get_pos()
    (row, col)=board_position (mouseX, mouseY)
    if((grid[row][col]=="X")or(grid[row][col]=="O")):
        return
                  #make sure there is no one's play on this space
#--------------------------------------------------------------------------
    draw_move(board, row, col, XO)
#--------------------------------------------------------------------------
    if(XO=="X"):
        XO="O"
    else:
        XO="X"

def game_won (board):#to determine if anyone won the game 
    global grid, winner
               #condition for row to see if he win
    for row in range (0, 3):#note:grid[row place][col place]
        if((grid[row][0]== grid[row][1]== grid[row][2]) and (grid[row][0] is not None)):
               #this row of (X player) or (O player) ----------> won
            winner=grid[row][0]
            pygame.draw.line(board, (250,0,0), (0,(row+1)*100-50), (300,(row+1)*100-50), 2)
            break
            
               #------------------------------------------------------------------
    for col in range(0, 3):
        
        if((grid[0][col]== grid[1][col]== grid[2][col]) and (grid[0][col])is not None):
           winner=grid[0][col]
           pygame.draw.line(board, (250,0,0), ((col+1)*100-50,0), ((col+1)*100-50,300), 2)
                #this col of(X player) or(O player)----------> won
           break
           
            #--------------------------------------------------------------------
                #now we check the horizontial rows and vertical col, the missing pro. is the diagonal one
        if((grid[0][0]==grid[1][1]==grid[2][2])and(grid[0][0] is not None)):
           winner=grid[0][0]
           pygame.draw.line(board, (250,0,0), (50,50), (250,250), 2)
           break
                      #diagonal from left to right won
            #----------------------------------------------------------------------
        if((grid[0][2]==grid[1][1]==grid[2][0])and(grid[0][2]is not None)):
           winner=grid[0][2]
           pygame.draw.line(board,(250,0,0), (250,50), (50,250), 2)
           break
                      #diagonal from right to left won
                      #notes:
                      #draw.line :used to draw line over complete winning part either col or row or even diagonl
                      #draw.circle:used to draw circle which is (O) which controlled size coder determine it in coding time 


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
                      
                      
pygame.init()#that used to iniyialize pygame library and window
x=pygame.display.set_mode((300, 350))
pygame.display.set_caption("X-O Game")#naming game in bar with font size
board=table(x) #creating game board
#now we should do aloop that is main one to determine at what moment the game stop and controll the function .
running=1
while(running==1):
    for event in pygame.event.get():#.event.get():to get events from the queue
        if((event.type)is QUIT):
            running=0
        elif((event.type)is MOUSEBUTTONDOWN):#so we should call all the function in order to continue game and return to main loop to detect if one of two player won or no
            #user click on place X or O
            click_board(board)
            #check for winner from function
        game_won(board)
            #update display
        scr_brd(x, board)
                      
                      
                      
                      
                      
               
               
               
               


               
               
        



    

