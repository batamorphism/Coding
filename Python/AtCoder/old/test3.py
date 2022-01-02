
def your(n, k):
    def into(x):
        return sum(map(int, list(str(x))))
    # n,k = map(int, input().split())
    g = [False]*100000
    g[n] = True
    c = []
    c.append(n)
    count = 0
    while True:
        count += 1
        n = into(n)+n
        n %= 100000
        c.append(n)
        if g[n]:
            break
        g[n] = True
    for i in range(len(c)):
        if c[i] == n:
            f = i
            break
    if f == 0:
        # print(c[((k+1)%count)-1])
        return(c[((k+1)%count)-1])
        # exit(0)
    # print(c[(k-(f-1))%(count-f)+(f-1)])
    return(c[(k-(f-1))%(count-f)+(f-1)])


def my(n, k):
    # ダブリング、メモ
    ans = calc(n, k)
    # print(ans)
    return ans


memo = {}
def calc(p_x, p_k):
    # xから始まる操作をk回行うときの値
    x = p_x
    k = p_k
    if (p_x, p_k) in memo:
        return memo[(p_x, p_k)]
    # print(x, k)
    if k == 1:
        # 一回だけ操作する
        y = calc_y(x)
        ret = (x+y) % 10**5
        memo[(p_x, p_k)] = ret
        return ret
    if k & 1:
        # 一回進めてkを偶数にする
        x = calc(x, 1)
        k -= 1
    x = calc(x, k // 2)
    k //= 2
    x = calc(x, k)
    memo[(p_x, p_k)] = x
    return x


def calc_y(x):
    # xの各桁の和を計算し、これをyとする
    y = 0
    x = str(x)
    for xx in map(int, x):
        y += xx
    return y


def main():
    for n in range(10):
        for k in range(1, 10):
            your_ans = your(n, k)
            my_ans = my(n, k)
            if your_ans != my_ans:
                print(n, k, your_ans, my_ans)


main()
