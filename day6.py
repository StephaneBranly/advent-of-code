from fileinput import input
import os, math

agent = {
    'position': None,
    'direction': None
}
directions = {
    'v': {
        'vector': (1,0),
        'turn': '<',
        'marker': '|'
    },
    '<': {
        'vector': (0,-1),
        'turn': '^',
        'marker': '-'
    },
    '^': {
        'vector': (-1,0),
        'turn': '>',
        'marker': '|'
    },
    '>': {
        'vector': (0,1),
        'turn': 'v',
        'marker': '-'
    }
}
map, i = [], 1
for line in input():
    line = line.replace('\n','')
    for symbol in directions.keys():
        if symbol in line:
            agent['direction'], agent['position'] = symbol, (i, line.index(symbol))
    map.append(line)
    i+=1
continuer, count = True, 1
while continuer:
    x, y = agent['position']
    next_y, next_x = y + directions[agent['direction']]['vector'][0], x + directions[agent['direction']]['vector'][1]
    if next_y < 0 or next_x < 0 or next_y >= len(map) or next_x >= len(map[0]):
        continuer = False
    elif map[next_y][next_x] == '#':
        map[y]= map[y][:x] + '+' + map[next_y][x + 1:]
        agent['direction'] = directions[agent['direction']]['turn']
    else:
        if map[next_y][next_x] == '.':
            map[next_y] = map[next_y][:next_x] + directions[agent['direction']]['marker'] + map[next_y][next_x + 1:]
            count += 1
        agent['position'] = (next_y, next_x)
    
    
print('---')
[print(l) for l in map]
print(agent, count)