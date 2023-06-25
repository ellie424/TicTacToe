import PySimpleGUI as sg
import game_window

sg.theme("GreenMono")

layout = [
	[sg.Text("Player1 name: "), sg.Input(key = 'FIRST_PLAYER', do_not_clear = True, size = (20,1))],
	[sg.Text("Player2 name: "), sg.Input(key = 'SECOND_PLAYER', do_not_clear = True, size = (20,1))],
	[sg.Button("Start Game"), sg.Exit()]
]

window = sg.Window('Tic Tac Toe', layout)

while True:
	event, values = window.read()
	if event == sg.WIN_CLOSED or event == 'Cancel':
		break
	elif event == "Start Game":
		players = [values['FIRST_PLAYER'], values['SECOND_PLAYER']]
		game_window.initiate_game(players)