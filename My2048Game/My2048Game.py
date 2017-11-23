import msvcrt
import os
import random
map = [[0,0,0,0],\
       [0,0,0,0],\
       [0,0,0,0],\
       [0,0,0,0]]
map1 =[[0,0,0,0],\
       [0,0,0,0],\
       [0,0,0,0],\
       [0,0,0,0]]
mapcopy =[[0,0,0,0],\
       [0,0,0,0],\
       [0,0,0,0],\
       [0,0,0,0]]


def geteveryboxlen():#获取每个坐标的长度
    lenth =[[3,3,3,3],\
       [3,3,3,3],\
       [3,3,3,3],\
       [3,3,3,3]]
    for y in range(4):
        for x in range(4):
            if map[y][x] > 1000:
                lenth[y][x] = lenth[y][x] - 3
            elif map[y][x] > 100 and map[y][x] < 1000:
                lenth[y][x] = lenth[y][x] - 2
            elif map[y][x] > 10 and map[y][x] < 100:
                lenth[y][x] = lenth[y][x] - 2
def printmap():   #打印游戏地图
    space =[[" "," "," "," "],\
       [" "," "," "," "],\
       [" "," "," "," "],\
       [" "," "," "," "]]
    i = os.system('cls')
    lenth =[[3,3,3,3],\
       [3,3,3,3],\
       [3,3,3,3],\
       [3,3,3,3]]
    for y in range(4):
        for x in range(4):
            if map[y][x] > 1000:
                lenth[y][x] = lenth[y][x] - 3
            elif map[y][x] > 100 and map[y][x] < 1000:
                lenth[y][x] = lenth[y][x] - 2
            elif map[y][x] > 10 and map[y][x] < 100:
                lenth[y][x] = lenth[y][x] - 1
    for y in range(4):
        for x in range(4):
            if map[y][x] == 0:
                map[y][x] == 1
    for empty in range(4):
        print(" ")
    for x in range(4):
        print("                       ",end = "      ")
        for y in range(4):
            for time in range(lenth[x][y]):
                space[x][y] = space[x][y] + " "
            print(space[x][y] + str(map[x][y]),end="    ")
        print("\n")
        print("\n")
    
def getkey(): #获取按键信息
    while True:
        key = msvcrt.getch()
        if key in[ b's',b'w',b'a',b'd']:
            #print(key)
            break        
    return key
def addnum(): #增加数字
    zerobox=[]
    for y in range(4):
        for x in range(4):
            if map[y][x] == 0:
                zerobox.append([y,x])
    thisboxwilladdnum = random.choice(zerobox)
    map[thisboxwilladdnum[0]][thisboxwilladdnum[1]] = random.choice([2,4])
def fristadd():  #第一次随机添加元素2和4
    for time in range(2):
        addnum()
def moveleft(): #向左移动
    clearall0()
    for y in range(4):
        if len(map[y]) == 2:
            if map[y][0] == map[y][1]:
                map[y][0] = map[y][0]*2
                del map[y][1]
        elif len(map[y]) ==3:
            if map[y][0] == map[y][1] or map[y][0] == map[y][1] == map[y][2]:
                map[y][0] = map[y][0]*2
                del map[y][1]
            elif map[y][1] == map[y][2]:
                map[y][1] = map[y][1]*2
                del map[y][2]
        elif len(map[y]) == 4:
            if map[y][0] == map[y][1] and map[y][2] == map[y][3]:
                map[y][0] = map[y][0]*2
                map[y][2] = map[y][2]*2
                del map[y][1]
                del map[y][2]#注意这个地方就是要删2，容易误以为是3
            elif (map[y][0] == map[y][1] and map[y][2] != map[y][3]) or map[y][0] == map[y][1] == map[y][2]:
                map[y][0] = map[y][0]*2
                del map[y][1]
            elif (map[y][0] != map[y][1] and map[y][1] == map[y][2]) or (map[y][0] != map[y][1] and map[y][1] == map[y][2] == map[y][3]):
                map[y][1] = map[y][1]*2
                del map[y][2]
            elif map[y][2] == map[y][3]:
                map[y][2] = map[y][2]*2
                del map[y][3]
    add0()
def moveright(): #向右移动
    for y in range(4):
        map[y].reverse()
    moveleft()
    for y in range(4):
        map[y].reverse()
