# Game Homework
import random

def rolldice():
    return random.randint(1,6)
# I defined rolldice() function by making it a number between the inclusive range (1,6)

squares = [
{
"penalty": -1,
"reward": -1
},
{
"penalty": -1,
"reward": -1
}
]

squares[0]["penalty"] = int(input("Player 1, please enter your penalty square number: "))
squares[0]["reward"] = int(input("Player 1, please enter your reward square number: "))
squares[1]["penalty"] = int(input("Player 2, please enter your penalty square number: "))
squares[1]["reward"] = int(input("Player 2, please enter your reward square number: "))
# users input the value of penalty and reward squares

print(squares) #just for me to see the values, not neccessary

players_current_squares = [0, 0]
# each value represents the position of a player, which will change later on

while players_current_squares[0] < 100 and players_current_squares[1] < 100:
    
    #for player 1
    rolldice()  
    dice = rolldice()
    print(f"player 1's dice rolled {dice}")
    
    players_current_squares[0] += dice
    

    if players_current_squares[0] == squares[0]['penalty'] or players_current_squares[0] == squares[1]['penalty']:
        players_current_squares[0] -= 10
        print(f'player 1 stepped on a penalty square. Player 1 is currently in square {players_current_squares[0]}')
    elif players_current_squares[0] == squares[0]['reward'] or players_current_squares[0] == squares[1]['reward']:
        players_current_squares[0] += 10
        print(f'player 1 stepped on a reward square. Player 1 is currently in square {players_current_squares[0]}')
    elif players_current_squares[0] >= 100:
        #in the rules it wasn't sepicified what happens if a dice rolls a random number and a player exceeds 100, so I count it as a win
        print(f'player 1 is currently in square {players_current_squares[0]}')
        print('player 1 won')
        break
    else:
        print(f'player 1 is currently in square {players_current_squares[0]}')
    
    #for player 2
    rolldice()
    dice = rolldice()
    print(f"Player 2's dice rolled {dice}")

    players_current_squares[1] += dice

    if players_current_squares[1] == squares[0]['penalty'] or players_current_squares[1] == squares[1]['penalty']:
        players_current_squares[1] -= 10
        print(f'player 2 stepped on a penalty square. Player 2 is currently in square {players_current_squares[1]}')
    elif players_current_squares[1] == squares[0]['reward'] or players_current_squares[1] == squares[1]['reward']:
        players_current_squares[1] += 10
        print(f'player 2 stepped on a reward square. Player 2 is currently in square {players_current_squares[1]}')
    elif players_current_squares[1] >= 100:
        print(f'player 2 is currently in square {players_current_squares[1]}')
        print('player 2 won')
        break
    else:
        print(f'player 2 is currently in square {players_current_squares[1]}')
