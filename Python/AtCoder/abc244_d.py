from collections import Counter


# 左から貪欲にやる
def main():
    S = list(input().split())
    T = list(input().split())

    if Counter(S) != Counter(T):
        print('No')

    # 持っている要素は同じ、偶奇を見る
    # swapに必要な回数が偶数か奇数か
    cnt = 0
    for i in range(3):
        if S[i] != T[i]:
            for delta in range(3):
                nex_i = i + delta
                if S[nex_i] == T[i]:
                    S[i], S[nex_i] = S[nex_i], S[i]
                    cnt += 1
                    break

    if cnt % 2 == 0:
        print('Yes')
    else:
        print('No')


main()
