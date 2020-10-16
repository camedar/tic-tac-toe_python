import numpy as np
import tkinter as tk
import math, time

class Board:
	cellSize = 150
	lineOfVictoryColour = "orange"
	def __init__(self, frame):
		self.containerFrame = frame
		self.boardMatrix = np.zeros((3,3))
		self.boardMatrixObjects = [[None for i in range(3)] for j in range(3)]
		self.currentPlayerIdentifier = 2 #Alternates between 2 and 10

	def __del__(self):
		self.canvas.destroy()

	def drawBoard(self):
		self.canvas = tk.Canvas( self.containerFrame, width=450, height=450)
		self.canvas.grid(column=2,row=2)

		# Lines
		leftVerticalLine = self.canvas.create_line(self.cellSize, 0, self.cellSize, 3*self.cellSize, width=5)
		rightVerticalLine = self.canvas.create_line(2*self.cellSize, 0, 2*self.cellSize, 3*self.cellSize, fill="red",width=5)
		upHorizontalLine = self.canvas.create_line( 0, self.cellSize, 3*self.cellSize, self.cellSize, width=5)
		downHorizontalLine = self.canvas.create_line(0, 2*self.cellSize, 3*self.cellSize, 2*self.cellSize, fill="red", width=5)

		# Dots in vertex
		self.canvas.create_oval(self.cellSize-7, self.cellSize-7, self.cellSize+7, self.cellSize+7, fill="white", outline="")#left-up dot
		self.canvas.create_oval(2*self.cellSize-7, self.cellSize-7, 2*self.cellSize+7, self.cellSize+7, fill="white", outline="")#right-up dot
		self.canvas.create_oval(self.cellSize-7, 2*self.cellSize-7, self.cellSize+7, 2*self.cellSize+7, fill="white", outline="")#left-down dot
		self.canvas.create_oval(2*self.cellSize-7, 2*self.cellSize-7, 2*self.cellSize+7, 2*self.cellSize+7, fill="white", outline="")#right-down dot

	def getXYCellFromClickPosition(self,**kwargs):
		matrixX = int(math.ceil(kwargs['x'] / self.cellSize)) - 1
		matrixY = int(math.ceil(kwargs['y'] / self.cellSize)) - 1

		if matrixX < 0 or matrixX > 2 or matrixY < 0 or matrixY > 2:
			return None

		return {"x": matrixX, "y": matrixY}

	def isCellFree(self, **kwargs):
		if self.boardMatrix[kwargs['x']][kwargs['y']] == 0:
			return True
		
		return False

	def setCellAsTaken(self, symbolObject, **kwargs):
		x,y = kwargs['x'],kwargs['y']
		self.boardMatrix[x][y] = self.currentPlayerIdentifier
		self.boardMatrixObjects[x][y] = symbolObject
		# Set identifier of player, alternates between 2 and 10 for odd and even turn resepctively
		self.currentPlayerIdentifier = 10 if self.currentPlayerIdentifier == 2 else 2

	def getCoordFromMatrixPosition(self, **kwargs):
		midPoint = int(math.floor(self.cellSize / 2))
		x = kwargs['x'] * self.cellSize + midPoint
		y = kwargs['y'] * self.cellSize + midPoint

		return {"x": x, "y": y}

	def getObjectFromCell(self, **kwargs):
		return self.boardMatrixObjects[kwargs['x']][kwargs['y']]

	def setCellAsNotTaken(self, symbolObject, **kwargs):
		self.boardMatrix[kwargs['x']][kwargs['y']] = 0
		objToDelete = self.boardMatrixObjects[kwargs['x']][kwargs['y']]
		self.boardMatrixObjects[kwargs['x']][kwargs['y']] = None
		del objToDelete

	#-1: No options for anybody; 0: Open Options; 1: Player 1 Wins; 2: Player 2 wins 
	def whoWins(self):
		player1 = 36
		player2 = 36
		linesForWins = [
						{'x1': 0, 'y1':0, 'x2': 1, 'y2': 1, 'x3': 2, 'y3': 2},#1 - diagonal 1
						{'x1': 2, 'y1':0, 'x2': 1, 'y2': 1, 'x3': 0, 'y3': 2},#2 - diagonal 2
						{'x1': 0, 'y1':0, 'x2': 1, 'y2': 0, 'x3': 2, 'y3': 0},#3 - horizontal 1
						{'x1': 0, 'y1':1, 'x2': 1, 'y2': 1, 'x3': 2, 'y3': 1},#4 - horizontal 2
						{'x1': 0, 'y1':2, 'x2': 1, 'y2': 2, 'x3': 2, 'y3': 2},#5 - horizontal 3
						{'x1': 0, 'y1':0, 'x2': 0, 'y2': 1, 'x3': 0, 'y3': 2},#6 - vertical 1
						{'x1': 1, 'y1':0, 'x2': 1, 'y2': 1, 'x3': 1, 'y3': 2},#7 - vertical 2
						{'x1': 2, 'y1':0, 'x2': 2, 'y2': 1, 'x3': 2, 'y3': 2},#8 - vertical 3
						]
		for idx,item in enumerate(linesForWins):
			lineSum = self.boardMatrix[item['x1']][item['y1']] + self.boardMatrix[item['x2']][item['y2']] + self.boardMatrix[item['x3']][item['y3']]
			if int(lineSum) == 6 or int(lineSum) == 30:
				self.drawLineVictory(idx+1)
				return 1 if int(lineSum) == 6 else 2
			
			if int(lineSum) >= 10:
				player1 = player1 - (idx + 1)
			if int(lineSum) % 2 == 0 and int(lineSum) % 10 > 0:
				player2 = player2  - (idx + 1)

		if player1 + player2 == 0:
			return -1

		return 0

	def drawLineVictory(self,winLine):
		step = 10
		initialX = 0
		initialY = 0
		finalX = 3 * self.cellSize
		finalY = 3 * self.cellSize
		if winLine == 2:
			initialX = int(self.cellSize * 3)
			finalX = 0
		if winLine == 3:
			initialY = finalY = int(self.cellSize / 2)
		if winLine == 4:
			initialY = finalY = int(self.cellSize + self.cellSize / 2)
		if winLine == 5:
			initialY = finalY = int(self.cellSize * 2 + self.cellSize / 2)
		if winLine == 6:
			initialX = finalX = int(self.cellSize / 2)
		if winLine == 7:
			initialX = finalX = int(self.cellSize + self.cellSize / 2)
		if winLine == 8:
			initialX = finalX = int(self.cellSize * 2 + self.cellSize / 2)

		i = 0
		while(i < int(self.cellSize * 3 / step)):
			finalX_ = initialX
			finalY_ = initialY
			if(initialX + step <= finalX):
				finalX_ += step
			if(initialY + step <= finalY):
				finalY_ += step
			if(initialX - step >= finalX):
				finalX_ -= step
			
			self.canvas.create_line(initialX, initialY, finalX_, finalY_, fill=self.lineOfVictoryColour, width=5)

			if(initialX + step <= finalX):
				initialX += step
			if(initialY + step <= finalY):
				initialY += step
			if(initialX - step >= finalX):
				initialX -= step

			i += 1
			time.sleep(0.01)
			self.canvas.update()