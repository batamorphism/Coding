MOD = 998244353


def main():
    t = int(input())
    ans_list = []
    for _ in range(t):
        n = int(input())
        S = input()

        ans = solve(n, S)
        ans_list.append(ans)

    print(*ans_list, sep='\n')


def solve(n, S):
    if n != len(S):
        raise

    # Sの左半分を右半分にコピーして回文にする
    target = list(S)
    le = 0
    ri = n-1
    while le < ri:
        target[ri] = target[le]
        le += 1
        ri -= 1

    # target以下の回文がいくつあるか
    last = (n-1)//2  # 回文の区切り目となる場所
    ans = 0
    for i in range(last+1):
        ans *= 26  # 既に確定した文字列の末尾にA~Zを追加
        ans += A2i(target[i])  # まだ確定していない文字の末尾にA~(target[i]の1文字前)を追加
        ans %= MOD
    # target自身を追加処理
    ans += 1

    # targetが条件を満た差ない場合は、1削る
    if ''.join(target) > S:
        ans -= 1
    ans %= MOD
    return ans


def A2i(c):
    return ord(c) - ord('A')


def i2A(i):
    return chr(ord('A') + i)


main()
