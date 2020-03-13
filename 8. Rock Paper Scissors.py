def player_input():
    p1_sign = ''
    p2_sign = ''
    while p1_sign != 'Rock' and p1_sign != 'Scissors' and p1_sign != 'Paper':
        p1_sign=input("Show Player1 Sign '[Rock/Scissors/Paper]'")
    while p2_sign != 'Rock' and p2_sign != 'Scissors' and p2_sign != 'Paper':
        p2_sign=input("Show Player2 Sign '[Rock/Scissors/Paper]'")
    return(p1_sign,p2_sign)

def win_check(p1_sign,p2_sign):
    if ((p1_sign=="Rock" and p2_sign=="Scissors")
            or(p1_sign=="Paper" and p2_sign=="Rock")
            or(p1_sign=="Scissors" and p2_sign=="Paper")):
        print('Player1 Wins the Game')


    if ((p2_sign == "Rock" and p1_sign == "Scissors")
            or (p2_sign == "Paper" and p1_sign == "Rock")
            or (p2_sign == "Scissors" and p1_sign == "Paper")):
        print('Player2 Wins the Game')

def tie_check(p1_sign,p2_sign):
    if p1_sign==p2_sign:
        replay=input('Game is in Tie.\nAre you want to replay the Game Again : (Y/N)')
        return replay

while True:
    print('Welcome to Rock Paper Scissors Game')
    p1,p2=player_input()
    win_check(p1,p2)
    replay_again = tie_check(p1,p2)
    if replay_again=='N':
        break