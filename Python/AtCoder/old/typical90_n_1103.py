from collections import deque


def main():
    # a1, a2 <= b1, b2のとき
    # b1-a1+b2-a2 = b1-a2+b2-a1
    # したがって、上記の大小関係の時は組み合わせは気にしなくてよい
    # aとbを小さいほうから見ていって
    # aが余っていれば、新たなbと組み合わせて不便さに加算
    # を繰り返せばよい
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    AB = []
    for a in A:
        AB.append((a, 'A'))
    for b in B:
        AB.append((b, 'B'))
    AB.sort()

    que_a = deque()
    que_b = deque()
    ans = 0
    for val, ab in AB:
        if ab == 'A':
            # 新たにAが来た時
            # Bが存在しない場合は、queに追加
            if que_b:
                b = que_b.popleft()
                ans += abs(val - b)
            else:
                que_a.append(val)
        else:
            if que_a:
                a = que_a.popleft()
                ans += abs(val - a)
            else:
                que_b.append(val)

    print(ans)


main()
