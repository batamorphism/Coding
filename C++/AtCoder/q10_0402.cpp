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
    int n = 123;
    auto g = gray_encode(n);
    std::cout << g << std::endl;
    auto b = gray_decode(g);
    std::cout << b << std::endl;
}