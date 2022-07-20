from pip import main


def solution(new_id):
    answer = ''
    
    # step 1: to lower case
    new_id = new_id.lower()
    # print("step 1")
    # print(new_id)

    for i in new_id:
       if i.isalpha() or i.isdigit() or i in ['-', '_', '.']:
            answer += i
    
    # print("step 2")
    # print(answer)
    # step 3 change ... or .. to .
    while '..' in answer:
        answer = answer.replace('..', '.')
        
    # step 4 if start with ., remove .
    if answer[0] == ".":
        answer = answer[1:]
    elif answer[len(answer) - 1] == '.':
        answer = answer[:len(answer) - 1]
    elif answer[0] == "." and answer[len(answer) - 1] == ".":
        answer = answer[1:len(answer) - 1]   
        
    # print(answer)
    
    # step5 빈 문자열이라면 a 추가해줍니다 
    answer = 'a' if len(answer) == 0 else answer[:15]
    
    # step 6 if last is . delete
    if answer[-1] == '.':
        answer = answer[:-1]
            
    # step 7 if length of id is equal or less than 2, copy the last charactor or new id until the length of new id is three
    while len(answer) < 3:
            answer += answer[-1]
    
    print(answer)
    return answer


def main():
    s = "abcdefghijklmn.p"
    print(len(s))
    solution(s)
    return 0
    
    
if __name__ == '__main__':
    main()