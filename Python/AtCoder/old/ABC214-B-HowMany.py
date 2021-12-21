def main():
    s, t = map(int, input().split())
    solv(s, t)


def solv(s: int, t: int):
    """
    a+b+c<=sかつ
    a*b*c<=tを満たす0以上の整数の組a, b, cはいくつあるか
    ここで
    s<=100
    t<=10000

    Args:
        s (int): [description]
        t (int): [description]
    """
    ans = 0
    for a in range(s+1):
        for b in range(s+1):
            if a+b>s:
                break
            for c in range(s+1):
                if a+b+c <= s and a*b*c <= t:
                    ans += 1
                if a*b*c > t or a+b+c > s:
                    break
    print(ans)


main()