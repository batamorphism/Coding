import string
MOD = 998244353


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        S = input()
        solve(n, S)


def solve(n, S):
    # Sより辞書順で小さい回文が何通りあるか
    # これは、Sより辞書順で小さい文字列をTとして
    # T + T[::-1]と、T[:-1] + T[::-1]が回文となることを使う
    # それぞれ、偶数と奇数なので重複はない
    # したがって、Tの組み合わせ数*2となる
    # ここで、Sを、Sより小さい長さnの最大の回文としてよい
    S = [c2i(s) for s in S]
    if n % 2 == 0:
        # 偶数の場合は、ちょうど前半と後半で分ければよい
        new_S = [-1]*n
        for i in range(n//2):
            if i < len(S):
                new_S[i] = S[i]
                new_S[n-i] = S[i]
        # -1がある場合、直前の文字を1小さくして、
    else:
    # 全要素が、S以下のものが何通りあるか
    ans = 0
    dp = 1
    if n % 2 == 0:
        for i in range(n//2):
            new_dp = 0
            # 何もしない
            new_dp = dp
            # top_valから連鎖
            if i < len(S):
                s_i = S[i]
                new_dp += dp*s_i
                # 既に確定している文字に、字を追加
                new_dp += dp*(s_i+1)
            dp = new_dp % MOD
    ans = dp
    print(ans)


def c2i(c):
    return ord(c) - ord('A')


main()
