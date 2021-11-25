def solution(lines):
    time = []
    for l in lines:
        x = l.split(' ')
        hour, minute, sec = x[1].split(":")
        res_t = int(hour) * 60 * 60 + int(minute) * 60 + float(sec)
        process_t = float(x[2][:-1])
        time.append([res_t - process_t + 0.001, res_t])

    answer = 0
    for t in time:
        start, end = t[0], t[1]
        cnt_start, cnt_end = 0, 0
        for log in time:
            # 해당 log가 존재하는 구간에서 1초 내에 처리되는 처리량의 최댓값 구하기
            if start + 0.999 >= log[0] and start <= log[1]:
                cnt_start += 1
            if end + 0.999 >= log[0] and end <= log[1]:
                cnt_end += 1
        answer = max(answer, cnt_start, cnt_end)

    return answer

    # import math
    # 이렇게 하면 0.001초가 아닌 1초 단위로 구간을 나누게 된다 (최대 처리량을 구할 수 없음)
    # start = round(min(time, key=lambda x: x[0])[0], 3)
    # end = math.ceil(time[-1][1])
    # traffic = {i: 0 for i in range(start, end)}
    # for t in time:
    #     start_t, end_t = math.floor(t[0]), math.ceil(t[1])
    #     while start_t < end_t:
    #         traffic[start_t] += 1
    #         start_t += 1
    #
    # print(traffic.values())


if __name__ == '__main__':
    solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"])
    solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"])
    solution([
        "2016-09-15 20:59:57.421 0.351s",
        "2016-09-15 20:59:58.233 1.181s",
        "2016-09-15 20:59:58.299 0.8s",
        "2016-09-15 20:59:58.688 1.041s",
        "2016-09-15 20:59:59.591 1.412s",
        "2016-09-15 21:00:00.464 1.466s",
        "2016-09-15 21:00:00.741 1.581s",
        "2016-09-15 21:00:00.748 2.31s",
        "2016-09-15 21:00:00.966 0.381s",
        "2016-09-15 21:00:02.066 2.62s"
    ])
