n, m = map(int, input().split())

data = []
for i in range(n):
    data.append(input())

data.sort()

dna = ''
# n: 주어지는 문자열 갯수
# m: 문자열의 길이
for y in range(m):
    value = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for x in range(n):
        acgt = data[x][y]
        value[acgt] += 1
    dna += max(value, key=value.get)

answer = 0
for x in range(n):
    for y in range(m):
        if dna[y] != data[x][y]:
            answer += 1

print(dna)
print(answer)
