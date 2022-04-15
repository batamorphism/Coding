from collections import deque


# 後手の取るカードを、(i+k)%modにする場合、
# 先手のスコアを最大化させる
def main():
    n = int(input())
    A = list(map(int, input().split()))

    # カードを取りうるパターンは
    # 後, 後, ..., 後, 前, 前, ..., 前
    # か
    # 前, 後
    # のみ
    # 1,1,...,1,0,0,...,0
    # or
    # 0,1
    # 回転可能であることを考えれば
    # 1,1,...,1,0,0,...,0
    # のみを考えればよい
    # したがって、0の部分を足して、1の部分を引いた場合の値の最大値を求めればよい

    used = [-1]*n
    total_score = 0
    for i in range(n):
        score = 0
        cur_ans = 0
        for cnt in range(1, n+1):
            first_i = (i+cnt-1) % n
            secon_i = (i-cnt) % n
            if not (used[first_i] == -1 and used[secon_i] == -1):
                continue
            first_a = A[first_i]
            secon_a = A[secon_i]
            nex_score = score + first_a - secon_a
            if nex_score >= score:
                score = nex_score
                cur_ans += first_a
                used[first_i] = 0
                used[secon_i] = 1
            else:
                break
        total_score += cur_ans
    print(total_score)
    print(used)


main()
