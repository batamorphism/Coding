from collections import deque


def main():
    # しゃくとり法
    n = int(input())
    S = input()
    cnt_of = {'o': 0, 'x': 0}
    total = (n+1)*n//2
    com_ans = 0  # oとxいずれかしか含まれない
    que = deque()

    for s in S:
        que.append(s)
        cnt_of[s] += 1
        while not (cnt_of['o'] == 0 or cnt_of['x'] == 0):
            rm = que.popleft()
            cnt_of[rm] -= 1
        com_ans += len(que)

    print(total-com_ans)


main()
