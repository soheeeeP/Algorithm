n = int(input())
data = [i for i in map(int, input().split())]

answer = 0

while len(data) > 1:
    # 최대의 레벨값을 가지는 card를 선택
    card = max(data)
    idx = data.index(card)

    left = data[idx - 1] if idx > 0 else 100001
    right = data[idx + 1] if idx < len(data) - 1 else 100001

    # 왼쪽과 오른쪽 중 더 작은 레벨값을 카지는 카드를 선택하여 흡수
    if left < right:
        new_card_value = left
        new_card_idx = idx - 1
    else:
        new_card_value = right
        new_card_idx = idx + 1

    # goal값을 갱신하고, 흡수할 카드를 data에서 제거
    answer += new_card_value + card
    data.remove(new_card_value)

print(answer)
