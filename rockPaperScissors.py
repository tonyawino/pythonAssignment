# Tony Awino
# Date: May 4th, 2018 
# homework2.1.py

#A game of rock paper scissors for 2 players

a=raw_input('Player 1?').lower()
while (a!='rock' and a!='paper' and a!='scissors'):
    print a, 'is not a valid input, enter "rock", "paper", or "scissors"'
    a=raw_input('Player 1?').lower()
b=raw_input('Playe r2?').lower()
while (b!='rock' and b!='paper' and b!='scissors'):
    print b, 'is not a valid input, enter "rock", "paper", or "scissors"'
    b=raw_input('Player 2?').lower()
if (a==b):
    print 'Tie'
elif ((a=='rock' and b=='scissors') or (a=='paper' and b=='rock') or (a=='rock' and b=='scissors')):
    print 'Player 1 wins'
else:
    print 'player 2 wins'