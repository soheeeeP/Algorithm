def solution(price, money, count):
    value = price * count * (count+1) / 2
    if money >= value:
        return 0
    return value-money
