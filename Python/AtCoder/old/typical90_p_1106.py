def main():
    n = int(input())
    a_val, b_val, c_val = map(int, input().split())
    ans = 10000
    for a_cnt in range(10000):
        val_a = a_cnt*a_val
        if val_a > n:
            break
        for b_cnt in range(10000-a_cnt):
            val_b = b_cnt*b_val
            val = val_a+val_b
            if val > n:
                break
            if (n-val) % c_val != 0:
                continue
            c_cnt = (n-val)//c_val
            ans = min(ans, a_cnt+b_cnt+c_cnt)

    print(ans)


main()
