# 一番多いケーキの間にほかのやつを挟んでいく
# *1*1*1* 一番多いケーキがn個あるとして、n-1個の隙間に挟んでいければおｋ
def main():
    k, t = map(int, input().split())
    A = list(map(int, input().split()))
    max_a = max(A)
    otr_a = sum(A) - max_a

    ans = max_a-1
    ans = max(ans-otr_a, 0)
    print(ans)


main()
