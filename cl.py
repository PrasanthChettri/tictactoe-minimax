import msvcrt
from os import system
from os import sys
from hna import comp
#TODO : Make GUI this shit is n00b
#__________________________________________________________________________________
class game:
	def __init__(self):
		self.ai = comp(self)
		self.mainmatrix = [' ']*9 
		self.pos_matrix = [' ']*9 
		self.pos,self.draw_var = 4,0
		self.symbols , self.feeder = ['o' , 'x'] , [] 
		self.emp = list(range(9))
	def checker( self,mat, sym):
		for i in range(3):
			if mat[i*3] + mat[i*3+1] + mat[i*3+2] == sym :
				return  1
			if mat[i] + mat[i+3] + mat[i+6] == sym :
				return  1
		if  mat[0]+ mat[4] + mat[8] == sym :
			return  1
		if mat[2] + mat[4] + mat[6]  == sym:
			return 1
		return None  
	def matrix_giver(self  , cord):
		self.pos_matrix[self.pos] = ' '
#conditions =============================================================================================
		if cord == 'w' and self.pos > 2 :
			self.pos-=3 
		elif cord == 's' and self.pos < 6:
			self.pos += 3
		elif cord == 'a' and  self.pos  not in [0 , 3, 6]:
			self.pos -= 1
		elif cord == 'd' and self.pos  not in [2 ,5 , 8]:
			self.pos += 1
		elif cord == 'e' and self.mainmatrix[self.pos] == ' ':
			self.mainmatrix[self.pos] = self.symbols[self.draw_var % 2]
			gameov = self.checker(self.mainmatrix, 'ooo')
			self.emp.remove(self.pos)
			if gameov is not None :
				print ("o won!\n")
				input()
				sys.exit()
			self.draw_var +=1 
			
#==============================================================================================		
		self.pos_matrix[self.pos] = self.symbols[self.draw_var % 2]

	def maingame(self):
		while(self.draw_var < 9):
			gameov = None	
			system("cls")
			print ("-"*13)
			for i in range(9):
				print ("|" + self.pos_matrix[i]+self.mainmatrix[i] , "", end = '')
				if (i+1) % 3 == 0 :	
					print ("|\n"+"-"*13)
			if (self.draw_var+1)%2 :
				gameov = self.checker(self.mainmatrix, 'xxx')
				if gameov :
					print("x won!")
					input()
					exit()		
				self.matrix_giver(msvcrt.getch().decode("UTF_8"))
			elif self.draw_var%2 :
				self.ai.move()
				self.draw_var += 1
				
z = game()
z.maingame()