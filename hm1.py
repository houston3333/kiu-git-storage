def solution(string):
    if len(string) % 2 != 0: 
        string += '_'
    return [string[i:i+2] for i in range(0, len(string), 2)]
