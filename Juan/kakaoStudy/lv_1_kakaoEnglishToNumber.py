def solution(s):
    answer = ""
    number_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    
    for number_alpha in number_dict:
        s = s.replace(number_alpha, str(number_dict[number_alpha]))

    answer = s
    return int(answer)



def main():
    s = "one4seveneight"
    solution(s)
    return 0
    
    
if __name__ == '__main__':
    main()