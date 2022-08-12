def solution(n, directions):
    # grid_size = int(input())
    # moves = input().split()
    gridsize = n
    moves = directions.split()
    
    print("grid size:", n)
    print("moves:", moves)
    
    starting_point = (1,1)
    for move in moves:
        x,y = starting_point
        starting_point = action(x, y, move, n)
        print(starting_point)
    
    
    return starting_point

def action(x, y, move, n):
    if move == 'R':
        if y + 1 > n:
            return (x, y)
        else:
            return (x, y + 1)
    
    if move == 'L':
        if y - 1 < 1:
            return (x, y)
        else:
            return (x, y - 1)
    
    if move == 'U':
        if x -1 < 1:
            return (x, y)
        else:
            return (x - 1, y)
    
    if move == 'D':
        if x + 1 > n:
            return (x, y)
        else:
            return (x + 1, y)


def main():
    n = 5
    directions = "R R R U D D"
    print(solution(n, directions))
    

if __name__=="__main__":
    main()