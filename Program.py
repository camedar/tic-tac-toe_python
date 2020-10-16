import tkinter as tk
from tkinter import messagebox as mbox
import time
from classes import Window, Circle, Cross, Square, Board, Human, Computer

class Program:
	canvas= None
	player1Symbol = 1
	player2Symbol = 3
	player1Obj = None
	player2Obj = None
	player1Turn = None
	player2Turn = None
	gameMode = 0 # 1: player 1 vs player 2; 2: player 1 vs Computer

	@staticmethod
	def definePlayerTurnsAndPlayers():
		Program.player1Turn = "odd"
		Program.player2Turn = "even"
		if Program.gameMode == 1:
			Program.player1Obj = Human("Player 1",Program.canvas)
			Program.player2Obj = Human("Player 2",Program.canvas)
		if Program.gameMode == 2:
			Program.player1Obj = Human("Player 1",Program.canvas)
			Program.player2Obj = Computer(Program.board.boardMatrix)

	def go2BoardScreen(gameMode):
		Program.screen.unsetGameOptionsModeScreen()
		Program.gameMode = gameMode

		# Draw frame of the screen for the Board
		Program.screen.setBoardScreen()
		Program.initBoard()
		

	@staticmethod
	def initBoard():
		# Object Game Board
		try:
			del Program.board
		except: pass

		Program.board = Board(Program.screen.frameBoard)
		Program.board.drawBoard()
		Program.canvas = Program.board.canvas

		Program.movesCounter = 1
		Program.definePlayerTurnsAndPlayers()
		Program.gameFlow()

	@staticmethod
	def makeMove(x,y):
		# if the cell in the matrix for the board is free
		if Program.board.isCellFree(x=x,y=y):
			# Get coordinates to draw the symbol according to position in the matrix
			coordToDrawSymbol = Program.board.getCoordFromMatrixPosition(x=x,y=y)
			symbolObj = None
			# Assign type of symbol corresponding to each player (turn1: player 1; turn 2: player 2)
			if(Program.board.currentPlayerIdentifier == 2):	
				symbolObj = Program.symbolFactory(Program.player1Symbol, coordToDrawSymbol['x'], coordToDrawSymbol['y'])
			else:
				symbolObj = Program.symbolFactory(Program.player2Symbol, coordToDrawSymbol['x'], coordToDrawSymbol['y'])
			symbolObj.draw()
			Program.canvas.update()
			# set position in board as taken
			Program.board.setCellAsTaken(symbolObj,x=x,y=y)

			return True
		
		return False

	@staticmethod
	def isGameFinished():
		gameResult = Program.board.whoWins()
		if gameResult != 0:
			finalMessage = ""
			if gameResult == -1:
				finalMessage = "Draw!"
			elif gameResult > 0:
				finalMessage = f"{Program.playerInTurn.name} wins!"

			mbox.showinfo('Game Over', finalMessage)
			Program.screen.setContinuePlayingOnBoardScreen(Program.initBoard,Program.go2BoardScreen)
			return True
		return False

	@staticmethod
	def gameFlow():
		if Program.isGameFinished():
			return
		print("Move: " + str(Program.movesCounter))

		# Activate Click
		Program.playerInTurn = Program.player1Obj

		#define whose turn it is
		if Program.movesCounter % 2 == 0:
			Program.playerInTurn = Program.player2Obj
		print (Program.playerInTurn)

		Program.playerInTurn.play(Program.verifyMove)

	def verifyMove(event):
		x,y = None,None
		matrixCoord = None
		if type(event) is tk.Event:
			x,y = event.x,event.y
			# detect cell in matrix for board according to click coordinates
			matrixCoord = Program.board.getXYCellFromClickPosition(x=x,y=y)
		else:
			matrixCoord = event

		if matrixCoord != None:
			moveDone = Program.makeMove(x=matrixCoord['x'],y=matrixCoord['y'])
			if moveDone:
				Program.movesCounter += 1
				Program.playerInTurn.setPlayModeOff()
				Program.gameFlow()

	@staticmethod
	def symbolFactory(playerNumber, x, y):
		symbolTypes = {
			1 : Circle(Program.canvas, x=x, y=y),
			2 : Cross(Program.canvas, x=x, y=y),
			3 : Square(Program.canvas, x=x, y=y)
		}
		return symbolTypes[playerNumber]

	@staticmethod
	def main():
		root = tk.Tk()
		root.title("Tic-Tac-Toe")
		root.geometry("800x600")
		Program.screen = Window(master=root)
		Program.screen.setGameOptionsModeScreen(Program.go2BoardScreen)
		Program.screen.mainloop()

Program.main()