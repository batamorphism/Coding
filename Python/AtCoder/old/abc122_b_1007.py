def main():
    S = input()
    n_end = len(S)
    ans = 0
    for left in range(n_end):
        for right in range(left+1, n_end+1):
            sub_str = S[left:right]
            is_acgt = True
            for char in sub_str:
                if char not in {'A', 'C', 'G', 'T'}:
                    is_acgt = False
                    break
            if is_acgt:
                ans = max(ans, len(sub_str))

    print(ans)


main()
