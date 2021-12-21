// copyright
#include<bits/stdc++.h>
int lcs(std::string x, std::string y) {
    // DP[i][j] = x[:i] y[:j]のlcs
    int max_i = x.length();
    int max_j = y.length();
    int DP[max_i+1][max_j+1];
    for (int i = 0; i <= max_i; i++) {
        for (int j = 0; j <= max_j; j++) {
            DP[i][j] = 0;
        }
    }

    for (int i = 0; i <= max_i; i++) {
        for (int j =  0; j <= max_j; j++) {
            if (i == 0 || j == 0) {
                DP[i][j] = 0;
                continue;
            }
            if (x[i-1] == y[j-1]) {
                DP[i][j] = std::max({DP[i-1][j-1]+1, DP[i][j-1], DP[i-1][j]});
            } else {
                DP[i][j] = std::max({DP[i-1][j-1], DP[i][j-1], DP[i-1][j]});
            }
        }
    }

    return DP[max_i][max_j];
}
int main() {
    int n;
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        std::string x;
        std::string y;
        std::cin >> x >> y;
        int ans;
        ans = lcs(x, y);
        std::cout << ans << std::endl;
    }
}
