import random

markers = []
positions = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9']
winner = 'Draw'
p1 = 'Player 1'
p2 = 'Player 2'


def tictactoe():
    def draw(board):
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')

    draw(positions)

    def marker_selection():
        starter = random.randint(1, 2)
        if starter == 1:
            print(p1 + " is starting the game")
            firstplayer = p1
        else:
            print(p2 + " is starting the game")
            firstplayer = p2

        while not markers:
            player = input(firstplayer + " you want to be X or O? ").upper()
            if player == "X":
                markers.extend(['X', 'O'])
                print(firstplayer + " wanted to play with X" + "\n")
            elif player == "O":
                markers.extend(['O', 'X'])
                print(firstplayer + " wanted to play with O" + "\n")
            else:
                print("Try again")
                continue
            return markers

    marker_selection()

    def placemarker():
        place = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        count = 1
        global winner, markers

        while winner == "Draw":
            p = int(input("Which position do you want to place your marker?"))
            if p > 9:
                continue
            while place[p] == ' ':
                if count % 2 != 0:
                    place[p] = markers[0]
                else:
                    place[p] = markers[1]
                count += 1
                draw(place)

            def winconditions():
                global winner, markers
                win = [p1, p2]
                for i in win:
                    for j in markers:
                        if place[1] == place[2] == place[3] == j:
                            winner = i
                        elif place[4] == place[5] == place[6] == j:
                            winner = i
                        elif place[7] == place[8] == place[9] == j:
                            winner = i
                        elif place[1] == place[4] == place[7] == j:
                            winner = i
                        elif place[2] == place[5] == place[8] == j:
                            winner = i
                        elif place[3] == place[6] == place[9] == j:
                            winner = i
                        elif place[1] == place[5] == place[9] == j:
                            winner = i
                        elif place[3] == place[5] == place[7] == j:
                            winner = i

            winconditions()
        print('The winner is ' + winner)
    placemarker()


tictactoe()
