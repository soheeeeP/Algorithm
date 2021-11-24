import re
import math


def solution(dartResult):
    regex = re.compile(r'[SDT]')

    stack = []
    dart = {'S': 1, 'D': 2, 'T': 3}

    idx = 0
    while idx < len(dartResult):
        if dartResult[idx] == "*":
            if idx+1 < len(dartResult) and dartResult[idx+1] == "*":
                op_num = 4
                idx += 2
            elif idx+1 < len(dartResult) and dartResult[idx+1] == "#":
                op_num = -2
                idx += 2
            else:
                op_num = 2
                idx += 1

            cnt = 0
            option = []
            while stack and cnt < 2:
                option.append(stack.pop())
                cnt += 1

            for o in reversed(option):
                stack.append(o*op_num)

        elif dartResult[idx] == "#":
            option = stack.pop()
            stack.append((-1)*option)
            idx += 1

        else:
            score_end_idx = regex.search(dartResult[idx:]).end()
            num, expo = int(dartResult[idx:idx + score_end_idx - 1]), dart[dartResult[idx + score_end_idx - 1]]
            stack.append(int(math.pow(num, expo)))
            idx += score_end_idx

    answer = sum(stack)
    return answer


if __name__ == '__main__':
    solution("1S2D*3T")
    solution("1D2S#10S")
    solution("1D2S0T")
    solution("1S*2T*3S")
    solution("1D#2S*3S")
    solution("1T2D3D#")
    solution("1S2D*3T*")
    solution("1S2D3T*")
