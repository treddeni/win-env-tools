from tkinter import *
from path import *

class PathEditor(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.render()
		
	def render(self):
		pathTextFrame = Frame(self)
		pathTextFrame.pack(padx = 10, pady = 10)
		
		pathTextScrollBar = Scrollbar(pathTextFrame)
		pathText = Text(pathTextFrame, height=40, width=100)
		pathText.insert(END, self.formattedPath())

		pathText.pack(side = LEFT, fill = BOTH)
		pathTextScrollBar.pack(side = LEFT, fill = BOTH)
		
		pathTextScrollBar.config(command = pathText.yview)
		pathText.config(yscrollcommand = pathTextScrollBar.set)
		self.pathText = pathText

		savePathButton = Button(self, text = "Save Path")
		savePathButton["command"] = self.save
		savePathButton.pack(side = LEFT, padx = 10, pady = 10)
		
		appendPathButton = Button(self, text = "Append to Path and Save Path")
		appendPathButton.bind('<Button-1>', self.append)
		appendPathButton.pack(side = RIGHT, padx = 10, pady = 10)		
		
		pathEntry = Entry(self, width = 70)
		pathEntry.pack(side = RIGHT, pady = 10)
		pathEntry.bind('<Return>', self.append)
		self.pathEntry = pathEntry
		
		pathLabel = Label(self, text = "Path to Append:")
		pathLabel.pack(side = RIGHT, pady = 10)
		
	def append(self, event):
		appendToPath(self.pathEntry.get())
		self.pathText.delete(1.0, END)
		self.pathText.insert(END, self.formattedPath())
		print(self.formattedPath())
		
	def save(self):
		setPath(self.pathText.get(1.0, END).replace('\n', ';'))
		
	def formattedPath(self):
		formattedPath = ''
		paths = getPath().split(';')
		for i in range(0, len(paths)):
			formattedPath += paths[i] + '\n'
		return formattedPath.rstrip()

root = Tk()
root.title("Windows Path Editor")
app = PathEditor(root)
root.mainloop()