// copyright
#include<iostream>
// 友愛数
// 自分自身を除いた約数の和が、互いに他方と等しくなるような数

int64_t calc_divisor_sum(int64_t n) {
    // nの約数の総和を計算する
    // 試し割り法でいいや
    int64_t sum = 0;
    for (int64_t i = 1; i*i <= n; i++) {
        if (n % i == 0) {
            sum += i;
            if (n/i != i) {
                sum += n/i;
            }
        }
    }
    return sum-n;
}

int main() {
    const int64_t n_end = 10000001;

    for (int64_t n = 1; n < n_end; n++) {
        auto div_sum = calc_divisor_sum(n);
        if (div_sum < n_end && n < div_sum) {
            if (calc_divisor_sum(div_sum) == n) {
                std::cout << n << " " << div_sum << std::endl;
            }
        }
    }

    return 0;
}