def solution(s):
    answer = 0
    answer = len(s)
    
    for pattern_length in range(1, len(s)//2+1):
        count = 1
        temp_sentence = ""
        for index in range(0, len(s), pattern_length):
            prev_s = s[index:index+pattern_length]
            next_s = s[index+pattern_length:index+(2*pattern_length)]
            if prev_s == next_s:
                count+=1
            else:
                if count != 1:
                    temp_sentence += str(count)+prev_s
                else:
                    temp_sentence += prev_s
                count = 1
        # print(temp_sentence, len(temp_sentence))
        if answer > len(temp_sentence):
            answer = len(temp_sentence)
    print(answer)
    return answer
                



def main():
    s = "aabbaccc"
    # s = '12345'
    solution(s)
    return 0
    
    
if __name__ == '__main__':
    main()
