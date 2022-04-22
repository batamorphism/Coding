// copyright
#include<iostream>

int div_cnt(int n) {
    // 整数nの約数の数を数える
    // 試し割り法
    int cnt = 0;
    for (int div = 1; div * div <= n; div++) {
        if (n % div == 0) {
            if (div * div != n) {
                cnt += 2;
            } else {
                cnt += 1;
            }
        }
    }
    return cnt;
}

int main() {
    int n_end;
    std::cin >> n_end;
    n_end++;

    int ans = 0;
    for (int n = 1; n < n_end; n+=2) {
        // nは奇数
        auto cnt = div_cnt(n);
        if (cnt == 8) ans++;
    }

    std::cout << ans << std::endl;
}