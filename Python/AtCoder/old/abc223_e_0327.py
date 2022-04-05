import itertools


def main():
    x0, y0, a0, b0, c0 = map(int, input().split())
    # 横に切るのか、縦に切るのかを判定
    # とりあえず常に右端を切り落とす

    def step1(x, y, a, b, c):
        # 右端を切り落として、cをあてがう
        w = (c+y-1)//y
        return x-w, y, a, b

    def step2(x, y, a, b):
        # 右端を切り落として、bをあてがう
        if y == 0:
            return False
        w = (b+y-1)//y
        x -= w
        if x*y >= a:
            return True
        else:
            return False

    for x, y in itertools.permutations([x0, y0]):
        for a, b, c in itertools.permutations([a0, b0, c0]):
            x1, y1, a, b = step1(x, y, a, b, c)
            for x2, y2 in itertools.permutations([x1, y1]):
                if step2(x2, y2, a, b):
                    print('Yes')
                    return
    print('No')


main()
