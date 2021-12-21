// copyright
#include<bits/stdc++.h>

/**
 * @brief solver
 * 1～6の出目があるさいころをa回降って、出た目の合計がbになるか
 * つまり、a<=b<=6*aを満たすか
 * @param a 
 * @param b 
 * @return true 
 * @return false 
 */
bool solver(int a, int b) {
    return a <= b && b <= 6*a;
}

int main() {
    // input
    int a, b;
    std::cin >> a >> b;
    bool ans;
    ans = solver(a, b);
    if (ans) {
        std::cout << "Yes" << std::endl;
    } else {
        std::cout << "No" << std::endl;
    }
}
