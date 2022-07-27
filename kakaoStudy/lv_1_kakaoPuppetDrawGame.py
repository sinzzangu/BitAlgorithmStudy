
import numpy as np
def solution(board, moves):
    answer = 0
    basket = list()
    real_moves = [i - 1 for i in moves]
    # print(real_moves)
    
    for column_index in real_moves:
        for i in range(len(board)):
           
            print("looking at board:[" , i, "]", "[", column_index, "]", ":", board[i][column_index])
            if board[i][column_index] != 0:
                print()
                print("board:    move:", column_index)
                print("=" * 100)
                printBoard(board)
                print("found at board[" , i, "]", "[", column_index, "]", ":", board[i][column_index])
                basket.append(board[i][column_index])
                board[i][column_index] = 0
                print("basket: ", basket)
                if len(basket) > 1:
                    if basket[len(basket) - 1] == basket[len(basket) - 2]:
                        print("popping[" , len(basket) - 1, "]", "[", len(basket) - 2, "]")
                        answer += 2
                        basket.pop(len(basket) - 1)
                        basket.pop(len(basket) - 1)
                        print("basket: ", basket)
                break
            
             


    print(answer)
    return answer

def printBoard(board):
    for i in board:
        for j in i:
            print(j, end = " ")
        print()

def main():
    board = [[0,0,0,0,0],
             [0,0,1,0,3],
             [0,2,5,0,1],
             [4,2,4,4,2],
             [3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]
    solution(board,moves)
    return 0
    
    
if __name__ == '__main__':
    main()