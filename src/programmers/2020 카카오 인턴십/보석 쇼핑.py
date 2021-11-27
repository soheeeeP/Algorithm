# https://programmers.co.kr/learn/courses/30/lessons/67258
# 2020 카카오 인턴십 보석 쇼핑

def solution(gems):
    start, end = 0, 0
    cnt = {gems[0]: 1}
    size = len(set(gems))
    answer = [0, len(gems)-1]

    while start < len(gems) and end < len(gems):
        if len(cnt) == size:
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
            cnt[gems[start]] -= 1
            if cnt[gems[start]] == 0:
                del cnt[gems[start]]
            start += 1
        else:
            end += 1
            if end == len(gems):
                break
            if gems[end] in cnt.keys():
                cnt[gems[end]] += 1
            else:
                cnt[gems[end]] = 1

    return [answer[0] + 1, answer[1] + 1]


if __name__ == '__main__':
    solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
    solution(["AA", "AB", "AC", "AA", "AC"])
    solution(["XYZ", "XYZ", "XYZ"])
    solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])
