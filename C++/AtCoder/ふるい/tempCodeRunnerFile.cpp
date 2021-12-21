// copyright
#include<bits/stdc++.h>
int main() {
    int r_end, c_end, n = 0;
    std::cin >> r_end >> c_end >> n;
    int DP_R[c_end];
    int DP_C[r_end];
    int DP[r_end][c_end];
    for (int64_t c = 0; c < c_end; c++) {
        DP_R[c] = 0;
    }
    for (int64_t r = 0; r < r_end; r++) {
        DP_C[r] = 0;
    }
    for (int64_t r = 0; r < r_end; r++) {
        for (int64_t c = 0; c < c_end; c++) {
            DP[r][c] = 0;
        }
    }

    std::vector<std::pair<int64_t, std::pair<int64_t, int64_t>>> node_list;
    std::vector<std::pair<int64_t, std::pair<int64_t, int64_t>>> node_list_ori;
    for (int64_t i = 0; i < n; i++) {
        int64_t r, c, a;
        std::cin >> r >> c >> a;
        r--;
        c--;
        node_list.emplace_back(std::make_pair(a, std::make_pair(r, c)));
        node_list_ori.emplace_back(std::make_pair(a, std::make_pair(r, c)));
    }
    std::sort(node_list.begin(), node_list.end());

    for (auto node : node_list) {
        auto rc = node.second;
        auto r = rc.first;
        auto c = rc.second;
        int64_t dp = 0;
        dp = std::max(DP_R[c]+1, dp);
        dp = std::max(DP_C[r]+1, dp);
        DP_R[c] = dp;
        DP_C[r] = dp;
        DP[r][c] = dp;
    }

    for (auto node : node_list_ori) {
        auto rc = node.second;
        auto r = rc.first;
        auto c = rc.second;
        std::cout << DP[r][c]-1 << std::endl;
    }
}
