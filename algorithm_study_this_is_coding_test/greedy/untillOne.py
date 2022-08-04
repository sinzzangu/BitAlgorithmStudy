def solution(n, k):
    answer = 0
    
    while True:
        if n == 1:
            break
        elif n % k == 0:
            n = n // k
            answer += 1
        else:
            n -= 1
            answer += 1
    
    return answer

def main():
    n = 25
    k = 3
    print(solution(n, k))
    return 0


if __name__ == '__main__':
    main()