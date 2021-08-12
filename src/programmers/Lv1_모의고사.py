# 불필요한 형변환을 피하자
# list의 index를 활용하여 접근하기
def solution(answers):
    answer = []

    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    len1 = len(s1)
    len2 = len(s2)
    len3 = len(s3)

    cnt = [0,0,0]

    for i in range(len(answers)):
        if answers[i] == s1[i % len1]:
            cnt[0] += 1
        if answers[i] == s2[i % len2]:
            cnt[1] += 1
        if answers[i] == s3[i % len3]:
            cnt[2] += 1

    num = max(cnt)
    for i in range(len(cnt)):
        if cnt[i] >= num:
            answer.append(i+1)

    return answer


if __name__ == "__main__":
    print(solution([1, 2, 3, 4, 5]))
    print(solution([1, 3, 2, 4, 2]))

