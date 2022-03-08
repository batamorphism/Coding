def main():
    S = input()
    q = int(input())
    for _ in range(q):
        t, k = map(int, input().split())
        k -= 1

        # 一個ずつ前に戻す
        val = 0  # k文字目をAにするのに必要な条件を最初に求める
        offset = 0
        for i in reversed(range(t)):
            if k % 2:
                k -= 1
                # 一個前の数字は、必ず1小さい
                val -= 1
                val %= 3
            k //= 2
            # 一個上の数字は、かならず1大きい
            val -= 1
            val %= 3
            if k == 0:
                offset = i
                break
        if k != 0:  # 最後までたどり着いた
            c = S[k]
            c_i = c2i(c)
            diff = c_i - val
            diff %= 3
            ans = i2c(diff)
            print(ans)
        else:  # 途中で、k=0になった
            c = S[0]
            # k回進める
            c_i = c2i(c)
            c_i += offset
            c_i %= 3
            diff = c_i - val
            diff %= 3
            ans = i2c(diff)
            print(ans)


def c2i(c):
    return ord(c) - ord('A')


def i2c(i):
    return chr(ord('A') + i)


main()
