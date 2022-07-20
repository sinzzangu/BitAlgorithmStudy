from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    
    report_dict = defaultdict(set)
    
    # split report list into dictionary
    for names in report:
        names_list = names.split(" ")
        report_dict[names_list[1]].add(names_list[0])
          
            
    # print(report_dict)
    
    mail_receive_list = list()
    # find people who 신고 2번 이상
    for reporters in report_dict.values():
        if len(reporters) >= k:
            while len(reporters) != 0:
                mail_receive_list.append(reporters.pop())
    
    # print(mail_receive_list)
                
    # id_list 기준으로 카운트 해줘서 더해준다
    for id in id_list:
        answer.append(mail_receive_list.count(id))
    
    print(answer)
    
    return answer



def main():
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    solution(id_list, report, 2)
    return 0
    
    
if __name__ == '__main__':
    main()