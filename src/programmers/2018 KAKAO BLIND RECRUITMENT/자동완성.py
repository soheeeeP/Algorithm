# https://programmers.co.kr/learn/courses/30/lessons/17685
# 2018 KAKAO BLIND RECRUITMENT [3차] 자동완성 (시간초과, 정확성 68.2)

def solution(words):
    answer = 0

    for w in words:
        idx = 0
        while idx < len(w):
            idx += 1
            cnt = 0
            flag = True
            for search_w in words:
                if w == search_w:
                    continue
                if w[:idx] == search_w[:idx]:
                    flag = False
                    break
            if flag:
                break
        answer += idx

    print(answer)
    return answer


if __name__ == '__main__':
    solution(["go", "gone", "guild"])
    solution(["abc", "def", "ghi", "jklm"])
    solution(["word", "war", "warrior", "world"])
