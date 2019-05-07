#MINIMAX AND SOME HELPER FUNCIONS
class comp():
    def __init__(self , gameins):
        self.gameins = gameins 
    def move(self):
        x ,p = self.minimax(self.gameins.mainmatrix , self.gameins.emp)
        self.gameins.emp.remove(x)
        self.gameins.mainmatrix[x] = 'x'
    def minimax(self , mat , emp , pl = 'x'):
        k  = -1
        cop = emp.copy() 
        if pl == 'x':
            np = 'o'
            mns = [-1 , -float('inf')]
        elif pl == 'o': 
            np = 'x'
            mns = [-1 , float('inf')]
        value = self.evaluate(mat)
        if value or len(emp) == 0 :
            return -1 , value
        for pos in emp :
            cop.remove(pos)
            mat[pos] = pl
            x , score = self.minimax(mat , cop ,pl = np) 
            cop.append(pos)
            mat[pos] = ' '
            if mns[1] < score and pl == 'x':
                mns[1] = score
                mns[0] = pos
            elif mns[1] > score and pl == 'o' :
                mns[1] = score
                mns[0] = pos
        return mns
    def evaluate(self, mat):
        if self.gameins.checker(mat , 'xxx') :
            return 1
        elif self.gameins.checker(mat , 'ooo') :
            return -1
        return 0 


