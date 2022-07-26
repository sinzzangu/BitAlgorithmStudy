def solution(N, stages):
    answer = []
    
    # stuck_users_per_stage = [0 for i in range(N + 1)]
    # failure_rates = []
    totalUserCount = len(stages)
    failure_rates = dict()
    
    for i in range(1, N + 1):
        stuck_users = stages.count(i)
        if stuck_users == 0:
            failure_rate = 0
            totalUserCount -= stuck_users
            failure_rates[i] = failure_rate
        else:        
            failure_rate = stuck_users / totalUserCount
            totalUserCount -= stuck_users
            failure_rates[i] = failure_rate
        
    # print("failure rates: ", failure_rates)
    failure_rates = sorted(failure_rates.items(), key = lambda item: item[1], reverse = True)
    # print("failure rates: ", failure_rates)
    
    answer = [failure_rates[i][0] for i in range(N)]
   
    
    return answer

def main():
    stages = [2, 1, 2, 6, 2, 4, 3, 3]
    n = 5
    solution(n, stages)
    return 0
    
    
if __name__ == '__main__':
    main()