board_size = int(input())
num_of_players = int(input())
num_of_snake = int(input())
stuff = {}
for _ in range(num_of_snake):
    answer = input().split()
    stuff[(str(answer[0]))+"-"+(str(answer[1]))]=([[int(answer[2]), int(answer[3])], 'S'])
num_of_ladd = int(input())
for _ in range(num_of_ladd):
    answer = input().split()
    stuff[(str(answer[0]))+"-"+(str(answer[1]))]=([[int(answer[2]), int(answer[3])], 'L'])
rolls = []
num_of_roll = int(input())
for _ in range(num_of_roll):
    x,y = input().split()
    rolls.append(int(x)+int(y))

position=[[0,1], [0,1]]
roller = 0
player=0
while roller!= len(rolls):
    
    if position[player][1] % 2 == 0:
        move = -1
    else:
        move = 1
    roll = rolls[roller]
    for j in range(roll):
        if position[player][1] != board_size and ((position[player][0]+move) > board_size or (position[player][0]+move)< 1):
            position[player][1] += 1
            move *= -1
        else:
            position[player][0] += move
        
        if position[player][0] == 0 and position[player][1] == board_size:
            break

    flag = True
    while flag == True:
        try:
            what_now = stuff[str(position[player][0])+"-"+str(position[player][1])]
            
            position[player][0]=what_now[0][0]
            position[player][1]=what_now[0][1]
        except:
            flag = False 
    
    flag = True
    for i in range(len(position)):
        if position[i] != [0,board_size]:
            flag=False
            break
    if flag == True:
        break

    player += 1
    player = player % num_of_players
    while position[player] == [0,board_size]:
        player += 1
        player = player % num_of_players
    
    roller+=1

for i in range(len(position)):
    print(i+1, end = ' ')
    if position [i] == [0,board_size]:
        print("winner")
    else:
        print (position[i][0], position[i][1])