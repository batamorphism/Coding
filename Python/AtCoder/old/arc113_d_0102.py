MOD = 998244353


def main():
    r_end, c_end, k = map(int, input().split())

    if r_end == 1:
        print(solve_simple(r_end, c_end, k))
        return
    if c_end == 1:
        print(solve_simple(r_end, c_end, k))
        return

    # r_end >= 2 and c_end >= 2
    # max(A) <= min(B)が必要。これを満たさない場合、解が存在しない
    # 逆に、max(A) <= min(B)を満たしている任意のA, Bに対し、対応するgridが存在するか
    # r_end == c_end == 2の時成立しているとする
    # 新たに列を追加し、b_3が新設されたとする
    # 対応するa_1, a_2 <= b_3は前提より成立
    # 追加された、gridは両方b_3として問題ない
    # 数学的帰納法により示された

    ans = 0
    for max_a in range(1, k+1):
        # max(A) = max_aを満たす数を求める
        cnt_a = pow(max_a, r_end, MOD) - pow(max_a-1, r_end, MOD)
        # min(B) >= max_aを満たす数を求める
        cnt_b = pow(k-max_a+1, c_end, MOD)
        ans += (cnt_a * cnt_b) % MOD
        ans %= MOD

    print(ans)


def solve_simple(r_end, c_end, k):
    if r_end == 1:
        # 1行c_end列に、k以下の整数を一つずつ書き込み
        # a_iはその行の最小値
        # b_iはその数値そのもの
        # したがって、考えうるパターン数は、b_iの取りうる数値と一致するため
        # k**c_end
        return pow(k, c_end, MOD)
    elif c_end == 1:
        return pow(k, r_end, MOD)
    else:
        raise


main()
