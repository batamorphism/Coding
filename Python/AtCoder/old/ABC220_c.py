def main():
    n = int(input())
    A = list(map(int, input().split()))
    x = int(input())

    sum_a = sum(A)
    a_cnt = x//sum_a
    other = x-a_cnt*sum_a  # 残りはAで補う
    ans = a_cnt*n
    for a in A:
        other -= a
        ans += 1
        if other < 0:
            break
    print(ans)


main()
