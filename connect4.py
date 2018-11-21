'''I pledge my honor that I have abided by the Stevens Honor System'''
class Board(object):
    def __init__(self, width=7, height=6):
        '''instantiates the board'''
    
        self.__width= width
        self.__height= height
        self.__board=[[' 'for _ in range(width)] for _ in range(height)]
        
    def __str__(self):
        '''prints out the board'''
    
        boardsym=''
        for row in range(self.__height):
            boardsym+='|'
            for col in range(self.__width):
                boardsym+=self.__board[row][col]+ '|'
            boardsym+='\n'
        boardsym+='-' * (((self.__width)*2)+1)+ '\n' + " "
        for row in range(self.__width):
            return boardsym
        
    def allowsMove(self,col):
        '''allows the move of the place'''
    
        cols=range(self.__width)
        if col not in cols:
            return False
        collo=False
        for row in range(self.__height):
            if self.__board[row][col]==' ':
                collo=True
        return collo
        
    def addMove(self,col,ox):
        '''adds the move to the other space'''
    
        row=self.__height-1
        while self.__board[row][col] != ' ':
            row-=1
        self.__board[row][col]=ox
        
    def setBoard(self,moveString):
    
        letr='O'
        for colet in moveString:
            col=int(colet)
            if 0<=col<=self.__width:
                self.addMove(col,letr)
            if letr=='O':
                letr='X'
            else:
                letr='O'
                
    def delMove(self,col):
    
        row=0
        while row in range(self.__height) and self.__board[row][col]==' ':
            row+=1
        if row !=6:
            self.__board[row][col]=' '
            
    def winsFor(self,ox): 
        '''checks for wins'''
    
        def winsDiaglr(ox,row,col):
        
            def lr(ox,row,col):
            
                if row ==self.__height or col==self.__width:
                    return 0
                if self.__board[row][col] != ox:
                    return 0
                return 1 + lr(ox,row+1,col+1)
            def ul(ox,row,col):
           
                if row < 0 or col  < 0:
                    return 0
                if self.__board[row][col] != ox:
                    return 0
                return 1 + lr(ox,row-1,col-1)
            return lr(ox,row,col)+ul(ox,row,col)-1
        def winsDiagll(ox,row,col):
        
            def ur(ox,row,col):
            
                if row<0 or col==self.__width:
                    return 0
                if self.__board[row][col] != ox:
                    return 0
                return 1 + ur(ox,row-1,col+1)
            def ll(ox,row,col):
           
                if col<0 or row==self.__height:
                    return 0
                if self.__board[row][col] != ox:
                    return 0
                return 1 + ll(ox,row+1,col-1)
            return ur(ox,row,col)+ll(ox,row,col)-1
        def winsVer(ox,row,col):
       
            def up(ox,row,col):
           
                if row<0:
                    return 0
                if self.__board[row][col] != ox:
                    return 0
                return 1 + up(ox,row-1,col)
            def dow(ox,row,col):
            
                if row==self.__height:
                    return 0
                if self.__board[row][col] != ox:
                    return 0
                return 1 + dow(ox,row+1,col)
            return up(ox,row,col)+dow(ox,row,col)-1  
        def winsHor(ox,row,col):
        
            def lef(ox,row,col):
            
                if col<0:
                    return 0
                if self.__board[row][col] != ox:
                    return 0
                return 1 + lef(ox,row,col-1)
            def rit(ox,row,col):
            
                if col==self.__width:
                    return 0
                if self.__board[row][col] != ox:
                    return 0
                return 1 + rit(ox,row,col+1)
            return lef(ox,row,col)+rit(ox,row,col)-1 
         
        def winHelp(self,ox,row,col):
        
            if winsHor(ox,row,col)>=4  or winsVer(ox,row,col)>=4  or winsDiagll(ox,row,col)>=4  or winsDiaglr(ox,row,col)>=4:
                return True
        for row in range(self.__height):
            for col in range(self.__width):
                if self.__board[row][col]==ox:
                    if winHelp(self,ox,row,col)==True:
                        return True
        return False
    def hostGame(self):
        '''runs the game itself'''
    
        print('Welcome to Connect Four!')
        iswin=False
        move='O'
        while iswin ==False:
            print(self)
            print()
            print(move+'s choice',end=' ')
            col=int(input())
            print('\n')
            if self.allowsMove(col)==True:
                self.addMove(col, move)
                iswin=self.winsFor(move)
                if iswin==True:
                    print(move+' wins -- Congratulations!\n')
                if move=='O':
                    move='X'
                else:
                    move='O'
            else:
                print('Nice try pick a different column')
                print()
        print(self)
        

                
        
                
            
                       
    
        
