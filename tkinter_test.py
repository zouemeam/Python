try:
	import tkinter
except ImportError:
	import Tkinter as tkinter
import os

mainWindow = tkinter.Tk()
mainWindow.title("Grid Demo")
mainWindow.geometry('640x400+50+50')
mainWindow['padx']=8
label1 = tkinter.Label(mainWindow, text="Tkinter Grid Demo").grid(row=0, column=0, columnspan=3, sticky="we")

mainWindow.columnconfigure(0, weight=1)#actually means how fast each widget increase as the box expands
mainWindow.columnconfigure(1, weight=1)#actual size of widget is largely determined by the widget itself
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

fileList = tkinter.Listbox(mainWindow)
fileList.grid(sticky='nsew', rowspan=2)
fileList.config(border=5, relief='sunken')
for zone in os.listdir('/Windows/System32'):
	fileList.insert(tkinter.END, zone)

listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)
listScroll.grid(row=1, column=1, rowspan=2, sticky="nsw")
listScroll.config(border=2, relief='sunken')
fileList["yscrollcommand"] = listScroll.set

optionFrame=tkinter.LabelFrame(mainWindow,text="File Details")
optionFrame.grid(row=1,column=2,sticky='ne')

rbValue=tkinter.IntVar()
rbValue.set(3)

radio1=tkinter.Radiobutton(optionFrame,text='Filename',value=1,variable=rbValue)
radio2=tkinter.Radiobutton(optionFrame,text='Path',value=2,variable=rbValue)
radio3=tkinter.Radiobutton(optionFrame,text='Timestamp',value=3,variable=rbValue)
radio1.grid(row=0,column=0,sticky='w')
radio2.grid(row=1,column=0,sticky='w')
radio3.grid(row=2,column=0,sticky='w')


resultLabel=tkinter.Label(mainWindow,text='Result')
resultLabel.grid(row=2,column=2,sticky='wn')
result=tkinter.Entry(mainWindow)
result.grid(row=2,column=2,sticky='sw')
#it is possible to add two widgets to the same grid
#timeFrame
timeFrame=tkinter.LabelFrame(mainWindow,text='Time')
timeFrame.grid(row=3,column=0,sticky='new')
hourSpinner=tkinter.Spinbox(timeFrame,width=2,values=tuple(range(0,24)))
minuteSpinner=tkinter.Spinbox(timeFrame,width=2,from_=0, to_=59)
secondSpinner=tkinter.Spinbox(timeFrame,width=2,from_=0, to_=59)
hourSpinner.grid(row=0,column=0)
tkinter.Label(timeFrame,text=":").grid(row=0,column=1)
minuteSpinner.grid(row=0,column=2)
tkinter.Label(timeFrame,text=":").grid(row=0,column=3)
secondSpinner.grid(row=0,column=4)
timeFrame['padx']=36
#frame for the date spinner
dateFrame=tkinter.LabelFrame(mainWindow,text="Date")
dateFrame.grid(row=4,column=0,sticky='new')
yearLabel=tkinter.Label(dateFrame, text='Year').grid(row=0, column=2)
monthLabel=tkinter.Label(dateFrame,text='Month').grid(row=0,column=1)
dayLabel=tkinter.Label(dateFrame,text='Day').grid(row=0,column=0)
daySpin=tkinter.Spinbox(dateFrame,width=5,from_=1, to_=30).grid(row=1,column=0)
monthSpin=tkinter.Spinbox(dateFrame,width=5,values=('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')).grid(row=1,column=1)
yearSpin=tkinter.Spinbox(dateFrame,width=5,from_=2000,to_=2018).grid(row=1,column=2)
dateFrame['padx']=18

#buttons
okButton=tkinter.Button(mainWindow,text="Ok")
cancelButton=tkinter.Button(mainWindow,text='Cancel',command=mainWindow.quit)#just use function name with no argument parenthesis
okButton.grid(row=4,column=3,sticky='e')
cancelButton.grid(row=4,column=4,sticky='w')
mainWindow.mainloop()
