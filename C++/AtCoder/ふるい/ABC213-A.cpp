// copyright
#include<bits/stdc++.h>

void solv(int a, int b) {
    /**
     * @brief
     * a xor c = bとなる整数cを求めよ
     */
    int c;
    c = a ^ b;
    std::cout << c << std::endl;
}

int main() {
    int a, b;
    std::cin >> a >> b;
    solv(a, b);
}