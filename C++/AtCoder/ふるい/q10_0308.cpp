// copyright
#include<iostream>

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
    auto gray = gray_encode(n);
    std::cout << gray << std::endl;
    auto dec = gray_decode(gray);
    std::cout << dec << std::endl;
    return 0;
}
