# みかんn個の組み合わせでa*k + b*(n-k) = wとなるかを判定する
# このnのうち最大のものと最小のものを考える

def main():
    a, b, w = map(int, input().split())
    w = w*1000

    max_ans = -1
    min_ans = 1e14

    # 答えとして考えうる範囲は、w//b 以上 w//a+1 以下
    for n in range(w//b, w//a+2):

        if is_possible(a, b, w, n):
            if max_ans < n:
                max_ans = n
            if min_ans > n:
                min_ans = n

    if max_ans > 0:
        print(min_ans)
        print(max_ans)
    else:
        print('UNSATISFIABLE')


def is_possible(a, b, w, n):
    # aとbをn個組み合わせてwになるか
    if a*n <= w <= b*n:
        return True
    else:
        return False


main()
