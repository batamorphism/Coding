import math


def main():
    n = int(input())
    ans = 0
    # 105 = 1*105, 3*35, 7*15
    for num in range(1, n+1):
        if num % 2 == 0:
            continue
        cnt = 0
        for div in range(1, math.ceil(num**0.5)+1):
            if num % div == 0:
                cnt += 2
            if cnt > 8:
                break
        if cnt == 8:
            ans += 1
    print(ans)


main()
