import heapq


def main():
    q = int(input())
    Q = []
    for _ in range(q):
        q = list(map(int, input().split()))
        Q.append(q)

    bag = []
    S = [0]  # i回目の操作までに足された数
    # ボールを入れるときに、S[i]をあらかじめ引いたものを入れておく

    i = 0
    for q in Q:
        i += 1
        if q[0] == 1:
            # 袋に入れるクエリ
            S.append(S[i-1])
            heapq.heappush(bag, q[1]-S[i])
        elif q[0] == 2:
            # 数字を書き換えるクエリ
            S.append(S[i-1]+q[1])
        else:
            # ボールを取り出すクエリ
            S.append(S[i-1])
            ball = heapq.heappop(bag)
            num = ball+S[i]
            print(num)


main()
