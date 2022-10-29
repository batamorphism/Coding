// copyright
#include<iostream>
#include<vector>
#include<array>
#include<algorithm>

void solve(int n, const std::vector<int>& w) {
    n++;
    std::vector<std::vector<int>> dp(n, std::vector<int>(n, 0));
    for (int cur_cnt = 2; cur_cnt < n; cur_cnt++) {
        for (int cur_le = 0; cur_le < n; cur_le++) {
            auto cur_ri = cur_le + cur_cnt;
            if (cur_ri >= n) break;
            // 1. 新たにw[cur_le]とw[cur_ri-1]を取り除く
            auto pre_le = cur_le+1;
            auto pre_ri = cur_ri-1;
            auto pre_cnt = cur_cnt-2;
            if (dp[pre_le][pre_ri] == pre_cnt) {
                // 一手前の段階ですべて取れているので、遷移可能
                if (std::abs(w[cur_le] - w[cur_ri-1]) <= 1) {
                    dp[cur_le][cur_ri] = dp[pre_le][pre_ri]+2;
                }
            }

            // 2. dp[le][sep]とdp[sep][ri]から遷移する
            for (int sep = cur_le; sep <= cur_ri; sep++) {
                auto pre_dp = dp[cur_le][sep] + dp[sep][cur_ri];
                dp[cur_le][cur_ri] = std::max(dp[cur_le][cur_ri], pre_dp);
            }
        }
    }

    auto ans = dp[0][n-1];
    std::cout << ans << std::endl;
}

int main() {
    // 区間DP
    // 貰うDP
    // DP[le][ri] = [le, ri)を見た状態における、取り除けたブロックの個数の最大値
    while (true) {
        int n;
        std::cin >> n;
        if (n == 0) return 0;
        std::vector<int> w(n);
        for (int i = 0; i < n; i++) {
            std::cin >> w[i];
        }
        solve(n, w);
    }
}
