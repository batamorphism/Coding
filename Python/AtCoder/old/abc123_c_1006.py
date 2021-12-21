def main():
    n_end, m_end = map(int, input().split())
    light_list = []
    for _ in range(m_end):
        _, *s = list(map(int, input().split()))
        s = [ss-1 for ss in s]
        light_list.append(s)

    p_list = list(map(int, input().split()))

    ALL = 1 << n_end
    ans = 0
    for bit in range(ALL):
        switch_set = set()
        for n in range(n_end):
            if bit >> n & 1:
                switch_set.add(n)

        is_All = True
        for light, p in zip(light_list, p_list):
            cnt = 0
            for s in light:
                if s in switch_set:
                    cnt += 1
            if cnt % 2 != p:
                is_All = False
        if is_All:
            ans += 1

    print(ans)
    return 0


main()
