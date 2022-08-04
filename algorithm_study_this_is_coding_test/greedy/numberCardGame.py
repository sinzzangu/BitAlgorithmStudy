

def solution(n, m, cards):
    answer = 0
    temp_list = list()
    cards_list = []
    for i in range(len(cards)):
        temp_list.append(cards[i])
        if len(temp_list) % m == 0:
            cards_list.append(temp_list)
            temp_list = []

    print(cards_list)
    
    smallest = -100
    for row in cards_list:
        row.sort()
        smallest_row = row[0]
        if smallest_row > smallest:
            smallest = smallest_row
    
    answer = smallest
    return answer
    
    
    
    
def main():
    n = 2
    m = 4
    cards = [7, 3, 1, 8, 3, 3, 3, 4]
    print(solution(n, m, cards))
    return 0


if __name__ == '__main__':
    main()