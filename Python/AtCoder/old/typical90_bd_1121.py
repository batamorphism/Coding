from collections import deque
# DP[day][val]
# day日目にval円となる買い方があるか


def main():
    n, s = map(int, input().split())
    DP = [[0]*(s+1) for _ in range(n+1)]
    DP[0][0] = 1

    AB = [(-1, -1)]
    for _ in range(n):
        a, b = map(int, input().split())
        AB.append((a, b))

    for day in range(1, n+1):
        a, b = AB[day]
        for val in range(s+1):
            if DP[day-1][val] != 0:
                # 前日にval円を実現する方法がある場合
                val_a = val+a
                val_b = val+b
                if val_a <= s:
                    DP[day][val_a] = a
                if val_b <= s:
                    DP[day][val_b] = b

    if DP[n][s] == 0:
        print('Impossible')
        return

    que = deque()
    val = s
    for day in range(n, 0, -1):
        a_or_b = DP[day][val]  # day日目に買った商品の価格
        if a_or_b == AB[day][0]:
            que.appendleft('A')
        else:
            que.appendleft('B')
        val -= a_or_b
    # print(DP[n][s])
    print(''.join(list(que)))


main()
