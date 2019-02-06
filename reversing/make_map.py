
f = open('maze.txt')
maze = f.read().strip()

def make_map():
    maze_map = []
    scrambled = ''
    for i in range(len(maze)):
        if maze[i] != '~':
            scrambled += maze[i]
            maze_map.append(str(i))
    return maze_map

def can_reach(node, maze):
    n = int(node) * 101
    can_reach = []
    for i in maze:
        hop = int(i)-n
        if hop >= 0:
            can_reach.append(str(hop))
    return can_reach

def make_graph(start, end):
    m = make_map()
    graph = {}
    lst = [start]
    while end not in graph.keys() and len(lst) > 0:
        n = lst.pop()
        while n in graph.keys():
            n = lst.pop()
        reach = can_reach(n,m)
        graph[n] = reach
        lst += reach
        lst = list(set(lst))
    return graph


def get_path(room_input):
    try:
        rooms = room_input.split(',')
        out = ''
        for i in range(len(rooms)-1):
            room = int(rooms[i])
            nroom = int(rooms[i+1])
            r = room * 4
            r = r + room
            r = r + (r * 4)
            r = r * 4
            r = r + room
            r = r + (nroom)
            print(r)
            #print(maze[r])
            out += maze[r]
        return out
    except:
        return '~'


if __name__ == '__main__':
    start_room = input('Give starting room!!! ')
    end_room = input('Give end room!!! ')
    possible_path = get_possible_path(start_room, end_room)
