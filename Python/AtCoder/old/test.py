import time


def main():
    siz = 1
    while siz <= 10**10:
        start = time.perf_counter()
        arr = [0]*siz
        sum_ = sum(arr)
        end = time.perf_counter()
        print(end-start, (end-start)/siz, siz, sum_)
        siz *= 2
        del arr


main()
