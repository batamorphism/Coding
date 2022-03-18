def main():
    t = int(input())
    for _ in range(t):
        a, s = map(int, input().split())
        print(solve(a, s))


def solve(a, s):
    # x & y = a
    # x + y = s
    # ここで
    # x + y = (x ^ y) + (x & y) << 1
    # しかるに
    # s = a<<1 + (x^y)
    # s-a<<1 = (x^y)
    # ゆえに
    # x&y=a
    # x^y=(s-a<<1)
    # を満たすx, yがあれば十分
    # x 0 0 1 1
    # y 0 1 0 1
    # & 0 0 0 1
    # ^ 0 1 1 0
    # より、x&yもx^yも両方とも1になるbitがあるとだめ
    o = s-(a << 1)
    if o < 0:
        return 'No'
    if o & a:
        return 'No'
    return 'Yes'


main()
