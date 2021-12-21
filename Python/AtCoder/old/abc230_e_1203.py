def main():
    n = int(input())
    ans = 0
    # i = n//2 + 1 -> n は1
    # i = n//3 -> n//2 は2
    val_end = int(n**0.5)
    for val in range(1, val_end):
        lo = n//(val+1) + 1
        hi = n//val
        ans += val*(hi-lo+1)
    # ここまでで、i = n//(val+1) + 1 以上の値は計算できた
    n1 = n//(val_end)
    for i in range(1, n1+1):
        ans += n//i

    print(ans)


main()
