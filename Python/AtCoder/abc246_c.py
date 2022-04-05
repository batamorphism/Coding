def main():
    n, k, x = map(int, input().split())
    A = list(map(int, input().split()))

    for i in range(n):
        a_i = A[i]
        # a_i // x枚のクーポンを使用できる
        use_k = a_i // x
        use_k = min(use_k, k)
        A[i] = a_i-use_k*x
        k -= use_k
        if k == 0:
            break

    if k == 0:
        print(sum(A))
        return

    A.sort(reverse=True)
    for i in range(n):
        A[i] = 0
        k -= 1
        if k == 0:
            break
    print(sum(A))


main()
