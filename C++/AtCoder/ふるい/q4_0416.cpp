// copyright
#include<iostream>

bool is_prime(int x) {
    if (x == 1) return false;

    for (int n = 2; n * n <= x; n++) {
        if (x % n == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int n_end = 100;
    for (int n = 1; n < n_end; n++) {
        if (is_prime(n)) {
            std::cout << n << std::endl;
        }
    }
}