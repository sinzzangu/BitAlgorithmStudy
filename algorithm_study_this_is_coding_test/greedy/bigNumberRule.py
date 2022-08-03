from math import remainder
import time
def solution(n, m, k, list):
    str_list = map(int, list.split())
    # print(str_list)
    sorted_list = sorted(str_list, reverse = True)
    times_to_add = m // (k + 1)
    num_max =  k * sorted_list[0] + sorted_list[1]
    remainder = m % (k + 1)
    
    result = times_to_add * num_max + sorted_list[0] * remainder
    print(result)
    
        
    
    
    
    
def main():
    n = 5
    m = 8
    k = 3
    list = ('2 4 5 4 6')
    # s = '12345'
    solution(n, m, k, list)
    return 0


if __name__ == '__main__':
    main()