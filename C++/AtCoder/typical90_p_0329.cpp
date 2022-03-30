// copyright
#include<iostream>
#include<vector>
#include<limits>

int main() {
    int64_t n, a, b, c;
    std::cin >> n >> a >> b >> c;

    // a, bを全探索
    int64_t cnt_end = 10000;
    int64_t ans = std::numeric_limits<int64_t>::max();
    for (int64_t a_cnt = 0; a_cnt < cnt_end; a_cnt++) {
        for (int64_t b_cnt = 0; b_cnt < cnt_end; b_cnt++) {
            if (a_cnt+b_cnt > cnt_end) break;

            int64_t ab_sum = a*a_cnt + b*b_cnt;
            if (ab_sum > n) break;

            int64_t c_sum = n-ab_sum;
            if (c_sum % c != 0) continue;
            int64_t c_cnt = c_sum / c;
            int64_t abc_cnt = a_cnt + b_cnt + c_cnt;
            ans = std::min(ans, abc_cnt);
        }
    }
    std::cout << ans << std::endl;
    return 0;
}
