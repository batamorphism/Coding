# 片方を全列挙して、もう一方を高速に処理する
# num[le] = [le, n-1]を指す数
# leを固定した時に、条件を満たすriは
# (num[le]-num[ri+1]) // 10**(le-ri+1)
# であり、これが2019の倍数であるriの個数を高速で数え上げたい
# ここで、2019と10は互いに素なので、10で割らなくても問題ない
# したがって、
# num[le]-num[ri]が2019の倍数であるriの個数を数えればよい
# num[le] == num[ri] (mod2019)を指すのだから
# cnt[val] = [le, n-1]でnum[ri]=val(mod2019)となる個数
# とすればよい
def main():
    S = input()

    n_end = len(S)
    cnt = [0] * 2019
    cnt[0] = 1
    # setup num
    num_of = [0] * n_end
    for le in range(n_end-1, -1, -1):
        if le == n_end-1:
            num_of[le] = int(S[le])
        else:
            val1 = num_of[le+1]
            val2 = int(S[le])*(pow(10, (n_end-le-1), 2019))
            num_of[le] = (val1+val2) % 2019
    ans = 0
    for le in range(n_end-1, -1, -1):
        # num = int(S[le:]) % 2019
        num = num_of[le]
        ans += cnt[num]
        # cntのアップデート
        cnt[num] += 1
    print(ans)


main()
