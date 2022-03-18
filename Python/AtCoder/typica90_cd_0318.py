MOD = 10**9 + 7


# xは、len(str(x))個貢献する
def main():
    le, ri = map(int, input().split())
    le_ans = solve(le-1)
    ri_ans = solve(ri)
    ans = ri_ans-le_ans
    ans %= MOD
    print(ans)


def solve(val):
    # 0, ...,valについて、
    # 整数xをx回書く操作を繰り返す
    ret = 0
    dgt = 1
    while 10**dgt <= val:
        # [10**(dgt-1), 10**dgt)について処理する
        lo = 10**(dgt-1)
        hi = 10**dgt-1
        cnt = (hi+lo)*(hi-lo+1)//2  # [10**(dgt-1), 10**dgt)の総和
        ret += cnt * dgt  # 各数値はdgt桁ある
        ret %= MOD
        dgt += 1
    # [10**(dgt-1), val]について処理する
    lo = 10**(dgt-1)
    hi = val
    cnt = (hi+lo)*(hi-lo+1)//2
    ret += cnt * dgt
    ret %= MOD
    return ret


main()
