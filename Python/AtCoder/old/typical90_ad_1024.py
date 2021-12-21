def main():
    n, k = map(int, input().split())
    # n以下の数について高速に素因数分解を行う
    # 櫛
    end = 10**7+10
    m = int(end**0.5)+10
    is_prime = [True]*end
    div_num = [i for i in range(end)]
    div_cnt = [0]*end

    is_prime[0] = False
    is_prime[1] = False
    # for num in range(m):
    for num in range(end):
        if is_prime[num]:
            # num*(num+i)は全て合成数
            for num2 in range(num, end, num):
                div_cnt[num2] += 1
            for not_prime in range(num*num, end, num):
                is_prime[not_prime] = False
                div_num[not_prime] = num

    ans = 0
    for num in range(2, n+1):
        if div_cnt[num] >= k:
            ans += 1

    print(ans)


main()
