// copyright
// #include<bits/stdc++.h>
#include<iostream>
#include<vector>
void solve(int n, std::vector<int> w) {
    // 区間DP

    // dp[le][ri] = [le, ri)を見た際における最大値
    std::vector<std::vector<int>> dp(n+1, std::vector<int>(n+1, 0));

    for (int cnt = 2; cnt <= n; cnt++) {
        for (int le = 0; le < n; le++) {
            int ri = le + cnt;
            if (ri > n) break;
            // 両端を落とす
            // [le, ri)を全て落としている場合かつ、
            // 重さの差が1以下である場合にのみ可能
            if (dp[le+1][ri-1] == cnt-2) {
                if (abs(w[le] - w[ri-1]) <= 1) {
                    dp[le][ri] = cnt;
                    continue;
                }
            }
            // 間で分ける
            for (int sep = le; sep < ri; sep++) {
                dp[le][ri] = std::max(dp[le][ri], dp[le][sep] + dp[sep][ri]);
            }
        }
    }
    auto ans = dp[0][n];
    std::cout << ans << std::endl;
}

int main() {
    while (true) {
        int n;
        std::cin >> n;
        if (n == 0) break;

        std::vector<int> w(n);
        for (int i = 0; i < n; i++) {
            std::cin >> w[i];
        }
        solve(n, w);
    }
    return 0;
}
