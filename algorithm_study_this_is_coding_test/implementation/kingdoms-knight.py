def solution(position):
    starting_row = int(position[1])
    starting_column = ord(position[0]) - 96
    count = 0
    
    possible_moves = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
    for row, column in possible_moves:
        new_row = starting_row + row
        new_column = starting_column + column
        
        if new_row < 1 or new_row > 8 or new_column < 1 or new_column > 8:
            count+=1
    
    return 8 - count
def main():
    n = 5
    position = "e5"
    print(solution(position))
    

if __name__=="__main__":
    main()