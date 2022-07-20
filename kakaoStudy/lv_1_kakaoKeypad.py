from multiprocessing.connection import answer_challenge


def solution(numbers, hand):
    answer = ''
    
    left = "3,0"
    right = "3,2"
    
    #numbers_to_coordinates_dict = [["3,1"], ["0,0"], ["0,1"], ["0,2"], ["1,0"], ["1,1"], ["1,2"], ["2,0"], ["2,1"], ["2,2"]]
    numbers_to_coordinates_dict = ['3,1', '0,0', '0,1', '0,2', '1,0', '1,1', '1,2', '2,0', '2,1', '2,2']
 
    for number in numbers: 
        print("number: ", number)
        coordinate = numbers_to_coordinates_dict[number]
        print("coordinate: ", coordinate)
        if number in (1,4,7):
            left = coordinate
            answer += "L"
        elif number in (3, 6, 9):
            right = coordinate 
            answer += "R"
        else:
            if calculate_distance(left, coordinate) > calculate_distance(right, coordinate):
                right = coordinate
                answer += "R"
            elif calculate_distance(left, coordinate) < calculate_distance(right, coordinate):
                left = coordinate
                answer += "L"
            else:
                if hand[0] == 'r':
                    right = coordinate
                    answer += "R"
                else:
                    left = coordinate
                    answer += "L"
    return answer

        
def calculate_distance(hand, coordinate):
    hand_x, hand_y = hand.split(",")
    coordinate_x, coordinate_y = coordinate.split(",")
    
    return abs(int(hand_x) - int(coordinate_x)) + abs(int(hand_y) - int(coordinate_y))


    


def main():
    numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
    hand = "left"
    
    print(solution(numbers, hand))
    return 0
    
# "LRLLLRLLRRL"
if __name__ == '__main__':
    main()