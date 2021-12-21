def main():
    n, m = map(int, input().split())
    lamp_list = []
    for i in range(m):
        k, *S = map(int, input().split())
        lamp_list.append([k, S])
    P = list(map(int, input().split()))

    switch_list = [0]*(n+1)
    ans = 0
    for i in range(1 << n):
        for switch in range(n):
            if(i >> switch & 1):
                switch_list[switch+1] = 1
            else:
                switch_list[switch+1] = 0
        is_all_lighting = True
        for j in range(m):
            lamp = lamp_list[j]
            p = P[j]
            lighting_cnt = 0
            for s in lamp[1]:
                if switch_list[s] == 1:
                    lighting_cnt += 1
            if (lighting_cnt % 2) != p:
                is_all_lighting = False
                break
        if is_all_lighting:
            ans += 1

    print(ans)


main()
