import random

try:
	import tkinter
except ImportError:
	import Tkinter as tkinter


def _load_images(card_images):
	suits = ['heart', 'club', 'diamond', 'spade']
	face_cards = ['jack', 'queen', 'king']
	for suit in suits:
		for card in range(1, 11):
			name = 'cards/{}_{}.{}'.format(str(card), suit, 'ppm')
			image = tkinter.PhotoImage(file=name)
			card_images.append((card, image,))
		for card in face_cards:
			name = 'cards/{}_{}.{}'.format(card, suit, 'ppm')
			image = tkinter.PhotoImage(file=name)
			card_images.append((10, image,))


def score_hand(hand):  # to calculate the total score of all cards in hand
	score = 0
	ace = False
	for card in hand:
		card_value = card[0]
		if card_value == 1 and not ace:
			card_value = 11
			ace = True
		score += card_value
		if score > 21 and ace:
			score -= 10
			ace = False
	return score


def deal_card(frame):
	# pop the next card off the top of the deck
	next_card = deck.pop(0)  # taking card off the top of the deck
	deck.append(next_card)  # adding card back do we don't run out of cards
	tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
	return next_card


def deal_dealer():
	# dealer_hand.append(deal_card(dealer_card_frame))
	dealer_score = score_hand(dealer_hand)
	while 0 < dealer_score < 17:
		dealer_hand.append(deal_card(dealer_card_frame))
		dealer_score = score_hand(dealer_hand)
		dealer_score_label.set(dealer_score)

	player_score = score_hand(player_hand)
	if player_score > 21:
		result_text.set("Dealer Wins")
	elif dealer_score > 21 or dealer_score < player_score:
		result_text.set("Player Wins")
	elif player_score < dealer_score:
		result_text.set("Dealer Wins")
	else:
		result_text.set("Draw")


def deal_player():
	player_hand.append(deal_card(player_card_frame))
	player_score = score_hand(player_hand)
	player_score_label.set(player_score)
	if player_score > 21:
		result_text.set("Dealer wins")
	elif player_score == score_hand(dealer_hand):
		result_text.set("Draw")


def newGame():
	global player_card_frame
	global dealer_card_frame
	global dealer_hand
	global player_hand
	# embedded frame to hold card images
	dealer_card_frame.destroy()
	dealer_card_frame = tkinter.Frame(card_frame, background='green')
	dealer_card_frame.grid(row=0, column=1, rowspan=2, sticky='ew')
	player_card_frame.destroy()
	player_card_frame = tkinter.Frame(card_frame, background='green')
	player_card_frame.grid(row=2, column=1, rowspan=2, sticky='ew')
	result_text.set('')
	dealer_hand = []
	player_hand = []
	deal_player()
	dealer_hand.append(deal_card(dealer_card_frame))
	dealer_score_label.set(score_hand(dealer_hand))
	deal_player()


def shuffle_card():
	random.shuffle(deck)


def playGame():
	mainWindow.mainloop()


mainWindow = tkinter.Tk()
mainWindow.title('Black Jack')
mainWindow.geometry("640x480")
mainWindow.configure(background='green')
result_text = tkinter.StringVar()

# main window
result = tkinter.Label(mainWindow, textvariable=result_text, background='green')
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background='green')
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

# dealer
dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg='white').grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background='green', fg='white').grid(row=1, column=0)
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

# player
player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Player", background='green', fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

# button frame
button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')
dealer_button = tkinter.Button(button_frame, text='Dealer', command=deal_dealer)
dealer_button.grid(row=0, column=0)
player_button = tkinter.Button(button_frame, text='Player', command=deal_player)
player_button.grid(row=0, column=1)
newgame_button = tkinter.Button(button_frame, text="New Game", command=newGame)
newgame_button.grid(row=0, column=2)
shuffle_button = tkinter.Button(button_frame, text="Shuffle", command=shuffle_card)
shuffle_button.grid(row=0, column=3)

cards = []
_load_images(cards)
# create a new deck of cards and shuffle it
deck = list(cards)
shuffle_card()
# create the list to store dealer and player hands
# dealer_hand = []
# player_hand = []
newGame()

# start game loop
if __name__ == "__main__":
	playGame()  # will only run this code if it is being executedm if run __name__=main otherwise name=name of this python file
