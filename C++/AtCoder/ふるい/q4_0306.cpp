// copyright
#include<bits/stdc++.h>

bool is_prime(int p) {
    if (p <= 1) return false;
    for (int i = 2; i * i <= p; i++) {
        if (p % i == 0) return false;
    }
    return true;
}

int main() {
    int n;
    std::cin >> n;

    for (int p = n; p >= 1; p--) {
        if (is_prime(p)) {
            std::cout << p << std::endl;
            return 0;
        }
    }
    std::cout << "NA" << std::endl;
    return 0;
}