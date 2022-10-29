// copyright
// 答えで2分探索
#include<iostream>
#include<vector>
#include<array>
#include<limits>
#include<algorithm>

using HS = std::array<int64_t, 2>;

bool check(const int64_t& mid, const std::vector<HS>& hs, const int n) {
    // 全ての風船を、高度mid以下で割ることができるか
    // 各風船を(mid-h_i) / s_i 秒以内に割ればよい
    std::vector<int64_t> time_limit;
    for (const auto& [h_i, s_i] : hs) {
        if (mid - h_i < 0) {
            return false;
        }
        time_limit.push_back((mid - h_i) / s_i);
    }

    std::sort(time_limit.begin(), time_limit.end());

    for (int64_t cur_time = 0; cur_time < n; cur_time++) {
        if (cur_time > time_limit[cur_time]) {
            return false;
        }
    }
    return true;
}

int main() {
    int n;
    std::cin >> n;
    std::vector<HS> hs(n);
    for (int i = 0; i < n; i++) {
        std::cin >> hs[i][0] >> hs[i][1];
    }

    int64_t ok = std::numeric_limits<int64_t>::max();
    int64_t ng = 0;
    while ((ok - ng) > 1) {
        auto mid = (ok + ng) / 2;
        if (check(mid, hs, n)) {
            ok = mid;
        } else {
            ng = mid;
        }
    }

    std::cout << ok << std::endl;
}
