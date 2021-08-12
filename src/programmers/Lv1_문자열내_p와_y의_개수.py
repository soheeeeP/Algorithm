def solution(s):
    answer = True

    s_list = list(s)
    cnt = [0, 0]
    for i in range(len(s_list)):
        if s_list[i] == 'p' or s_list[i] == 'P':
            cnt[0] += 1
        elif s_list[i] == 'y' or s_list[i] == 'Y':
            cnt[1] += 1
        else:
            continue

    num = max(cnt)
    if num == 0:
        return True

    if cnt[0] == cnt[1]:
        return True
    else:
        return False


if __name__ == "__main__":
    print(solution("pPoooyY"))
    print(solution("Pyy"))
