import itertools


def main():
    arr = list(input())
    arr = [int(a) for a in arr]
    i_end = len(arr)
    ALL = 1 << i_end
    ans = 0
    for bit in range(ALL):
        list_a = []
        list_b = []
        for i in range(i_end):
            if bit >> i & 1:
                list_a.append(arr[i])
            else:
                list_b.append(arr[i])
        # list_aのうち、必要なものは最大の数値だけである
        # したがって、ソートすればよい
        if len(list_a) == 0 or len(list_b) == 0:
            continue
        list_a.sort(reverse=True)
        list_b.sort(reverse=True)
        num_a = 0
        num_b = 0
        if list_a[0] == 0 or list_b[0] == 0:
            continue
        for a in list_a:
            num_a = num_a*10
            num_a += a
        for b in list_b:
            num_b = num_b*10
            num_b += b
        ans = max(num_a*num_b, ans)
    print(ans)


main()