def moveup(): #向上移动
    bigchange()
    for y in range(4):
        for t in range(map1[y].count(0)):
            map1[y].remove(0)
    for y in range(4):
        if len(map1[y]) == 2:
            if map1[y][0] == map1[y][1]:
                map1[y][0] = map1[y][0]*2
                del map1[y][1]
        elif len(map1[y]) ==3:
            if map1[y][0] == map1[y][1] or map1[y][0] == map1[y][1] == map1[y][2]:
                map1[y][0] = map1[y][0]*2
                del map1[y][1]
            elif map1[y][1] == map1[y][2]:
                map1[y][1] = map1[y][1]*2
                del map1[y][2]
        elif len(map1[y]) == 4:
            if map1[y][0] == map1[y][1] and map1[y][2] == map1[y][3]:
                map1[y][0] = map1[y][0]*2
                map1[y][2] = map1[y][2]*2
                del map1[y][1]
                del map1[y][2]#注意这个地方就是要删2，容易误以为是3
            elif (map1[y][0] == map1[y][1] and map1[y][2] != map1[y][3]) or map1[y][0] == map1[y][1] == map1[y][2]:
                map1[y][0] = map1[y][0]*2
                del map1[y][1]
            elif (map1[y][0] != map1[y][1] and map1[y][1] == map1[y][2]) or (map1[y][0] != map1[y][1] and map1[y][1] == map1[y][2] == map1[y][3]):
                map1[y][1] = map1[y][1]*2
                del map1[y][2]
            elif map1[y][2] == map1[y][3]:
                map1[y][2] = map1[y][2]*2
                del map1[y][3]
    for y in range(4):
        for howmany in range(4 - len(map1[y])):
            map1[y].append(0)
    bigchangeback()
def movedown():
    bigchange()
    for y in range(4):
        map1[y].reverse()
    for y in range(4):
        for t in range(map1[y].count(0)):
            map1[y].remove(0)
    for y in range(4):
        if len(map1[y]) == 2:
            if map1[y][0] == map1[y][1]:
                map1[y][0] = map1[y][0]*2
                del map1[y][1]
        elif len(map1[y]) ==3:
            if map1[y][0] == map1[y][1] or map1[y][0] == map1[y][1] == map1[y][2]:
                map1[y][0] = map1[y][0]*2
                del map1[y][1]
            elif map1[y][1] == map1[y][2]:
                map1[y][1] = map1[y][1]*2
                del map1[y][2]
        elif len(map1[y]) == 4:
            if map1[y][0] == map1[y][1] and map1[y][2] == map1[y][3]:
                map1[y][0] = map1[y][0]*2
                map1[y][2] = map1[y][2]*2
                del map1[y][1]
                del map1[y][2]#注意这个地方就是要删2，容易误以为是3
            elif (map1[y][0] == map1[y][1] and map1[y][2] != map1[y][3]) or map1[y][0] == map1[y][1] == map1[y][2]:
                map1[y][0] = map1[y][0]*2
                del map1[y][1]
            elif (map1[y][0] != map1[y][1] and map1[y][1] == map1[y][2]) or (map1[y][0] != map1[y][1] and map1[y][1] == map1[y][2] == map1[y][3]):
                map1[y][1] = map1[y][1]*2
                del map1[y][2]
            elif map1[y][2] == map1[y][3]:
                map1[y][2] = map1[y][2]*2
                del map1[y][3]
    for y in range(4):
        for howmany in range(4 - len(map1[y])):
            map1[y].append(0)
    for y in range(4):
        map1[y].reverse()
    bigchangeback()
def clearall0():
    for y in range(4):
        for t in range(map[y].count(0)):
            map[y].remove(0)
def add0():
    for y in range(4):
        for howmany in range(4 - len(map[y])):
            map[y].append(0)
def bigchange():
    for y in range(4):
        for x in range(4):
            map1[x][y] = map[y][x]
def bigchangeback():
    for y in range(4):
        for x in range(4):
            map[x][y] = map1[y][x]    
def iswin():
    for y in range(4):
        for x in range(4):
            if map[y][x] == 2048:
                print("                 YOU WIN")
                break
def cannotadd():
    count = 0
    for x in range(4):
        for y in range(3):
            if map[x][y] == map[x][y+1]:
                count = count + 1
    for y in range(4):
        for x in range(3):
            if map[x][y] == map[x+1][y]:
                count = count + 1
    return count 
addnum()
addnum()
printmap()

while True:
    empty = 0
    for y in range(4):
        for x in range(4):
            mapcopy[y][x] = map[y][x]
    key = getkey()
    for y in range(4):
        for x in range(4):
            if map[y][x] == 2048:
                print("                 YOU WIN")
                break
            if map[y][x] == 0:
                empty = empty + 1
    if empty ==0 and cannotadd() == 0 :
        print("                 YOU ARE LOSER MOTHERFUCKER   ！！！")
        break
    if key == b'w':
        moveup()
        printmap()
    elif key == b's':
        movedown()
        printmap()
    elif key == b'a':
        moveleft()
        printmap()
    elif key == b'd':
        moveright()
        printmap()
    if mapcopy != map:
        addnum()
    printmap()
