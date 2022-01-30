def main():
    # フィボナッチ数列を作成する
    fib = [1, 1]
    for _ in range(84):
        fib.append(fib[-1]+fib[-2])

    fib.reverse()
    ans = []
    parity = 1
    n = int(input())
    for i in range(len(fib)):
        # 4-3-4-3と操作を繰り返す
        while n >= fib[i]:
            n -= fib[i]
            ans.append(1+parity)
        ans.append(3+parity)
        parity = (1-parity)
    print(len(ans))
    print(*ans)


main()
