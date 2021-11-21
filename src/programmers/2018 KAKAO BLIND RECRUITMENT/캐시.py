# https://programmers.co.kr/learn/courses/30/lessons/17680
# 2018 KAKAO BLIND RECRUITMENT [1차] 캐시

def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)

    answer = 0
    cache = []
    for c in cities:
        data = c.upper()
        if data in cache:
            answer += 1
            cache.remove(data)
            cache.append(data)
        else:
            answer += 5
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(data)

    return answer


if __name__ == '__main__':
    solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
    solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])
    solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])
    solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])
    solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"])
    solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
