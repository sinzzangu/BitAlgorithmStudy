def solution(n, arr1, arr2):
    answer = []
    
    map1 = ""
    map2 = ""
    decipheredRow = ""
    for row in arr1:
        decipheredRow = toBinary(row)
        while len(decipheredRow) != n:
            decipheredRow = '0' + decipheredRow
        map1 += (decipheredRow)

    for row in arr2:
        decipheredRow = toBinary(row)
        while len(decipheredRow) != n:
            decipheredRow = '0' + decipheredRow
        map2+=(decipheredRow)
    row = ""
    for i in range(len(map1)):
        if map1[i] == '0' and map2[i] == '0':
            #print("MATCHED AT INDEX:", i , ' map1:', map1[i], ' map2:',map2[i])
            row += " "
        else: 
            row += "#"
        
       #  print('index: ', i , ' map1:', map1[i], ' map2:',map2[i], 'row: ', row)
        if len(row) % n == 0:
            answer.append(row)
            row = ""
        # print('index: ', i , ' map1:', map1[i], ' map2:',map2[i], 'row: ', row)
    
    #print()
    #print(answer)
    return answer

def toBinary(num):
    if num == 0:
        return "" 
    else:
        return toBinary(num//2) + str(num%2) 


def main():
    n = 6
    arr1 = [46, 33, 33, 22, 31, 50]
    arr2 = [27, 56, 19, 14, 14, 10]
    
    
    solution(n, arr1, arr2)
    return 0
    
    
if __name__ == '__main__':
    main()