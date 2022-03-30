// copyright
#include<bits/stdc++.h>

int gray_encode(int n) {
    return n ^ (n >> 1);
}

int gray_decode(int n) {
    int res = 0;
    while (n) {
        res ^= n;
        n >>= 1;
    }
    return res;
}

int main() {
    int n;
    std::cin >> n;
    auto g_n = gray_encode(n);
    std::cout << g_n << std::endl;
    auto b_n = gray_decode(g_n);
    std::cout << b_n << std::endl;
    return 0;
}
