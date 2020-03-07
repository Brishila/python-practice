import random

def printboard(testboard):
    print(testboard[9] + '|' + testboard[8] + '|' + testboard[7])
    print(testboard[6] + '|' + testboard[5] + '|' + testboard[4])
    print(testboard[3] + '|' + testboard[2] + '|' + testboard[1])

def getinput():
    check = True
    while check:
        marker = input("Please pick a marker 'X' or 'O'").upper()
        if marker == 'X':
            return('X', 'O')
        elif marker == 'O':
            return('O', 'X')

def wincheck(testboard):
    for i in range(1, len(testboard)-1):
        if testboard[i:i+3] == ['X', 'X', 'X'] or ['X', 'X', 'X'] == testboard[i::4] or ['X', 'X', 'X'] == testboard[i::3]:
            return True

def getplayer(players):
    return random.choice(players)

def getnumber(testboard, marker, player):
    position = int(input(player + ': Please enter a number'))
    testboard[position] = marker[player]
    return testboard

def replay():
    check = True
    while check:
        replayflag = input('Do you want to replay ? (yes/no)').upper()
        if replayflag == 'YES':
            return True
        elif replayflag == 'NO':
            print('Untill next time..')
            return False
        else:
            print('Please enter (yes/no)')

replayflag = True

while replayflag:
    testboard = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    players = ['Player1', 'Player2']
    player = getplayer(players)
    print('Welcome to TicTacToe')
    print(f'Hi {player} it is your turn')
    marker = {}
    inputs = getinput()
    if player == players[0]:
        marker[players[0]] = inputs[0]
        marker[players[1]] = inputs[1]
    else:
        marker[players[1]] = inputs[0]
        marker[players[0]] = inputs[1]

    check = False 

    while not check:
        for key,value in marker.items():
            printboard(testboard)
            testboard = getnumber(testboard, marker, key)
            check = wincheck(testboard)
            if check:
                break
    print(player + ' Congratulations !!')
    replayflag = replay()

 