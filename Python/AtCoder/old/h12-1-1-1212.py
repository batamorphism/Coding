P = {1: 100,
     2: 90,
     3: 80}
Sur = {1: -65,
       2: 25,
       3: 55}

r = 0.02

def div_fac(r, n):
    # 利率rのn年割引率
    return 1/(1+r)**n

def pm(r):
    # 割引率をrとした場合のpm
    p_pv = 0
    sur_pv = 0
    for y in range(1, 4):
        p_pv += P[y] * div_fac(r, y-1)
        sur_pv += Sur[y] * div_fac(r, y)
    return sur_pv/p_pv

ans = pm(r)
print(ans)

ok = 0
ng = 1
# pm(r) == 0となるrを求める
while ng - ok > 1e-9:
    mid = (ok + ng) / 2
    if pm(mid) > 0:
        ok = mid
    else:
        ng = mid

ans = ok
print(ans)
