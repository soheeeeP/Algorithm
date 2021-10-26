import sys

T = int(input())

for t in range(T):
    n = int(input())
    data = []
    for i in range(n):
        data.append([j for j in map(int, sys.stdin.readline().split())])
    # 서류 순위를 기준으로 오름차순 정렬
    data.sort()

    answer = n
    # 면접 순위 기준값 설정
    standard = data[0][1]

    # 면접 순위 기준을 만족하는지 확인
    for i in range(1, n):
        # 만족하지 않는 경우 (서류/면접 순위가 모두 다른 지원자보다 떨어지는 경우), 합격자에서 제외
        if standard < data[i][1]:
            answer -= 1
        # 만족하는 경우, 면접 순위 기준값을 업데이트
        else:
            standard = data[i][1]
    print(answer)