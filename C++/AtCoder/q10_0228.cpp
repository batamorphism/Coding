// copyright
#include<bits/stdc++.h>

int64_t gray_encode(int64_t n) {
    return n ^ (n >> 1);
}

int64_t gray_decode(int64_t n) {
    int64_t res = 0;
    while (n) {
        res ^= n;
        n >>= 1;
    }
    return res;
}

int main() {
    for (int64_t bit = 0; bit < 16; bit++) {
        int64_t n_gray = 1 << bit;
        std::cout << "---" << std::endl;
        std::cout << gray_decode(n_gray) << std::endl;
        std::cout << gray_decode(n_gray ^ (1 << 10)) << std::endl;
    }
    return 0;
}
