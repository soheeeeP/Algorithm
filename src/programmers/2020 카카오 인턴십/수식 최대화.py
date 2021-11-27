# https://programmers.co.kr/learn/courses/30/lessons/67257
# 2020 카카오 인턴십: 수식 최대화

# 문자열을 연산자와 피연산자로 분리, 중위 표기법 stack과 연산자 집합을 반환
def str_to_prefix(exp):
    stack = []
    op = set()

    import re
    idx = 0
    for i, val in enumerate(exp):
        if re.match(r'\D', val):
            stack.append(exp[idx:i])
            stack.append(val)
            op.add(val)
            idx = i + 1

    stack.append(exp[idx:])
    return stack, op


# 중위 표기법을 후위 표기법으로 변환
def prefix_to_postfix(prior, exp):
    stack = []
    op = []
    for e in exp:
        if e.isdigit():
            stack.append(e)
        else:
            while op and prior[e] <= prior[op[-1]]:
                stack.append(op.pop())
            op.append(e)
    while op:
        stack.append(op.pop())

    return stack


# 후위 표기법 연산
def get_postfix_sum(exp):
    ans = []
    for e in exp:
        if e.isdigit():
            ans.append(e)
        else:
            b = ans.pop()
            a = ans.pop()
            if e == '*':
                ans.append(int(a) * int(b))
            elif e == '+':
                ans.append(int(a) + int(b))
            elif e == '-':
                ans.append(int(a) - int(b))

    return abs(ans[0])


def solution(expression):
    _expression, op = str_to_prefix(expression)

    # 연산자 우선순위 설정
    import itertools
    priority = []
    for it in itertools.permutations(op):
        priority.append({val: i for i, val in enumerate(it)})

    answer = 0
    for p in priority:
        stack = prefix_to_postfix(p, _expression)
        answer = max(answer, get_postfix_sum(stack))

    print(answer)
    return answer


if __name__ == '__main__':
    solution("100-200*300-500+20")
    solution("50*6-3*2")
