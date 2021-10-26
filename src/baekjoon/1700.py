n, k = map(int, input().split())
data = [x for x in map(int, input().split())]

"""
    data_set: 전기 용품의 이름을 저장한 set
    idx: 전기 용품 사용 순서 index
    usage: 전기 용품이 처음으로 사용되게 되는 순서 index를 저장한 dict
    _usage: 사용 우선 순위가 낮은(가장 먼저 제거할) 전기 용품 순으로 정렬한 list
    port: 멀티탭에서 플러그가 꽂힌 위치를 저장한 set
"""

data_set = set(data)
idx = 1
usage = {x: data[idx:].index(x) if x in data[idx:] else 100 for x in data_set}
_usage = [val[0] for val in sorted(usage.items(), key=lambda x:x[1], reverse=True)]

answer = 0
port = set()

for x in data:
    if x not in port and len(port) < n:
        port.add(x)
    elif x not in port and len(port) == n:
        for u in _usage:
            if u in port:
                port.remove(u)
                port.add(x)
                answer += 1
                break
    idx += 1
    usage = {x: data[idx:].index(x) if x in data[idx:] else 100 for x in data_set}
    _usage = [val[0] for val in sorted(usage.items(), key=lambda x: x[1], reverse=True)]

print(answer)
