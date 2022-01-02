from collections import deque


def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    sliding_minimum_query(A, k)
    print(*A[:n-k+1])


def sliding_minimum_query(A, k):
    """スライド最小値
    Aを幅kのスライド最小値に差し替える

    Args:
        A ([type]): スライド最小値を取る対象のリスト
        k ([type]): スライド最小値を取る幅
    """
    # 最小値の候補となる(i, a_i)をqueに入れていく
    que = deque()
    # 後ろから見ていく
    for lo in range(len(A)-1, -1, -1):
        a_lo = A[lo]
        hi = lo + k - 1
        # hi >= となる要素しか候補にならない
        while que and not(que[0][0] <= hi):
            que.popleft()
        # que[0][1] >= a_loの時は候補にならない
        while que and not(que[0][1] < a_lo):
            que.popleft()
        # queの末尾がa_lo以上の時は候補とならない
        while que and not(que[-1][1] < a_lo):
            que.pop()
        # この時点で、que[0][0] < a_loかつ queは単調増加、若しくは空が確定
        que.append((lo, a_lo))
        # queの先頭の要素が、最小値
        min_i, min_a = que[0]
        A[lo] = min_a


main()
