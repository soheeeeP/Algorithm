def solution(n, arr1, arr2):
    answer = []
    maze1, maze2 = [], []
    map = {1: "#", 0: ' '}
    format_len = "%0"+str(n)+"d"

    for i in range(n):
        maze1.append(format_len % int(format(arr1[i], 'b')))
        maze2.append(format_len % int(format(arr2[i], 'b')))

    for x in range(n):
        data = ''
        for y in range(n):
            data += map[int(maze1[x][y]) or int(maze2[x][y])]
        answer.append(data)

    return answer


if __name__ == '__main__':
    solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
    solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10])
