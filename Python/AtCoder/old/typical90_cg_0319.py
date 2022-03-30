def main():
    k = int(input())
    ans = 0
    for a in range(1, k+1):
        # a**3 <= abc
        # ゆえに、a**3 > k の場合は解が存在しない
        if a**3 > k:
            break
        # abc = kより、k % a == 0
        if k % a != 0:
            continue
        for b in range(a, k+1):
            if a*b**2 > k:
                break
            if (k//a) % b != 0:
                continue
            c = k//a//b
            if c < b:
                break
            ans += 1
    print(ans)


main()
