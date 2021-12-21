def main():
    # input
    n = int(input())
    le_list = []
    ri_list = []
    for _ in range(n):
        l, r = map(int, input().split())
        le_list.append(l)
        ri_list.append(r)

    ans = 0
    for i in range(n):
        a_le, a_ri = le_list[i], ri_list[i]
        prob = 1/(a_ri-a_le+1)
        for a in range(a_le, a_ri+1):
            for le, ri in zip(le_list[:i], ri_list[:i]):
                len = ri-le+1
                ans += max((ri-max(a, le-1))/len*prob, 0)
    print(ans)


main()
