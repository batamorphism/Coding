// copyright
#include <bits/stdc++.h>

int solver(int n, int *W) {
    // 区間DP
    // DP[le][ri] := 区間[le, ri)で取り除いたブロックの最大値
    int n_end = n+1;
    int DP[n_end][n_end];
    for (int i = 0; i < n_end; i++) {
        for (int j = 0; j < n_end; j++) {
            DP[i][j] = 0;
        }
    }

    // d:= leとriの間にある個数
    // le:= 左端
    // ri:= 右端
    for (int d = 0; d < n_end; d++) {
        for (int le = 0; le < n_end; le++) {
            int ri = le + d;
            if (ri >= n_end) {
                break;
            }
            int max_value = 0;
            // [le, ri)のすべてを取り除ける場合
            if (DP[le+1][ri-1] == d-2) {
                if (abs(W[le] - W[ri-1]) <= 1) {
                    max_value = d;
                }
            }
            // [le, sep), [sep, ri)に分けて取り除く場合
            for (int sep = le; sep <= ri; sep++) {
                int left_value = DP[le][sep];
                int right_value = DP[sep][ri];
                if (left_value + right_value > max_value) {
                    max_value = left_value + right_value;
                }
            }
            // std::cout << d << le << ri << max_value << std::endl;
            DP[le][ri] = max_value;
        }
    }
    int ans = DP[0][n_end-1];
    std::cout << ans << std::endl;
    return 0;
}


int main() {
    // 入力
    while (true) {
        int n;
        std::cin >> n;
        if (n == 0) {
            break;
        }
        int W[n];
        for (int i = 0; i < n; i++) {
            std::cin >> W[i];
        }
        solver(n, W);
    }
    return 0;
}
