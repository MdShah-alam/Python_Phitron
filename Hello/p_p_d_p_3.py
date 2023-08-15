player_1=input('player-1 : ')
player_2=input('player-2 : ')

if (player_1=='Rock' or player_2=="Rock" ) and (player_1=='Scissor' or player_2=="Scissor"):
    if player_1=='Rock':
        print('Player 1 is the winner')
    else :
        print('Player 2 is the winner')
elif (player_1=='Paper' or player_2=='Paper' ) or (player_1=='Scissor' and player_2=='Scissor'):
    if player_1=='Scissor':
        print('Player 1 is the winner')
    else :
        print('Player 2 is the winner')
else:
    if player_1=='Paper':
        print('Player 1 is the winner')
    else :
        print('Player 2 is the winner')
