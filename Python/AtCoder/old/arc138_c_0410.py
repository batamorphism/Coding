# 上界が答え
def main():
    n = int(input())
    A = list(map(int, input().split()))
    # Aのうち、大きい方半分をすぬけ君(1)が、それ以外を最小太郎君(-1)がとる
    is_first = [-1]*n

    # Aのうち、大きい半分のほうのインデックス
    greater_A = get_greater_A(A)
    for i in greater_A:
        is_first[i] = 1

    # print(is_first)
    sum_is_first = is_first[:]

    # 累積和が最大になるところが答え
    for i in range(1, n):
        sum_is_first[i] += sum_is_first[i-1]

    # print(sum_is_first)
    max_val = max(sum_is_first)
    ind = sum_is_first.index(max_val)
    k = (ind+1) % n

    ans = 0
    for i in range(n):
        if is_first[i] == 1:
            ans += A[i]

    print(k, ans)


def get_greater_A(A):
    B = [(a_i, i) for i, a_i in enumerate(A)]
    B.sort(reverse=True)
    B = B[:len(B)//2]
    ret = [i for b_i, i in B]
    return ret


main()
