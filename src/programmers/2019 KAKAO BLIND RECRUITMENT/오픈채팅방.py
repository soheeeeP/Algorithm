# https://programmers.co.kr/learn/courses/30/lessons/42888
# 2019 KAKAO BLIND RECRUITMENT 오픈채팅방

def solution(record):
    user = {}
    room = []
    message = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}

    for r in record:
        info = r.split()
        status, uid = info[0], info[1]
        if status in ["Enter", "Change"]:
            user[uid] = info[2]

    answer = []
    for r in record:
        info = r.split()
        status, uid = info[0], info[1]
        if status in message.keys():
            answer.append(f'{user[uid]}{message[status]}')

    return answer


if __name__ == '__main__':
    solution(
        ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"])
