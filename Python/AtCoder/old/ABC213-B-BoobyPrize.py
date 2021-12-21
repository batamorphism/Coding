
def main():
    n, *A = map(int, open(0).read().split())
    B = sorted(A)
    length = len(A)
    booby = B[length-2]
    rank = A.index(booby)+1
    print(rank)


main()
