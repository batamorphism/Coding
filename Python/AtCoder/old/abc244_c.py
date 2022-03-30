def main():
    n = int(input())
    useful = set()
    for val in range(1, 2*n+2):
        useful.add(val)

    while True:
        taka = useful.pop()
        print(taka, flush=True)
        aoki = int(input())
        if aoki == 0:
            return
        useful.remove(aoki)


main()
