from collections import namedtuple

Config = namedtuple('Config', ['min_r', 'min_c', 'max_r', 'max_c', 'SUM', 'k'])


def main():
    h, w, k, v = map(int, input().split())
    min_r = 1
    min_c = 1
    max_r = h
    max_c = w
    # SUM[r][c] = A[r][c]まで足した総和
    # ただし、aは1 indexed
    A = [[0]*(max_c+1)]
    for _ in range(h):
        tmp = list(map(int, input().split()))
        tmp = [0] + tmp
        A.append(tmp)

    SUM = [[0]*(max_c+1) for _ in range(max_r+1)]

    for r in range(max_r+1):
        for c in range(max_c+1):
            if r < min_r or c < min_c:
                SUM[r][c] = 0
            SUM[r][c] = SUM[r][c-1]+SUM[r-1][c]-SUM[r-1][c-1]+A[r][c]

    config = Config(min_r, min_c, max_r, max_c, SUM, k)

    # 全探索
    # (125*125)**2 = 244_140_625なので多分間に合う
    ans = 0
    for r0 in range(min_r, max_r+1):
        for c0 in range(min_c, max_c+1):
            for r1 in range(r0, max_r+1):
                for c1 in range(c0, max_c+1):
                    cost = calc_cost(r0, c0, r1, c1, config)
                    if cost <= v:
                        m = (r1-r0+1)*(c1-c0+1)
                        ans = max(m, ans)
    print(ans)


def calc_cost(r0, c0, r1, c1, cnf: Config) -> int:
    # 購入した土地に係るコスト
    # r0c0~r1c1の累積和
    cost1 = cnf.SUM[r1][c1]-cnf.SUM[r0-1][c1]-cnf.SUM[r1][c0-1]+cnf.SUM[r0-1][c0-1]
    # 建設費用
    m = (r1-r0+1)*(c1-c0+1)
    cost2 = m*cnf.k
    return cost1+cost2


main()
