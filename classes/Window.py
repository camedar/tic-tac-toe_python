from math import *
import tkinter as tk
from tkinter import messagebox as mbox
from lib import *
from classes import Board

class Window(tk.Frame):
	def __init__(self,master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		#self.setGameOptionsModeScreen()

		#self.quit = tk.Button(self, text="Exit", fg="red", command=self.master.destroy)
		#self.quit.pack()
	
	def setGameOptionsModeScreen(self,callback):
		self.frameGameMode = tk.Frame(self)
		self.frameGameMode.grid(column=1,row=1)

		self.btn_2Players = tk.Button(self.frameGameMode, text="Player 1 Vs Player 2", command=lambda: callback(1))
		self.btn_2Players.grid(column=3,row=1)

		self.btn_1Player = tk.Button(self.frameGameMode, text="Player 1 Vs Computer", command=lambda: callback(2))
		self.btn_1Player.grid(column=3,row=2)

		self.removeGameModeFrame = tk.Button(self.frameGameMode, text="Clean", fg="red",
		                      command=self.frameGameMode.pack_forget)
		self.removeGameModeFrame.grid(column=3,row=4)

	def unsetGameOptionsModeScreen(self):
		self.frameGameMode.destroy()

	def setBoardScreen(self):
		self.frameBoard = tk.Frame(self)
		self.frameBoard.grid(column=1,row=1)

	def unsetBoardScreen(self):
		self.frameBoard.destroy()

	def quitGameMode(self,callback):
		confirm = mbox.askquestion ('Exit Game','Are you sure you want to exit the game',icon = 'warning')
		if confirm == "yes":
			self.unsetBoardScreen()
			self.setGameOptionsModeScreen(callback)

	def reInitGameMode(self,callbackRematch):
		confirm = mbox.askquestion ('Re-match','Are you sure you want re-initialize the game',icon = 'warning')
		if confirm == "yes":
			self.buttonContinuePlaying.destroy()
			self.buttonQuitGameMode.destroy()
			callbackRematch()

	def setContinuePlayingOnBoardScreen(self, callbackRematch, callbackQuitGame):
		self.buttonContinuePlaying = tk.Button(self.frameBoard, text="Re-match", command= lambda: self.reInitGameMode(callbackRematch))
		self.buttonQuitGameMode = tk.Button(self.frameBoard, text="Quit Game", command= lambda: self.quitGameMode(callbackQuitGame))
		self.buttonContinuePlaying.grid(column=1,row=1)
		self.buttonQuitGameMode.grid(column=4,row=1)