import re
import os 
import pygame 
from pygame import * 



pygame.init()
pygame.font.init()


def print1(value):
    for i in value:
        for j in i: 
            print( j , end = '\t')
        print()
def prints1(value):
    print("-"*100)
    for i in value:
        for j in i :
            if j == 0:
                print ( ' ' , end = '')
            elif j == '#':
                print ( '#' , end = '')
            elif j == -1:
                print ( '#' , end = '')
            else :
                print(".", end = '')
        print()
    print("-"*100)

def prints(value):
    print("-"*100)
    for i in value:
        for j in i :
            if j == 0:
                print ( ' ' , end = '')
            elif j == '#':
                print ( '#' , end = '')
            elif j == -1:
                print ( '*' , end = '')
            else :
                print(" ", end = '')
        print()
    print("-"*100)

# Create Values 


class pathFinder:


    def __init__(self,width,height,colors,board ):

        self.x = width         # Screen width
        self.y = height          # Screen height
        self.display = pygame.display.set_mode([  width,height  ]) # Root Display 
        self.gameRunning = True    # [True] = game is running , [False] games stops 
        self.color = colors         # Colors of the game
        self.board = gameBoard      # Main Board
        self.myfont = pygame.font.SysFont('Comic Sans MS', 20)  # Pygame Fonts

        self.pick = -1  # Barrier 
        self.target = [0,0]
        self.start = [0,0]
        
        self.prev= 0

        
    # Create Values 

    
        # -3 = path 
        # -2 = target 
        # -1 = barrier 
        # -0 = empty space 
        # 1  = player
        # else all target 
    
    def pathFinder(self,board , position,target):
        # Create value place
        player = 1
        # Change in board using value position 
        board[ position[0]  ][ position[1]   ] = player 


        # Count the distance between player and the target 
        
        stacks =[position]
        for val in stacks:
            # For out of bounce 
          
            # TOP MIDDLE 
            if val[0] > 0:
                if board[ val[0]-1  ][   val[1]   ] == 0 or board[ val[0]-1  ][   val[1]   ] == -2:
                    board[ val[0]-1 ][ val[1] ] =   board[ val[0]  ][   val[1]   ] + 1
                    stacks.append(  [ val[0]-1 ,    val[1]   ]   )

            # MIDDLE LEFT 
            if val[1] > 0 :
                if board[ val[0]  ][ val[1]-1  ] == 0 or  board[ val[0]  ][ val[1]-1  ] == -2 :
                    board[ val[0]  ][ val[1]-1  ] =  board[ val[0]  ][ val[1] ] +1
                    stacks.append( [ val[0], val[1]-1 ])

            # Middle Right 
            if val[1] < len(board[ val[0]  ])-1:
                if board[ val[0]  ][  val[1]+1 ] == 0 or board[ val[0]  ][  val[1]+1 ] == -2 :
                    board[ val[0] ][ val[1]+1 ] = board[val[0]][val[1]]+1 
                    stacks.append( [ val[0], val[1]+1  ]  )
            
                
            
            # Bottom center
            if val[0] < len(board)-1:
                if   board[ val[0]+1 ][ val[1] ] == 0 or board[ val[0]+1 ][ val[1] ] == -2:
                    board[ val[0]+1 ][ val[1] ] = board[ val[0] ][ val[1]  ]+1
                    stacks.append(  [ val[0]+1  , val[1] ] )
        
            #print(target, board[val[0]][val[1]] , val)
            if ( val[0] == target[0] and val[1] == target[1]):
                break 
            #prints1(board)
            
            #os.system('cls')
            
            

        # GET THE VALUE POSITION OF THE TARGET and put them to stack 
        #prints(board)
        #print()
        stacks = [ target]
        point =  board[ target[0] ][ target[1] ]
        board[ target[0] ][ target[1] ] = -3
        for val in stacks:
            
            if val[0] > 0:
                if board[ val[0]-1  ][   val[1]   ] != -3 and board[ val[0]-1  ][   val[1]   ] != -1:
                    if board[ val[0]-1  ][   val[1]   ] != 0 and board[ val[0]-1  ][   val[1]   ] < point :
                        board[ val[0]-1 ][ val[1] ] =   -3
                        stacks.append(  [ val[0]-1 ,    val[1]   ]   )
                        point -=1 
                        #board[ target[0] ][ target[1] ] = -2

            # MIDDLE LEFT 
            if val[1] > 0 :
                if board[ val[0]  ][ val[1]-1  ] != -3 and  board[ val[0]  ][ val[1]-1  ] != -1 :
                    if board[ val[0]  ][ val[1]-1  ] != 0 and board[ val[0]  ][ val[1]-1  ] < point:
                        board[ val[0]  ][ val[1]-1  ] =  -3 #board[ val[0]  ][ val[1] ] +1
                        stacks.append( [ val[0], val[1]-1 ])
                        point -=1 
                        #board[ target[0] ][ target[1] ] = -2

            # Middle Right 
            if val[1] < len(board[ val[0]  ])-1  :
                
                if board[ val[0]  ][  val[1]+1 ] != -3 and board[ val[0]  ][  val[1]+1 ] != -1 : 
                    if board[ val[0]  ][  val[1]+1 ] != 0 and  board[ val[0]  ][  val[1]+1 ] < point :
                        board[ val[0] ][ val[1]+1 ] = -3
                        stacks.append( [ val[0], val[1]+1  ]  )
                        point -=1 
                        #board[ target[0] ][ target[1] ] = -2

            # Bottom center
            if val[0] < len(board)-1:
                #prints(board)
                if board[ val[0]+1 ][ val[1] ] != -3 and board[ val[0]+1 ][ val[1] ] != -1 :
                    if  board[ val[0]+1 ][ val[1] ] != 0 and board[ val[0]+1 ][ val[1] ] < point:
                        board[ val[0]+1 ][ val[1] ] = -3
                        stacks.append(  [ val[0]+1  , val[1] ] )
                        point -=1 
                        #board[ target[0] ][ target[1] ] = -2
            board[ position[0] ][  position[1] ] = 1
            if (board[ val[0] ][ val[1] ] == 1 ):
                board[ target[0] ][ target[1] ] = -2
                board[ position[0] ][  position[1] ] = 1
                print(  target,val )
                break
        
        
            #prints(board)
            #os.system('cls')
        
    

    # This method is for qutting options
    def controls(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameRunning = False
            pos  = pygame.mouse.get_pos() # Get the position 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if pos[1]//35  == 17 and pos[0]//35 == 10:
                        self.pick = 1 
                        for i in (self.board):
                            print(i)
                    if pos[1]//35  == 17 and pos[0]//35 == 14:
                        self.pick = -1 
                    if pos[1]//35  == 17 and pos[0]//35 == 18:
                        self.pick = -2 
                    if pos[1]//35  == 17 and pos[0]//35 == 26:
                        self.pick = 0 
                    # RESET 
                    if pos[1]//35  == 17 and  pos[0]//35 == 22:
                        for i in range(len(self.board)):
                            for j in range(len(self.board[i])): 
                                self.board[i][j] = 0
                                self.target = [0,0]
                                self.start = [0,0]

            # START
            if pygame.mouse.get_pressed()[0] and self.pick == 1:
                try:
                    
                    for i in range(len(self.board)):
                        for j in range(len(self.board[i])):
                            if self.board[i][j] == 1 and (j != pos[1]//35 or i != pos[0]//35):
                                self.board[i][j] = self.prev
                            if self.board[i][j] >= 2 or self.board[i][j] == -3:
                                self.board[i][j]  =0
                    self.prev =  self.board[   pos[1]//35  ][ pos[0]//35 ]
                    self.board[   pos[1]//35  ][ pos[0]//35 ]=1
                    self.start = [pos[1]//35  ,pos[0]//35  ]

                    
               
                except:
                    pass


            # TARGET 
            if pygame.mouse.get_pressed()[0] and self.pick == -2:
                try:
                    for i in range(len(self.board)):
                        for j in range(len(self.board[i])):
                            if self.board[i][j] == -2 and (j != pos[1]//35 or i != pos[0]//35):
                                self.board[i][j] = self.prev
                            if self.board[i][j] >= 2 or  self.board[i][j] == -3 :
                                self.board[i][j]  =0
                    self.prev =  self.board[   pos[1]//35  ][ pos[0]//35 ]
                    self.board[   pos[1]//35  ][ pos[0]//35 ] =   -2
                    self.target = [pos[1]//35  ,pos[0]//35  ]
                    self.pathFinder(self.board,self.start,self.target)

                except:
                    pass

            # ERASER
            if pygame.mouse.get_pressed()[0] and self.pick == -1:
                try: 
                    self.board [  pos[1]//35 ] [  pos[0]//35 ] = self.pick 
                except:
                    pass
            if pygame.mouse.get_pressed()[0] and self.pick == 0:
                try: 
                    if self.board [ pos[1]//35 ][pos[0]//35] <=1 :
                        self.board [  pos[1]//35 ] [  pos[0]//35 ]   = self.pick 
                except:
                    pass
                        
    def text(self,message , color , position ): 
        self.textsurface = self.myfont.render(message, False, color)
        self.display.blit( self.textsurface, position )
    # Updates the game display

    
    def displayUp(self):
        self.display.fill(  self.color['background1'] )
        #self.pathFinder( self.board ,  self.start  , self.target )
        #print(self.start,self.target)
        
        self.gameDisplay()

        self.changeCustom()
        pygame.display.update() # Updates the screem



    def changeCustom(self): 

        gap = 5 
        size = 30 
        

        self.text("Player" , self.color['Color5'] , [size*10+gap*10 + 35  ,size*17+gap*17] ) 
        self.drawRect(self.color['Color5'] ,[ size*10+gap*10 ,  size*17+gap*17,size, size ])
        # Change the pick 
        
        
        self.text("Barrier" , self.color['Color2'] , [size*14+gap*14 + 35  ,size*17+gap*17] ) 
        self.drawRect(self.color['Color2'] ,[ size*14+gap*14 ,  size*17+gap*17,size, size ])

        self.text("Target" , self.color['Color3'] , [size*18+gap*18 + 36  ,size*17+gap*17] ) 
        self.drawRect(self.color['Color3'] ,[ size*18+gap*18 ,  size*17+gap*17,size, size ])

        self.text("Reset" , self.color['Color4'] , [size*22+gap*22 + 36  ,size*17+gap*17] ) 
        self.drawRect(self.color['Color4'] ,[ size*22+gap*22 ,  size*17+gap*17,size, size ])

        self.text("Eraser" , self.color['Color1'] , [size*26+gap*26 + 36  ,size*17+gap*17] ) 
        self.drawRect(self.color['Color1'] ,[ size*26+gap*26 ,  size*17+gap*17,size, size ])

    def gameDisplay(self):
        gap = 5 
        size = 30 
        self.display.fill(  self.color['background1'] )
        for row in range(len(self.board)):                  
            for col in  range(len(self.board[row-1])):
                if self.board[row][col] == 0:    # Empty Slot
                    self.drawRect(self.color['background2'] ,[ size*col+gap*col ,  size*row+gap*row  ,size, size ])
                if self.board[row][col] == -1:  # Barrier
                    self.drawRect(self.color['Color2'] ,[ size*col+gap*col ,  size*row+gap*row  ,size, size ])
                if  self.board[row][col] >1 :
                    self.drawRect(self.color['Color1'] ,[ size*col+gap*col ,  size*row+gap*row  ,size, size ])
                if self.board[row][col] == -3:  # Barrier
                    self.drawRect(self.color['Color4'] ,[ size*col+gap*col ,  size*row+gap*row  ,size, size ])
        for row in range(len(self.board)):                  
            for col in  range(len(self.board[row])):
                if self.board[row][col] == 1: # Player 
                    self.text("Player" , self.color['Color5'] , [size*col+gap*col + 35  ,size*row+gap*row] ) 
                    self.drawRect(self.color['Color5'] ,[ size*col+gap*col ,  size*row+gap*row  ,size, size ])

                if self.board[row][col] == -2: # Player 
                    self.text("Target" , self.color['Color3'] , [size*col+gap*col + 35  ,size*row+gap*row] ) 
                    self.drawRect(self.color['Color3'] ,[ size*col+gap*col ,  size*row+gap*row  ,size, size ])

    def drawRect (self, color , position ):
        # Root display , [Color] [x ,y , width , height]
        pygame.draw.rect( self.display , color, position)
    # Main Method
    def main(self,*args,**kwargs):
        while self.gameRunning: 
            self.controls()
            self.displayUp()
            
                    
        
if __name__ == '__main__':
    
    width = 1295 
    height = 675
    colors = {
        'background1': [21, 32, 43],   
        'background2': [25, 39, 52],
        'Color1':      [0, 0, 0],
        'Color2' :     [29, 161, 242],
        'Color3' :     [224, 36, 94],
        'Color4' :     [255, 173, 31],
        'Color5':      [255,255, 255],
        'Color6':      [23, 191, 99]
        

    }
    gameBoard = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    path = pathFinder(width,height , colors , gameBoard)
    path.main() 

