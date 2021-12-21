def main():
    s = input()
    t = input()
    i_end = len(s)
    if s == t:
        print('Yes')
        return
    for i in range(i_end-1):
        arr = list(s)
        arr[i], arr[i+1] = arr[i+1], arr[i]
        new_s = ''.join(arr)
        if new_s == t:
            print('Yes')
            return
    print('No')


main()
