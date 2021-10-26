def solution(k, dungeons):
    answer = 0
    dungeons.sort(key=lambda x: (x[0] - x[1], -x[1], x[0]), reverse=True)

    value = k
    for d in dungeons:
        if value >= d[0]:
            value -= d[1]
            answer += 1

    return answer

# def dfs(k, dungeons, visited, cnt, answer):
#     for i in range(len(dungeons)):
#         if visited[i] != 1 and dungeons[i][0] <= k:
#             visited[i] = 1
#             answer = dfs(k - dungeons[i][1], dungeons, visited, cnt + 1, answer)
#             visited[i] = 0
#
#     answer = max(answer, cnt)
#     return answer
#
#
# def solution(k, dungeons):
#     visited = [0 for i in range(len(dungeons))]
#     value = dfs(k, dungeons, visited, 0, 0)
#     print(value)
#     return value


if __name__ == "__main__":
    solution(80, [[80, 20], [50, 40], [30, 10]])
