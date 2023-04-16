import random
human = 0
robot = 0
while human < 3 and robot < 3:
    print('choose one of these: stone, scissors, paper ')
    a = input()
    if a != 'stone' and a != 'scissors' and a != 'paper':
        print('invalid input')
    else:
        roll = random.choice(['stone', 'scissors', 'paper'])
        print(roll)
        if a == roll:
            print('draw')
        elif a == 'stone' and roll == 'scissors' or a == 'scissors' and roll == 'paper' or a == 'paper' and roll == 'stone':
            human += 1
            print('You won!')
        else:
            robot += 1
            print('Robot won!')
if human > robot:
    print('You won the game')
else:
    print('Robot won the game')
print(f'final score: {human} - {robot}')