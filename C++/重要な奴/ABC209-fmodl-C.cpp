// copyright
#include<bits/stdc++.h>

/**
 * @brief
 * 以下の条件を満たす長さNの整数列Aの個数を求めよ
 * 各A[i]は1以上C[i]以下
 * 各A[i]とA[j]は異なる
 * A[0]として取りえるのは、C[0]通り
 * A[1]として取りえるのは、A[0]<=C[1]であれば、C[1]-1通り
 *                       A[0]>C[1]であれば、C[1]通り
 * Cをソートしておく
 * この時、A[i-1]<=C[i]が確定するので
 * A[i]として取りえるのは、C[i]-i通り
 */
int solver(int n, std::vector<int> C) {
    std::sort(C.begin(), C.end());
    int64_t ans = 1;
    for (int i = 0; i < n; i++) {
        if (C[i]-i > 0) {
            ans = fmodl((ans*(C[i]-i)), (pow(10, 9)+7));
        } else {
            ans = 0;
        }
    }
    return ans;
}

int main() {
    // input
    int n;
    std::cin >> n;
    std::vector<int> C(n);
    for (int i = 0; i < n; i++) {
        int foo;
        std::cin >> foo;
        C[i] = foo;
    }

    // solve
    int ans;
    ans = solver(n, C);
    std::cout << ans << std::endl;
}
