// copyright
#include<iostream>

int gray_encode(int n) {
    return n ^ (n >> 1);
}

int gray_decode(int n) {
    int ret = 0;
    while (n) {
        ret ^= n;
        n >>= 1;
    }
    return ret;
}

int main() {
    int n;
    std::cin >> n;
    auto g = gray_encode(n);
    std::cout << g << std::endl;
    auto b = gray_decode(g);
    std::cout << b << std::endl;
    return 0;
}
