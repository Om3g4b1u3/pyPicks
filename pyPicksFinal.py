'''
#	Program:	Python Picks ( I2P Final Exam )
#	Filename:	pyPicks.py
#	Author:		omegaBlue
'''
from tkinter import *
from random import *

class PyPicksApp:
	def __init__(self, master):
		self.master = master
		master.title("Python Picks App")
        
		self.entries = list()
		self.currentEntry = StringVar()
		self.currentEntry.set("PRESS RESET OR NEXT")
		self.entryLbl = Label(master, textvariable=self.currentEntry, font="Impact 48")
		self.entryLbl.pack()

		self.dispBar = Frame(master)
		self.dispLbl = Label(self.dispBar, text="No. Left: ", font="Impact 48")
		self.dispLbl.pack(side=LEFT)
		
		self.totalLeft = IntVar()
		self.totalLeft.set(0)
		self.numLbl = Label(self.dispBar, textvariable=self.totalLeft, font="Impact 48")
		self.numLbl.pack(side=LEFT)
		self.dispBar.pack()

		self.btnBar = Frame(master, width=36)
		self.nextBtn = Button(self.btnBar, text="NEXT", width=12, font="Impact 28", command=self.getNext)
		self.nextBtn.pack(side=LEFT)
		self.resetBtn = Button(self.btnBar, text="RESET", width=12, font="Impact 28", command=self.reset)
		self.resetBtn.pack(side=LEFT)
		self.quitBtn = Button(self.btnBar, text="QUIT", width=12, font="Impact 28", command=master.quit)
		self.quitBtn.pack(side=LEFT)
		self.btnBar.pack()

	def getEntries(self):
		tempList = list()
		entryFile = open('classRoster.txt')
		'''
			Part 1: 	For Loops
			Objectives:	Create a for loop that will "readlines()" of a file, and save them to the tempList
			Warning:	Do not alter anything outside of the "YOUR CODE HERE" Comments
			Hint:		How can you remove end-line characters?
		'''
		#	YOUR CODE HERE - BEGIN

	
		#	YOUR CODE HERE - END
		return tempList

	'''
		Part 2:		IF-ELSE Control Statements
		Objectives:	Remove the 2 lines and create an if-else statement to "reset()" when their are 0 left.
		Warning:	Again, stay inside "YOUR CODE HERE" Comments
		Hints:		You may want to see how I used .set() before deleting the lines
	'''
	def getNext(self):
		#	YOUR CODE HERE - BEGIN
		self.currentEntry.set("omegaBlue")
		self.totalLeft.set(909)
		#	YOUR CODE HERE - END

	'''
		Part 3:		Writing & Calling Functions
		Objectives:	A) Rewrite the function to re-initialize "entries" by calling call getEntries()
				B) Call getNext() to restart the list
		Warnings:	Yes, a third time, stay within "YOUR CODE HERE" Comments
	'''
	def reset(self):
		#	YOUR CODE HERE - BEGIN
		self.currentEntry.set("PRESS NEXT")
		self.totalLeft.set(3.14)
		#	YOUR CODE HERE - END		

root = Tk()
myGUI = PyPicksApp(root)
root.mainloop()
