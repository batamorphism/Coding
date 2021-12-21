# N個の街があり、
# b君がi街に行くとa君は0票を獲得、b君はA[i]+B[i]票を獲得
# b君がi街に行かないと、a君はA[i]票を獲得、b君は0票を獲得
# この時の、b君が最小で行かないといけない街の数

def main():
    n = int(input())
    A = []
    B = []
    for _ in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # 仮にb君が一街もいかなかった場合の、票数差
    diff = -sum(A)
    # Cは、街に行った場合に縮まる票数差
    C = []
    for (a, b) in zip(A, B):
        C.append(2*a+b)
    # 票数差が縮まる街から訪れて、票数差が0より大きくなるタイミング
    C.sort(reverse=True)
    ans = 0
    for c in C:
        ans += 1
        diff += c
        if diff > 0:
            break

    print(ans)


main()