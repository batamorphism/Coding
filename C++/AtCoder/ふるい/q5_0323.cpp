// copyright
#include<iostream>
#include<vector>

int main() {
    int n;
    std::cin >> n;

    std::vector<bool> is_prime(n+1, true);

    is_prime[0] = false;
    is_prime[1] = false;
    for (int val = 2; val <= n; val++) {
        if (is_prime[val]) {
            for (int i = val * 2; i <= n; i += val) {
                is_prime[i] = false;
            }
        }
    }

    for (int val = 2; val <= n-6; val++) {
        if (is_prime[val] && is_prime[val+6]) {
            std::cout << val << " " << val+6 << std::endl;
        }
    }
}
