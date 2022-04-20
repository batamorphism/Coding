// copyright
#include<iostream>
#include<array>

void longest_collaz() {
    constexpr int64_t n_end = 1000001;
    std::cout << "test1" << std::endl;
    static std::array<int64_t, n_end> memo;
    std::cout << "test2" << std::endl;
    memo[1] = 1;
    for (int64_t n = 1; n < n_end; n++) {U
        // memoに値が存在するまでループする
        if (n % 1000 == 0) {
            std::cout << n << std::endl;
        }
        int64_t step = 0;
        auto cur_n = n;
        auto pre_n = cur_n;
        auto test_n = cur_n;
        while (cur_n >= n_end || memo[cur_n] == 0) {
            step++;
            if (cur_n % 2 == 0) {
                cur_n /= 2;
            } else {
                cur_n = 3 * cur_n + 1;
            }
            pre_n = cur_n;
            test_n = pre_n * 3 + 1;
        }
        memo[n] = memo[cur_n] + step;
    }
    std::cout << memo[100] << std::endl;
}

int main() {
    longest_collaz();
}
