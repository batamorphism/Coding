def main():
    # oを0
    # xを1とする?
    # o->xになる箇所と、x->oになる箇所を記録する
    # s[i]=='o' and s[i+1]=='x'のとき
    # leftがi以下かつ、rightがi+1以上ならばよい->(i+1)*(n-i)みたいな
    n = int(input())
    s = input()
    # arr = [0]*(n-1)
    ans = 0
    pre_left = -1
    for i in range(n-1):
        if s[i] != s[i+1]:
            ans += (i-pre_left)*(n-i-1)
            pre_left = i
    print(ans)


main()
