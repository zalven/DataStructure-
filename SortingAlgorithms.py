import pygame 
from pygame import *
import random
import numpy as np
import time, sys
from pygame import mixer

pygame.init()
mixer.init()

class SortingVisualization:
    def __init__(self,sizeX,sizeY,colors,values , eratosthenes):

        self.values = values       #Graph values (Random Range)
        self.eratosthenes  = eratosthenes
        self.popSound = pygame.mixer.Sound("pop.wav")
        self.clock = pygame.time.Clock()  #Frames per second 
        self.screen = pygame.display.set_mode([sizeX,sizeY]) # Screen display
        self.x = sizeX         # Width of the window
        self.y = sizeY         # Length of the window
        self.gameRunning = True    # Main game loop
        self.color = colors        # Colors of the game [Background , graph ...etc]
        # Create Values 
    def pathFinder(self,board , position,target):
        # Create value place
        player = 1
        # Change in board using value position 
        board[ position[0]  ][ position[1]   ] = player 


        # Count the distance between player and the target 
        
        stacks =[position]
        for val in stacks:
            # For out of bounce 
            if ( val[0] == target[0] and val[1] == target[1]):
                break 
            '''
            # The use of A* algorithm 
            # TOP LEFT 
            if val[0] > 0 and val[1] > 0:
                if board[  val[0]-1  ] [ val[1]-1  ] == 0 and (board[ val[0]  ][ val[1]-1  ] == 0 and board[ val[0]-1  ][   val[1]   ] == 0):
                    board[  val[0]-1  ] [ val[1]-1  ] +=  board[  val[0] ] [ val[1]  ] +1 
                    stacks.append(   [val[0]-1 , val[1]-1]    )
            # TOP RIGHT 
            if val[0] > 0 and val[1] < len( board[ val[0]  ] )-1:
                if board[ val[0]-1  ][   val[1]+1   ] == 0 and( board[ val[0]  ][  val[1]+1 ] == 0 or board[ val[0]-1  ][   val[1]   ] == 0):
                    board[  val[0]-1   ][ val[1]+1 ] +=  board[ val[0]  ][ val[1]  ]+1 
                    stacks.append([  val[0]-1,val[1]+1 ])
            # Bottom Right 
            if val[0] < len(board)-1 and val[1] < len(board[ val[0] ]) -1:
                if board[ val[0]+1 ][ val[1] + 1  ] == 0 and  (board[ val[0]  ][  val[1]+1 ] == 0  or board[ val[0]+1 ][ val[1] ] == 0 ):
                    board[ val[0]+1  ][ val[1]+ 1 ] += board[ val[0] ][ val[1] ]+1
                    stacks.append( [ val[0]+1,val[1]+1 ] )
            if val[0] < len(board)-1 and val[1] > 0:
                if board[  val[0]+1 ][ val[1]-1  ] == 0 and ( board[ val[0]  ][ val[1]-1  ] == 0 or  board[ val[0]+1 ][ val[1] ] == 0):
                    board[ val[0]+1  ][ val[1]-1 ] += board[val[0]][val[1]]+1
                    stacks.append( [ val[0]+1 , val[1]-1 ] )
            '''
            
            # TOP MIDDLE 
            if val[0] > 0:
                if board[ val[0]-1  ][   val[1]   ] == 0 :
                    
                    board[ val[0]-1 ][ val[1] ] =   board[ val[0]  ][   val[1]   ] + 1
                    if target[0] >= val[0]-1 and val[0]-1 <= target[0]:
                        stacks.append(  [ val[0]-1 ,    val[1]   ]   )

            # MIDDLE LEFT 
            if val[1] > 0 :
                if board[ val[0]  ][ val[1]-1  ] == 0:
                    board[ val[0]  ][ val[1]-1  ] =  board[ val[0]  ][ val[1] ] +1
                    stacks.append( [ val[0], val[1]-1 ])

            # Middle Right 
            if val[1] < len(board[ val[0]  ])-1:
                if board[ val[0]  ][  val[1]+1 ] == 0:
                    board[ val[0] ][ val[1]+1 ] = board[val[0]][val[1]]+1 
                    stacks.append( [ val[0], val[1]+1  ]  )
            
                
            
            # Bottom center
            if val[0] < len(board)-1:
                if   board[ val[0]+1 ][ val[1] ] == 0:
                    board[ val[0]+1 ][ val[1] ] = board[ val[0] ][ val[1]  ]+1
                    stacks.append(  [ val[0]+1  , val[1] ] )
        

            if ( val[0] == target[0] and val[1] == target[1]):
                break 
            prints1(board)
            os.system('cls')
            

        # GET THE VALUE POSITION OF THE TARGET and put them to stack 
        prints(board)
        print()
        stacks = [ target]
        point =  board[ target[0] ][ target[1] ]
        board[ target[0] ][ target[1] ] = '#'
        for val in stacks:

            if val[0] > 0:
                if board[ val[0]-1  ][   val[1]   ] != '#' and board[ val[0]-1  ][   val[1]   ] != -1:
                    if board[ val[0]-1  ][   val[1]   ] != 0 and board[ val[0]-1  ][   val[1]   ] < point :
                        board[ val[0]-1 ][ val[1] ] =   '#'
                        stacks.append(  [ val[0]-1 ,    val[1]   ]   )
                        point -=1 

            # MIDDLE LEFT 
            if val[1] > 0 :
                if board[ val[0]  ][ val[1]-1  ] !='#' and  board[ val[0]  ][ val[1]-1  ] != -1 :
                    if board[ val[0]  ][ val[1]-1  ] != 0 and board[ val[0]  ][ val[1]-1  ] < point:
                        board[ val[0]  ][ val[1]-1  ] =  '#' #board[ val[0]  ][ val[1] ] +1
                        stacks.append( [ val[0], val[1]-1 ])
                        point -=1 

            # Middle Right 
            if val[1] < len(board[ val[0]  ])-1  :
                
                if board[ val[0]  ][  val[1]+1 ] != '#' and board[ val[0]  ][  val[1]+1 ] != -1 : 
                    if board[ val[0]  ][  val[1]+1 ] != 0 and  board[ val[0]  ][  val[1]+1 ] < point :
                        board[ val[0] ][ val[1]+1 ] = '#'
                        stacks.append( [ val[0], val[1]+1  ]  )
                        point -=1 
            
                
            
            # Bottom center
            if val[0] < len(board)-1:
                #prints(board)
                if board[ val[0]+1 ][ val[1] ] != '#' and board[ val[0]+1 ][ val[1] ] != -1 :
                    if  board[ val[0]+1 ][ val[1] ] != 0 and board[ val[0]+1 ][ val[1] ] < point:
                        board[ val[0]+1 ][ val[1] ] = '#'
                        stacks.append(  [ val[0]+1  , val[1] ] )
                        point -=1 
            if (board[ val[0] ][ val[1] ] == 1 ):
                break
        
        
            prints(board)
            os.system('cls')
        
    # Method to quit the game 
    def pygameQuit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                pygame.quit()
                self.gameRunning = False 

    def display(self):
        self.screen.fill(self.color['background'])
    
        self.randomizer(0,100)
        self.quickSort(self.values)
        self.randomizer(0,100)
        self. insertionSort(self.values)
        self.randomizer(0,100)
        self. bubbleSort(self.values)
        self.randomizer(0,100)
        self.selectionSort()
    
        pygame.display.update()
    def sieve(self):
        n = self.eratosthenes # Value 
        width = 600 # Area of the Square
        area = width*width
        numberOfsqrs = n*n
        sqrs = area // numberOfsqrs
        start  = self.x//2 - width  //2
        self.drawRect(self.color['background2'] ,[start ,50,width  ,width  ] )
        for i in range(self.eratosthenes):
            for j in range(self.eratosthenes):
                
                # Divide it into segments 
                self.drawRect(self.color['graphLine'] ,[start+10*(1+j)+10 ,10*(1+i) , sqrs,sqrs ] )
                #print(area/n)
        self.sieveOfEratosthenes(self.eratosthenes)
        #self.drawRect(self.color['background2'] ,[100,100,100,100])

        



    def randomizer(self,start,end):
        for i in range(50):
            self.popSound.play()
            self.values = self.valueRandomizer(start,end+1)
            num1 = random.randrange(start,end+1)
            num2 = random.randrange(start,end+1)
            num3 = random.randrange(start,end+1)
            self.graphPrint(self.values,num1,num2 ,num3)
            pygame.display.update()
            self.pygameQuit()
           
    def drawRect(self,color,pos):
        #   Colors , [position-x , position-y , width-x , length-y]
        pygame.draw.rect( self.screen,color ,pos)


    def graphPrint(self,values,pick1,pick2,pick3):
        pygame.display.update()
        self.screen.fill(self.color['background'])
        
        gap = 12# Gaps between the lines
        for data,value in enumerate( values) : 
            if(pick3 == value):  # Color for change values 
                self.drawRect(self.color['graphColorChange2'],[(gap*data)+50,self.y-value*3-50,10,value*3])
            if(pick1 == value):  # Color for change values 
                self.drawRect(self.color['graphColorChange'],[(gap*data)+50,self.y-value*3-50,10,value*3])
            if(pick2 == value): # Color for change values2  
                self.drawRect(self.color['graphColor'],[(gap*data)+50,self.y-value*3-50,10,value*3])
            if(value != pick1 and value != pick2 and value != pick3) : # Color Of the graph 
                 self.drawRect(self.color['graphLine'],[(gap*data)+50,self.y-value*3-50,10,value*3])
        pygame.display.update()
       
    def quickSort(self,value):
        return self._quickSort(value,0,len(value)-1)
    def _quickSort(self,value,low,high):
        if low < high: 
            pivot = self.partition(value , low , high )
            self._quickSort(value,pivot+1,high)
            self._quickSort(value,low,pivot-1)
            self.graphPrint(value,value[low] ,value[high] ,pivot)
            self.pygameQuit()
        self.pygameQuit()
        
    def partition(self,value,low,high):
        pivot = value[high]
        left = low-1 
        for count in range(low,high):
            if value[count] < pivot:
                left +=1 
                value[count], value[left]  = value[left] , value[count] 
            self.graphPrint(value,value[count] ,value[left] ,pivot)
            self.pygameQuit()

        value[left+1] , value[high] = value[high] , value[left+1]
        self.graphPrint(value,value[left+1] ,value[high] ,pivot )
        self.pygameQuit()
        return left+1

    # Random Numbers That ranges[start] and [end] 
    def valueRandomizer(self,start,end):
        store = []
        count = 0
        while len(store ) <= 100 :
            
            radnomNum = random.randrange(start,end+1)
            if radnomNum not in store: 
                store  += [radnomNum]
                count +=1 
        return store 

    # Algorithm O(N^2)
    def bubbleSort(self,values):
        for i in range(len(values),-1,-1):
            for j in range(i-1):
                if values[j] > values[j+1]: 
                   values[j],values[j+1] = values[j+1],values[j]
                #self.popSound.play() # PLay pop sound
                self.graphPrint(values,values[j+1] ,values[j]  ,values[i-1] )
                self.pygameQuit()
              
                
    def insertionSort(self,values):
        for i in range(1,len(values)):
            j = i-1
            while j >=0 and  values[j] > values[j+1]:
                values[j],values[j+1] = values[j+1] ,values[j]
                j -=1
                self.graphPrint(values,values[j+1] ,values[i],-1)
                self.pygameQuit()

            self.graphPrint(values,values[j+1] ,values[i] ,-1 )
            self.pygameQuit()

    def selectionSort(self,values):
        for i in range(len(values)):
            minIndex = i 
            for j in range(i,len(values)):
                if values[minIndex] > values[j]:
                    minIndex = j 
                self.graphPrint(values,values[minIndex],values[j] ,values[i]  )
                self.pygameQuit()

            values[i], values[minIndex]= values[minIndex],values[i] 
            self.graphPrint(values,values[i] ,values[minIndex],values[i]  )
            self.pygameQuit()
            
          
    def main(self,*args,**kwargs):
        while self.gameRunning == True:
           
            self.pygameQuit()
            self.display()

