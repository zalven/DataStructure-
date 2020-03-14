import re
import os 

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
def pathFinder(board , position,target):
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
    




values=[[0, 0, 0, 0, 0, 0, 0, 0, -1, 0],
        [0, -1, 0, 0, 0, 0, 0, 0, 0, -1],
        [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, -1, -1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, -1, 0, 0, 0],
        [0, 0, 0, 0, -1, -1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
        [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, -1, 0, 0, 0, 0, 0, -1, 0, 0]]






a = ''.join([
".WW...W.....W........W.WWW.......W....W..W....W\n",
"...W..W.....WWWW...WW...WW.W.W..WW...WW.WWWW...\n",
"W.............W...W.WWW.....W.......W......W.WW\n",
"..W.WW.W...W.W.W..........W..WWW...W.WWW....WW.\n",
".......WWWW......WW..W.........W....W......WWWW\n",
".WWW..W....W.........W...WWW..W...W....W......W\n",
".W...W.W...W...WW..W.WWWW..WWWWW......W.WW....W\n",
"WWW.WWWW.....W..WWW.......W..WW.....WW.WW.....W\n",
".W.WW.WWW...W......WWWW...WW.W....W..WWWW......\n",
".....WW.......W...WW...WW.....W...WW.WWW.W.....\n",
".W..W...........WWW.W..WW............WW.WW..W.W\n",
"..WWWW...WW....W.WW.WW........WWW.W..W.......W.\n",
".W......WW..WWWWW..W.W.W..W.......W...WW....WW.\n",
".WWW.WWW..........W..WW.........WWW.WW....WWW.W\n",
"........WWW....W....W...W.W....W.W...WWW.......\n",
".W...WW.W......WWW.W.W..W..W.W.WW..W.WW.W...W..\n",
"W..W.WW...W..W...W....W.....W...W....W....W.W..\n",
".......WW..W....W.....WW.....W.WW...WW.WWWWWW.W\n",
"W.W...WW.W.W..WW..W....W.W........W....W..W.W.W\n",
"..W...W.........W..W....WWW...W.....W..........\n",
"..W.WW......W..W..W..WW..W..WWW.......W.......W\n",
"...W.W....W...W.W..WW.W......W...W.............\n",
"..........W..WWWW.W....W.W.W...WW...W.W........\n",
"...W.W....W..W..W.WW....WWW............W.WW....\n",
"W...W.W...W.....W..W..W.W..WW.W...W.....WW.W..W\n",
".W...W....WWW.......W....W.....WWWW.WW..W...WW.\n",
".W.WW..W.WWW.W.WW.W.WW....W....W.W.WWWW..WW....\n",
".W....W.W.W...W...WW....W..W..WWW...W.....W.W..\n",
"..W...W.WW..W..........W..W.W.W.WW.W.W.....W.W.\n",
"..WW..W.W...W..WW..W......W.W..W...WW..........\n",
".W....WW..WW....W..WW..WW.WW.W...W..W.W...W.W..\n",
"...W.WW.....W..W....W....W..W...WWWW....W.....W\n",
"W...W.W.....WWW.W.WW....WWW..W......WWW....W..W\n",
"W.W.WW...W.W.W..W...W..WW...WWW..WW.WW...W....W\n",
"WW....WW.WW....W..WW....W..W.W.W..W....W......W\n",
".W.WWW.WWWWW...W.W........WW.....W..WW...W...W.\n",
"W.W.....WW.W.W.W....WW.............W..W........\n",
"W....W.WWW.W.WW.W..WW.WWW.W...W......W.W.......\n",
"W.......WW.W.W...W....WWW.WW.W.....WW.W....W.WW\n",
".W....WWW..WW.W...W..W.W..W.WWW.W.......W..W...\n",
"...W..WWWWW..W......WW.W..W.W.WW.W........WW...\n",
"....WWWW.....W.W..W.W.....W...WW..W..W.....WW..\n",
"W.WW.W.......WW..W..W.W..WW..W.W..........W....\n",
"W...WW.W..W..WW....WW.WWW.WWW....W.......WW...W\n",
"W...........W........WW........W.W...........WW\n",
"....WWWW.....W.WW.WW...W....WW....W............\n",
"..W.WWW...WW.W.W.WWWW..W.W..W.W..W.W........WW."])

x = a.replace('W',',-1,').replace(".",',0,').replace(",,",",").split("\n")
for j,i in enumerate(x):
    x[j] = ([int(i) for i in i.split(",") if i != ''])

position = [5,5]
target = [46,46]
pathFinder(x,position,target)