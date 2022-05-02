// copyright
#include<iostream>
#include<array>
#include<vector>

int main() {
    // 不便さの変化幅で管理する
    int n, q;
    std::cin >> n >> q;
    // こういう描き方もできるのね
    // auto A = std::vector{n, std::vector{n, std::vector{n, 0}}};
    auto A = std::vector<int64_t>{n, 0};
    for (int i = 0; i < n; i++) {
        std::cin >> A[i];
    }

    using QUERY = std::array<int64_t, 3>;
    //auto query_list = std::vector<QUERY>(q, QUERY{});
    auto query_list = std::vector<QUERY>(q);
1000
    for (int i = 0; i < q; i++) {
        QUERY query;
        std::cin >> query[0] >> query[1] >> query[2];
        query[0]--;
        query[1]--;
        query_list[i] = query;
    }

    // 不便さの合計を求めておく
    int64_t ans = 0;
    for (int i = 0; i < n-1; i++) {
        auto bef_a = A[i];
        auto aft_a = A[i+1];
        ans += std::abs(bef_a - aft_a);
    }

    for (auto query : query_list) {
        auto [le, ri, val] = query;
        // le-1 -> leが、le側が+valされ
        // ri -> ri+1が-valされる
        auto cur_ans = ans;
        if (le-1 >= 0) {
            auto pre_bef_a = A[le-1];
            auto pre_aft_a = A[le];
            auto pre_val = std::abs(pre_bef_a - pre_aft_a);
            auto aft_val = std::abs(pre_bef_a - (pre_aft_a + val));
            cur_ans += aft_val - pre_val;
        }
        if (ri+1 < n) {
            auto pre_bef_a = A[ri];
            auto pre_aft_a = A[ri+1];
            auto pre_val = std::abs(pre_bef_a - pre_aft_a);
            auto aft_val = std::abs(pre_bef_a - (pre_aft_a - val));
            cur_ans += aft_val - pre_val;
        }
        std::cout << cur_ans << std::endl;
    }
}
