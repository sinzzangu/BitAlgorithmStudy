import math

from numpy import number 


def solution(input):
    answer = list()
    list_by_index = list()
    length = 0
    for tmp_list in input:
        tmp = tmp_list.split()
        # ones.append(tmp.pop(0)
        list_by_index.append(tmp)
        length += len(tmp)
        
    print(length)
    number_of_arrays = int(math.sqrt(length))
    # print(number_of_arrays)
    # print(list_by_index)
    
    list_by_index.reverse()
    # ones = [num.pop(0) for num in list_by_index]
    # print('ones:', ones)
    # print(result)
    # print(list_by_index)
    
    for i in range(number_of_arrays):
        # print('i:', i)
        num_final = ''
        for j in range(i + 1):
            print('j:',j , "  ", end = '')
            if len(list_by_index[j]) % 2 == 1:
                num = list_by_index[j].pop(0)
                num_final += num
            else:
                num = list_by_index[j].pop(1)
                num1 = list_by_index[j].pop(0)
                num_final += num + " "+ num1 + " "
            print('num_final:', num_final)
            
        answer.append(num_final)
        print('=' * 40)
    return answer



def main():
    wise = False
    input = ['1', '2 3 4', '5 6 7 8 9', '10 11 12 13 14 15 16']
    if(wise ==True):
        print(solution(input))
    else:
        print(solution(solution(input)))
    # print(solution(input))
    
    
    

if __name__=="__main__":
    main()