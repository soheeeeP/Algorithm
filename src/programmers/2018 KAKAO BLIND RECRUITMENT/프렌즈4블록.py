# https://programmers.co.kr/learn/courses/30/lessons/17679
# 2018 KAKAO BLIND RECRUITMENT [1차] 프렌즈4블록

def solution(m, n, board):
    answer = 0
    _board = []
    for b in board:
        _board.append(list(b))

    while True:
        block = [[0] * n for _ in range(m)]     # 지울 블록 정보를 저장할 2차원 배열 생성
        for i in range(0, (m-1)):
            for j in range(0, (n-1)):
                kakao = _board[i][j]            # 기준 블록 설정
                if kakao and _board[i][j+1] == kakao and _board[i+1][j+1] == kakao and _board[i+1][j] == kakao:
                    # (i,j)에 위치한 블록이 비어있지 않고, 2*2범위에서 지워지는 조건을 만족하는지 확인
                    block[i][j] = block[i][j+1] = block[i+1][j+1] = block[i+1][j] = 1

        cnt = 0
        for i in range(m):
            for j in range(n):
                if block[i][j] == 1:
                    cnt += 1        # 지울 수 있는 블록의 갯수를 카운트

        if cnt == 0:
            break                   # 블록을 더 이상 지울 수 없다면, 종료

        answer += cnt               # 지운 블록의 갯수를 업데이트
        for j in range(n):
            for i in reversed(range(m)):
                if block[i][j] == 1:        # 지워야 하는 블록인지 확인한 뒤
                    loc = i
                    while block[loc][j] == 1 and loc >= 0:
                        loc -= 1            # 아래로 떨어뜨린 블록의 최초 위치를 탐색
                    if loc < 0:             # 더 이상 떨어뜨릴 블록이 없는 경우, 해당 위치의 블록을 바로 지워버림
                        _board[i][j] = ''
                    else:                   # 떨어뜨릴 블록이 존재하는 경우
                        _board[i][j] = _board[loc][j]   # 위의 블록을 아래로 떨어뜨리고
                        _board[loc][j] = ''             # 위쪽의 블록을 지워줌
                        block[loc][j] = 1               # 확인해야 하는 블록 목록에 추가

    return answer


if __name__ == '__main__':
    solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])
    solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])