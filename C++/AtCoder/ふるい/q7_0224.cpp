// copyright
#include<bits/stdc++.h>

int64_t div_sum(int64_t num) {
    // numの約数の総和
    int64_t ans = 1;
    for (int i = 2; i*i <= num; i++) {
        if (num % i == 0) {
            ans += i;
            if (i != num / i) {
                ans += num / i;
            }
        }
    }
    return ans;
}

int main() {
    int n_end = 1000000+1;
    std::vector<std::pair<int, int>> ans_list;
    for (int n = 2; n < n_end; n++) {
        int ds = div_sum(n);
        if (ds > n && n == div_sum(ds)) {
            ans_list.emplace_back(std::make_pair(n, ds));
        }
    }
    for (auto p : ans_list) {
        std::cout << p.first << " " << p.second << std::endl;
    }
    return 0;
}
