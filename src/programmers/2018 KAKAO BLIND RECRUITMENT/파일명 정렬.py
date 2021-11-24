# https://programmers.co.kr/learn/courses/30/lessons/17686
# 2018 KAKAO BLIND RECRUITMENT [3차] 파일명 정렬

import re


def solution(files):
    answer = []
    num_start, num_end = re.compile(r'\d'), re.compile(r'\D')

    data = []
    for i, f in enumerate(files):
        num_start_idx = num_start.search(f).start()
        head = f[:num_start_idx]

        number = f[num_start_idx:]
        tail = num_end.search(number)
        if tail:
            num_end_idx = tail.start() + num_start_idx
        else:
            num_end_idx = len(f)

        data.append([i, head.upper(), int(f[num_start_idx:num_end_idx])])

    data.sort(key=lambda x: (x[1], x[2]))

    for i in range(len(data)):
        answer.append(files[data[i][0]])
    return answer


if __name__ == '__main__':
    solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
    solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])
