// copyright
#include<bits/stdc++.h>

std::pair<int64_t, int64_t> longest_collatz(int64_t const limit) {
    // [初項, 長さ]からなるpairを返す
    int64_t len = 0;
    int64_t num = 0;
    std::vector<int64_t> cache(limit + 1, 0);

    for (int64_t i = 2; i <= limit; i++) {
        auto n = i;
        int64_t steps = 0;
        while (n != 1 && n >= i) {
            if ((n % 2) == 0) {
                n = n/2;
            } else {
                n = 3*n + 1;
            }
            steps++;
        }
        cache[i] = steps + cache[n];
        if (cache[i] > len) {
            len = cache[i];
            num = i;
        }
    }

    return std::make_pair(num, len);
}

int main() {
    auto [n, m] = longest_collatz(1000000);
    std::cout << n << ' ' << m << std::endl;
    return 0;
}
