# アンバランスである定義
# 最も頻度が高い要素の数が、全体の半分より大きいこと
# 文字が26種類しかないことから攻める
# aとxのみからなる文字列について、aがアンバランスであるかを判定することを考える
# aを1, xを0とすれば、0と1のみからなる部分列について、区間の和が区間の幅の2倍より大きい区間があるかの判定問題
# アンバランスでない判定は次の通り
# sum(ri)-sum(le) <= (ri-le)//2 かつ、ri - le >= 2
# sum(ri)*2 - ri <= sum(le)*2 - le
# ここで、sum(i) = [1, i]の和
# f(i) = sum(i) - 2*iとして、f(i)が広義単調減少であることを見ればよい
# また、そうでない場合に、f(le) < f(ri)となるle, riのペアを出力すればよい
import string
INF = float('inf')


def main():
    s = input()
    s = '*' + s
    for char in string.ascii_lowercase:
        is_ans, ans = solve(s, char)
        if is_ans:
            print(*ans)
            return
    print(-1, -1)


def solve(S, char):
    # Sは1-indexed
    n = len(S)
    A = []
    for s in S:
        if s == char:
            A.append(1)
        else:
            A.append(0)
    # 累積和を取る
    for i in range(1, n):
        A[i] += A[i-1]
    for i in range(n):
        A[i] *= 2
    # 2*iを引く
    for i in range(n):
        A[i] -= i
    # Aが広義単調減少であることを見る
    min_a = INF
    min_a_i = -1
    for i, a_i in enumerate(A):
        if a_i < min_a:
            min_a = a_i
            min_a_i = i
        elif a_i > min_a and i - min_a_i >= 2:
            # 単調増加でないかつ長さが2以上
            is_ans = True
            ans = [min_a_i+1, i]
            return is_ans, ans
    return False, None


main()
