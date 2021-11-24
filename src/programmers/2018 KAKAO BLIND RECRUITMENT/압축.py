# https://programmers.co.kr/learn/courses/30/lessons/17684
# 2018 KAKAO BLIND RECRUITMENT [3차] 압축

def solution(msg):
    answer = []
    msg_dict = {chr(i+64): i for i in range(1, 27)}

    start = 0
    end = start + 1
    while end < len(msg) + 1:
        if msg[start:end] not in msg_dict:
            answer.append(msg_dict[msg[start:end-1]])
            msg_dict[msg[start:end]] = len(msg_dict) + 1
            start = end - 1
            end = start + 1
        else:
            if end == len(msg):
                answer.append(msg_dict[msg[start:end]])
                break
            end += 1

    return answer


if __name__ == '__main__':
    solution("KAKAO")
    solution("TOBEORNOTTOBEORTOBEORNOT")
    solution("ABABABABABABABAB")
