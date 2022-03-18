// copyright
#include<iostream>
#include<vector>
int main() {
    int64_t n_max = 1000000;

    std::vector<int64_t> length(n_max+1, -1);
    length[1] = 1;

    for (int64_t n = 2; n <= n_max; n++) {
        int64_t cur_n = n;
        int64_t cnt = 0;
        while (!(cur_n <= n_max && length[cur_n] != -1)) {
            cnt++;
            if (cur_n % 2 == 0) {
                cur_n = cur_n /2;
            } else {
                cur_n = 3 * cur_n + 1;
            }
        }
        length[n] = cnt + length[cur_n];
    }

    int64_t ans = 0;
    for (auto len : length) {
        if (len > ans) {
            ans = len;
        }
    }
    std::cout << ans << std::endl;
}
