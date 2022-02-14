import pypyjit
pypyjit.set_param("max_unroll_recursion=-1")


def main():
    # [le, ri]を今使っているものとして処理する
    n, q = map(int, input().split())
    que_end = (n+q)*4
    que = [None]*que_end
    le = que_end//2 - n//2
    ri = le + n - 1
    A = list(map(int, input().split()))
    for i, a_i in enumerate(A):
        que[i+le] = a_i

    query_list = [tuple(map(int, input().split())) for _ in range(q)]

    for t, x, y in query_list:
        x -= 1
        y -= 1
        if t == 1:
            # xとyを交換
            x = x + le
            y = y + le
            que[x], que[y] = que[y], que[x]
        elif t == 2:
            # 右方向にシフト
            # すなわち、le-1とriをswap
            que[le-1], que[ri] = que[ri], que[le-1]
            le -= 1
            ri -= 1
        else:
            # x項を求める
            x = x + le
            print(que[x])
        # print(que[le:ri+1])


main()
