# 反転のさせ方はnH2 = (n+2-1)C2 = n+1*n//2とおり。そのうち重複がいくつあるか

# Aの部分文字列で回文となるものを列挙することを考える
# a in Aについて、スタックの末尾がaならば、popして回文に追加
# a以外なら、スタックにaを追加
# これで、Aの部分文字列で回文となるもののうち、構成要素が最小のものを列挙できる

def main():
    A = list(input())
    n = len(A)

    def palindrome(A):
        stack = []
        ret = []
        for ri, a_ri in enumerate(A):
            if not stack:
                stack.append((ri, a_ri))
            elif len(stack) >= 1 and stack[-1][1] == a_ri:
                # XXパターンの回文
                le, a_ri = stack.pop()
                ret.append((ri, A[le:ri+1]))
            elif len(stack) >= 2 and stack[-2][1] == a_ri:
                # YXYパターンの回文
                stack.pop()
                le, a_le = stack.pop()
                ret.append((ri, A[le:ri+1]))
            else:
                stack.append((ri, a_ri))
        if len(ret) == 0:
            return []
        # stackに残っている、1文字回文を追加する
        for i, a_i in stack:
            ret.append((i, [a_i]))
        ret.sort()
        ret = [a for _, a in ret]
        ret2 = palindrome(ret)
        return ret + ret2

    ret = palindrome(A)
    print(ret)
    ans = 1+(n-1)*n//2 - len(ret)
    print(ans)


main()
