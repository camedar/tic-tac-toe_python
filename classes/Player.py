import random
import time

class Player:
	def play():
		pass

# Overridden method
class Human(Player):
	x=-1
	y=-1
	def __init__(self,name,canvas):
		self.canvas = canvas
		self.name = name

	def play(self,callbackMakeMove):
		self.setPlayModeOn(callbackMakeMove)

	def setPlayModeOn(self,callback):
		if self.canvas:
			self.canvas.bind("<Button-1>", callback)

	def setPlayModeOff(self):
		if self.canvas:
			self.canvas.unbind("<Button-1>")

class Computer(Player):
	name = "Computer"
	def __init__(self,board):
		self.board = board

	def play(self,callback):
		time.sleep(1)
		x = random.randint(0,2)
		y = random.randint(0,2)
		while self.board[x][y] != 0:
			x = random.randint(0,2)
			y = random.randint(0,2)
		
		callback( {'x':x,'y':y} )

	def setPlayModeOff(self):
		pass


