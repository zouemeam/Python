import random

try:
	import tkinter as tt
except ImportError:
	import Tkinter as tt


def loadimages(card_images):
	suits = ['heart', 'club', 'diamond', 'spade']
	face_cards = ['jack', 'queen', 'king']
	for pattern in suits:
		for card in range(1, 11):
			name = 'cards/{}_{}.{}'.format(str(card), pattern, 'ppm')
			image = tt.PhotoImage(file=name)
			card_images.append((card, image))
		for card in face_cards:
			name = 'cards/{}_{}.{}'.format(str(card), pattern, 'ppm')
			image = tt.PhotoImage(file=name)
			card_images.append((card, image))


def dealcard(frame):
	next_card = deck.pop()
	tt.Label(frame, image=next_card[1], relief='raised').pack(side='left')


def dealdealer():
	dealcard(dealerCardFrame)


def dealplayer():
	dealcard(playerCardFrame)


mainWindow = tt.Tk()

# mainwindow
mainWindow.title("Blackjack")
mainWindow.geometry("640x480")

# result
result_text = tt.StringVar
result = tt.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tt.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, rowspan=2, columnspan=3,sticky='ew')

# dealer
dealerScore = tt.IntVar()
dealerLabel = tt.Label(card_frame, text="Dealer", background='green', fg='white').grid(row=0, column=0)
dealerScoreLabel = tt.Label(card_frame, textvariable=dealerScore, background='green', fg='white').grid(row=1, column=0)
dealerCardFrame = tt.Frame(card_frame, background='green')
dealerCardFrame.grid(row=0, column=1, rowspan=2, sticky='ew')
# player
playerScore = tt.IntVar()
playerLabel = tt.Label(card_frame, text="Player", background='green', fg='white').grid(row=2, column=0)
playerScoreLabel = tt.Label(card_frame, textvariable=playerScore, background='green', fg='white').grid(row=3, column=0)
playerCardFrame = tt.Frame(card_frame, background='green')
playerCardFrame.grid(row=2, column=1, rowspan=2, sticky='ew')

# buttons
buttonFrame = tt.Frame(mainWindow)
buttonFrame.grid(row=3, column=0, columnspan=3, sticky='w')
dealButton = tt.Button(buttonFrame, text="Dealer", command=dealdealer).grid(row=0, column=0)
playButton = tt.Button(buttonFrame, text='Player', command=dealplayer).grid(row=0, column=1)
# program logic
cards = []

loadimages(cards)
deck = list(cards)
random.shuffle(deck)

# running the program
mainWindow.mainloop()
