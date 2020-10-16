import tkinter as tk

class Symbol:
	symbolSize = 60
	def __init__(self, **kwargs):
		self.coordX = kwargs['x']
		self.coordY = kwargs['y']

class Circle(Symbol):
	color = "green"
	def __init__(self, canvas, **kwargs):
		self.canvas = canvas
		super().__init__(**kwargs)

	def draw(self):
		self.circle = self.canvas.create_oval( self.coordX - self.symbolSize, self.coordY - self.symbolSize, self.coordX + self.symbolSize, self.coordY + self.symbolSize, fill=None, outline=self.color, width=5)

	def undraw(self):
		self.canvas.after(100, self.canvas.delete, self.circle)

class Cross(Symbol):
	color = "blue"
	def __init__(self, canvas, **kwargs):
		self.canvas = canvas
		super().__init__(**kwargs)

	def draw(self):
		self.line1 = self.canvas.create_line( self.coordX - self.symbolSize, self.coordY - self.symbolSize, self.coordX + self.symbolSize, self.coordY + self.symbolSize, width=5, fill=self.color)
		self.line2 = self.canvas.create_line( self.coordX - self.symbolSize, self.coordY + self.symbolSize, self.coordX + self.symbolSize, self.coordY - self.symbolSize, width=5, fill=self.color)

	def undraw(self):
		self.canvas.after(100, self.canvas.delete, self.line1)
		self.canvas.after(100, self.canvas.delete, self.line2)

class Square(Symbol):
	color = "yellow"
	def __init__(self, canvas, **kwargs):
		self.canvas = canvas
		super().__init__(**kwargs)

	def draw(self):
		self.line1 = self.canvas.create_line( self.coordX - self.symbolSize, self.coordY - self.symbolSize, self.coordX + self.symbolSize, self.coordY - self.symbolSize, width=5, fill=self.color)
		self.line2 = self.canvas.create_line( self.coordX + self.symbolSize, self.coordY - self.symbolSize, self.coordX + self.symbolSize, self.coordY + self.symbolSize, width=5, fill=self.color)
		self.line3 = self.canvas.create_line( self.coordX - self.symbolSize, self.coordY + self.symbolSize, self.coordX + self.symbolSize, self.coordY + self.symbolSize, width=5, fill=self.color)
		self.line4 = self.canvas.create_line( self.coordX - self.symbolSize, self.coordY - self.symbolSize, self.coordX - self.symbolSize, self.coordY + self.symbolSize, width=5, fill=self.color)

	def undraw(self):
		self.canvas.after(100, self.canvas.delete, self.line1)
		self.canvas.after(100, self.canvas.delete, self.line2)
		self.canvas.after(100, self.canvas.delete, self.line3)
		self.canvas.after(100, self.canvas.delete, self.line4)