import PySimpleGUI as sg      

sg.theme("GreenMono")

layout = [[sg.Text("Place your move")]]    

def check_if_winner(board):
	for col in range(0, 3):
		print(board)
		if ((0, col) in board.keys()) and ((1, col) in board.keys()) and ((2, col) in board.keys()):
			if board[(0, col)] == board[(1, col)] == board[(2, col)]:
				return board[(0, col)]
	for row in range(0, 3):
		print(board)
		if ((0, row) in board.keys()) and ((1, row) in board.keys()) and ((2, row) in board.keys()):
			if board[(0, row)] == board[(1, row)] == board[(2, row)]:
				return board[(0, row)]

	if ((0, 0) in board.keys()) and ((1, 1) in board.keys()) and ((2, 2) in board.keys()):
		if board[(0,0)] == board[(1,1)] == board[(2,2)]:
			return board[(1,1)]
	if ((2, 0) in board.keys()) and ((1, 1)in board.keys()) and ((0, 2) in board.keys()):
		if board[(2,0)] == board[(1,1)] == board[(0,2)]:
			return board[(2,0)]


def initiate_game(players):
	board, player = {}, 0

	layout = [[sg.Text("Your move", key = 'CURRENT_PLAYER')]]
	
	for row in range(3):
		new_row = []
		for column in range(3):
			new_row.append(sg.Button(size=(3,2), key=(row, column)))
		layout.append(new_row)
	layout.append([sg.Button("reset"), sg.Button('quit')])
	
	window = sg.Window("TicTacTow", layout)
	
	while True:
		event, values = window.read()
		if event == sg.WIN_CLOSED or event == "quit":
			break
	
		if event == 'reset':
			board = {}
			for row in range(3):
				for col in range(3):
					window[(row, col)].update('')
		elif event not in board:
			board[event] = player
			window[event].update('X' if player else 'O')
			is_winner = check_if_winner(board)
			if is_winner is not None:
				sg.popup('The Winner is ' + players[player])
				break
			player = (player + 1) %2
			window["CURRENT_PLAYER"].update("Your moveCurrent player: " + players[player])

	window.close()