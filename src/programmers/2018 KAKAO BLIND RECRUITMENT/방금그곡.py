# https://programmers.co.kr/learn/courses/30/lessons/17683
# 2018 KAKAO BLIND RECRUITMENT [3차] 방금그곡

def get_note(data):
    m = []
    i = 0
    while True:
        if i >= len(data) - 1:  break
        if data[i] == "#":
            continue
        if data[i + 1] == "#":
            m.append(data[i:i + 2])
            i += 2
        else:
            m.append(data[i])
            i += 1

    if i == len(data) - 1:
        m.append(data[len(data) - 1])
    return m


def solution(m, musicinfos):
    answer = []
    melody = get_note(m)

    for x in musicinfos:
        start, end, title, info = x.split(',')

        start = int(start[0:2]) * 60 + int(start[3:])
        end = int(end[0:2]) * 60 + int(end[3:])
        play_time = end - start

        sample = get_note(info)
        song = []
        for t in range(play_time):
            song.append(sample[t % len(sample)])

        idx = 0
        while idx < len(song):
            # 같은 음 발견
            if song[idx] == melody[0]:
                # 카운트용 변수 설정
                cnt = 0
                for i in range(len(melody)):
                    if (i + idx) >= len(song):
                        break
                    if song[idx + i] != melody[i]:  # 다른 음이 나타나면 break
                        break
                    cnt += 1  # 동일한 음 갯수를 센다

                if cnt == len(melody):  # 동일한 멜로디 발견!
                    answer.append([play_time, title])
                    break
                else:
                    idx += cnt  # 동일한 멜로디가 아니다.. 하면 탐색할 다음 위치 설정
            else:
                idx += 1

    if len(answer) == 0:
        return '(None)'

    answer.sort(key=lambda y: y[0], reverse=True)
    return answer[0][1]


if __name__ == '__main__':
    solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])
    solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])
    solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])