if __name__ == '__main__':
    # Main Color for the game 
    colors = {
        'background':            [21, 32, 43],   
        'background2' :           [25, 39, 52],
        'graphLine':              [255, 255, 255],
        'graphColor' :            [29, 161, 242],
        'graphColorChange' :      [224, 36, 94],
        'graphColorChange2' :     [255, 173, 31],

    }
    width = 1300    # Width of the screen 
    height = 700    # Height of the screen
    values =  [1, 35, 88, 37, 26, 43, 101, 75, 70, 3, 67, 56, 97, 79, 98, 53, 69, 31, 39, 13, 81, 20, 30, 59, 27, 58, 12, 63, 92, 47, 42, 16, 62, 51, 60, 28, 6, 89, 7, 74, 93, 73, 32, 99, 4, 17, 2, 45, 71, 55, 77, 10, 18, 22, 36, 86, 38, 65, 24, 11, 85, 64, 68, 41, 14, 82, 34, 96, 19, 21, 49, 40, 29, 76, 90, 84, 50, 9, 80, 78, 94, 57, 52, 100, 54, 72, 66, 44, 46, 61, 91, 33, 83, 5, 8, 23, 48, 0, 15, 87]

    
    sorting = SortingVisualization(width,height,colors,values , 100) 
    sorting.main()
    
                


        

        
