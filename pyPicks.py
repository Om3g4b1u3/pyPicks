'''
#	Program:	Python Picks
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
		self.btnBar.pack()4
	
	def getEntries(self):
		tempList = list()
		entryFile = open('classRoster.txt')
		for entry in entryFile.readlines():
			entry = entry.replace('\n', ' ').replace('\r', '')
			tempList.append(entry)
		return tempList
	
	def getNext(self):
		#self.currentEntry.set("omegaBlue")
		#self.totalLeft.set(909)
		
		if len(self.entries)==0:
			self.reset()
		else:
			tempStr = self.entries.pop(randint(0,(len(self.entries)-1)))
			self.currentEntry.set(tempStr)
			self.totalLeft.set(len(self.entries))
	
	def reset(self):	
		self.entries = self.getEntries()
		self.totalLeft.set(len(self.entries))
		self.getNext()
	

root = Tk()
myGUI = PyPicksApp(root)
root.mainloop()
