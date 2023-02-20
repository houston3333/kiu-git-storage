state = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

def noneCounter():
    steps = 0
    for i in range(3):
        steps += state[i].count(None)
    return steps


def victory_check():   
    if state[0][0]==state[1][1]==state[2][2] != None or state[2][0]==state[1][1]==state[0][2] != None:
        return True    
            
    for i in range(3):
        if state[i][0]==state[i][1]==state[i][2] != None or state[0][i]==state[1][i]==state[2][i] != None:
            return True