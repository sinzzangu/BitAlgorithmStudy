
from pandas import isnull


def solution(dartResult):
    answer = 0
    index = 0
    eachDartResults = []
    scores = []
    
    for i in range(len(dartResult)):
        
        if dartResult[i] == '0':
            continue
        
        if dartResult[i].isdigit():
            index = i
            
        else:
            if not dartResult[i].isalpha():
                eachDartResults.append(dartResult[index: i + 1])
                index = i + 1
        
            else:
                if i == len(dartResult) - 1 or dartResult[i + 1].isdigit():
                    eachDartResults.append(dartResult[index: i + 1])
                    index = i + 1
            
    print(eachDartResults)
    
    for i in range(len(eachDartResults)):
        totalPoints = 0
        points = int(eachDartResults[i][0])
        if(eachDartResults[i][1] == '0'):
            points = 10
            
            
        if not eachDartResults[i][len(eachDartResults[i]) - 1].isalpha():
            if eachDartResults[i][-2:-1] == 'D':
                totalPoints = points * points
            elif eachDartResults[i][-2:-1] == 'T':
                totalPoints = points * points * points
            else:
                totalPoints = points
            
            if eachDartResults[i][-1:] == '*':
                if i == 0:
                    totalPoints = totalPoints * 2
                    scores.append(totalPoints)
                else:
                    scores[i - 1] = scores[i - 1] * 2
                    totalPoints = totalPoints * 2
                    scores.append(totalPoints)
            elif eachDartResults[i][-1:] == '#':
                scores.append(totalPoints * -1)
        
        else:
            if eachDartResults[i][-1:] == 'D':
                totalPoints = points * points
            elif eachDartResults[i][-1:] == 'T':
                totalPoints = points * points * points
            else:
                totalPoints = points
            
            scores.append(totalPoints)
            

    for score in scores: 
        answer = score + answer
    
    return answer

def main():
    dartResult = "1D2S#10S"
    solution(dartResult)
    return 0
    
if __name__ == '__main__':
    main()