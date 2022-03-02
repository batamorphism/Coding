// copyright
#include<bits/stdc++.h>

int solve(std::string x, std::string y) {
    // 1-indexed
    int n = x.size()+1;
    int m = y.size()+1;
    std::vector<std::vector<int>> dp(n, std::vector<int>(m, 0));

    for (int i = 1; i < n; i++) {
        for (int j = 1; j < m; j++) {
            if (x[i-1] == y[j-1]) {
                dp[i][j] = dp[i-1][j-1] + 1;
            } else {
                dp[i][j] = std::max(dp[i-1][j], dp[i][j-1]);
            }
        }
    }
    return dp[n-1][m-1];
}

int main() {
    int q;
    std::cin >> q;
    for (int i = 0; i < q; i++) {
        std::string x, y;
        std::cin >> x >> y;
        int ans = solve(x, y);
        std::cout << ans << std::endl;
    }
    return 0;
}