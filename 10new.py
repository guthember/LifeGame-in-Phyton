def live( state ):
    ## create new state
    sizeSpace = len(state)
    newState = []
    for i in range(0,sizeSpace):
        newState.append([])
        for j in range(0, sizeSpace):
            newState[i].append(0)

    ## without the last rows and lines
    for i in range(0,sizeSpace - 1):
        for j in range(0,sizeSpace - 1):
            howMany = 0
            ##print(state[i][j],end=' ')
            
            for si in range(-1,2):
                for ri in range(-1,2):
                    if i+si >= 0 and j+ri >= 0 and i+si < sizeSpace and j+ri < sizeSpace :
                        if state[i+si][j+ri] == 1:
                            howMany += 1
            
            howMany -= state[i][j]
            if howMany > 3 or howMany < 2 :
                newState[i][j] = 0
            elif howMany == 3:
                newState[i][j] = 1
            else:
                newState[i][j] = state[i][j]
        
    return newState

def printState( state ):
    for st in state:
        for s in st: 
            if s == 0:
                print(' ',end=' ')
            else:  
                print('*',end=' ')
        print()

"""
 startLive = [
    [ 0,0,0,0,0,0],
    [ 0,0,0,0,0,0],
    [ 0,0,1,1,1,0],
    [ 0,1,1,1,0,0],
    [ 0,0,0,0,0,0],
    [ 0,0,0,0,0,0]
]
"""

startLive = []

with open('life.txt','r') as file:
    sor = file.readline().split()
    
    while sor:
        newArray = []
        for s in sor:
            newArray.append(int(s))
        startLive.append(newArray)
        sor = file.readline().split()
        


for i in range(0,4):
    printState(startLive)
    print('-'*10)
    startLive = live(startLive)
