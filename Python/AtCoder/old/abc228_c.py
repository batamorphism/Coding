# 累積和
# それ以外の生徒が0点、その生徒が300点を取った時に、上位K人に入るか
# つまり、その生徒の点数をpとして、p+300より大きい生徒がK-1人以下か
# つまり、p+300以下の生徒がn-k+1人以上か(ただし本人を除く)
# p+300以下の生徒が、n-k人以上か
def main():
    n, k = map(int, input().split())
    P_list = [0]*1201
    human_list = []
    for _ in range(n):
        p1, p2, p3 = map(int, input().split())
        P_list[p1+p2+p3] += 1
        human_list.append(p1+p2+p3)

    cumsum = [0]*1201
    cumsum[0] = P_list[0]
    for p in range(1, 1201):
        cumsum[p] = cumsum[p-1] + P_list[p]

    for p in human_list:
        val = p+300
        # val以下の生徒がcnt人
        cnt = cumsum[val]
        # valより多い人数はcnt2人
        cnt2 = n - cnt
        # print(val, cnt)
        if cnt2 <= k-1:
            ans = 'Yes'
        else:
            ans = 'No'
        print(ans)


main()
