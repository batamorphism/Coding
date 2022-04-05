// copyright
#include<iostream>
#include<vector>
#include<utility>

std::vector<int> calc_div_prime(int n) {
    std::vector<int> ret;
    for (int i = 2; i*i <= n; i++) {
        while (n % i == 0) {
            ret.push_back(i);
            n /= i;
        }
    }
    if (n != 1) {
        ret.push_back(n);
    }
    return std::move(ret);
}

int main() {
    int n;
    std::cin >> n;

    auto div_prime = calc_div_prime(n);
    for (auto div : div_prime) {
        std::cout << div << " ";
    }
}
