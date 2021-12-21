# 答えで二分探索
# 丸太の長さをxとして、何回切る必要があるか
def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    def check(x):
        if x == 0:
            return False
        cnt = 0
        for a in A:
            # 長さaをx毎に切り分けていく
            # aをx毎に切り分けるとき、a/xを切り上げして-1
            cnt += -(-a//x) - 1
        return cnt <= k

    """
    for i in range(1, 10):
        print(i, check(i))
    """
    # bisect
    ng = 0
    ok = sum(A)+1
    while ok-ng > 1:
        mid = (ok+ng)//2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)


main()
