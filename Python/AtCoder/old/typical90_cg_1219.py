def main():
    k = int(input())
    cnt = 0
    for a in range(1, k+1):
        if a**3 > k:
            break
        if k % a != 0:
            continue
        for b in range(a, k+1):
            if a*b*b > k:
                break
            # a*b*c = k
            # c = k // (a*b)
            if k % (a*b) == 0:
                c = k // (a*b)
                if c >= b:
                    cnt += 1
    print(cnt)


main()
