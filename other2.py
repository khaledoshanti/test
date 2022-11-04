import random
def mydice():
    return random.randint(1, 6)

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

players_current_squares = [0, 0]



while players_current_squares[0] < 100 and players_current_squares[1] < 100:
    mydice()
    number = mydice()
    print('the dice rolled', number)
    players_current_squares[0] += number
        
    if players_current_squares[0] == squares[0]["penalty"] or players_current_squares[0] == squares[1]["penalty"]:
        players_current_squares[0] -= 10
        print("player 1 landed in a penalty box; -10. player 1 is in ", players_current_squares[0])
    elif players_current_squares[0] == squares[0]["reward"] or players_current_squares[0] == squares[1]["reward"]:
        players_current_squares[0] += 10
        print("player 1 landed in a reward box; +10. player 1 is in ", players_current_squares[0])
    else:
        print('player 1 is in', players_current_squares[0])

    if players_current_squares[0] >= 100:
        print("player 1 is the winner")
        break

    mydice()
    number = mydice()
    players_current_squares[1] += number
    print('the dice rolled', number)
    players_current_squares[1] += number
        
    if players_current_squares[1] == squares[0]["penalty"] or players_current_squares[1] == squares[1]["penalty"]:
        players_current_squares[1] -= 10
        print("player 2 landed in a penalty box; -10. player 2 is in ", players_current_squares[1])
    elif players_current_squares[1] == squares[0]["reward"] or players_current_squares[1] == squares[1]["reward"]:
        players_current_squares[1] += 10
        print("player 2 landed in a reward box; +10. player 2 is in ", players_current_squares[2])
    else:
        print('player 2 is in', players_current_squares[1])
    
    
    if players_current_squares[1] >= 100:
        print('player 2 is in', players_current_squares[1])
        print("player 2 is the winner")
        break
