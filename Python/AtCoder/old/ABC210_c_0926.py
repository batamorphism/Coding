from collections import Counter


def main():
    n, k = map(int, input().split())
    color_list = list(map(int, input().split()))
    ans = 0
    for left in range(n-k+1):
        right = left+k-1
        if left == 0:
            count = Counter(color_list[:right+1])
        else:
            # remove left-1
            count[color_list[left-1]] -= 1
            if count[color_list[left-1]] == 0:
                del count[color_list[left-1]]
            # add right
            count[color_list[right]] += 1
        ans = max(len(count), ans)
    print(ans)


main()
