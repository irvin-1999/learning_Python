'''
The 3Cups problem:We going to track the location of a ball under a cup as the cup move

Rori has a row of 3 opaque cups: one at the left(location),one at the middle(location),
one at the right(location).There's a ball under the cup at left.It's our job to keep track
of the location of the ball as Rori Swaps the location of the cups

Rori can make 3 types of swaps:
A:Swap the left & middle cups
B:swap the middle & right cups
C:swap the left & right cups
D:swap 

'''

swaps=str(input('Please Enter any Swap between A,B and C \n'))

ball_location=1

for swap_type in swaps:
    if swap_type =='A' and ball_location ==1:
        ball_location=2
    elif swap_type =='A' and ball_location==2:
        ball_location=1
    elif swap_type =='B' and ball_location==2:
        ball_location=2
    elif swap_type =='B' and ball_location==3:
        ball_location=2
    elif swap_type =='C' and ball_location==1:
        ball_location=3
    elif swap_type =='C' and ball_location==3:
        ball_location=1

print(ball_location)