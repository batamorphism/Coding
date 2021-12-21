def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def partition(A, p, r):
    # A[p,...,r]を、A[p,..,q-1]はpiv以下、それ以外はpiv以上になるよう分割する
    piv = A[r][1]
    le = p-1
    for ri in range(p, r):
        if A[ri][1] <= piv:
            le += 1  # A[le+1]はpivより大
            A[ri], A[le] = A[le], A[ri]
    A[le+1], A[r] = A[r], A[le+1]
    return le+1


def main():
    n = int(input())
    Arr = []
    for _ in range(n):
        char, num = input().split()
        num = int(num)
        Arr.append((char, num))

    orig_Arr = Arr[:]
    quicksort(Arr, 0, n-1)

    # check stable
    # 同じ数字を持つカードで、文字の出てくる順番が変わっていなければstable
    A_char_of = {}
    B_char_of = {}
    for char, num in Arr:
        if num not in A_char_of:
            A_char_of[num] = []
        A_char_of[num].append(char)
    for char, num in orig_Arr:
        if num not in B_char_of:
            B_char_of[num] = []
        B_char_of[num].append(char)

    is_stable = True
    for num in A_char_of.keys():
        if A_char_of[num] != B_char_of[num]:
            is_stable = False
            break

    if is_stable:
        print("Stable")
    else:
        print("Not stable")

    for char, num in Arr:
        print(char, num)


main()
