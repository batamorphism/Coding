// copyright
#include<bits/stdc++.h>
std::vector<int> calc_divisors(int n) {
    // nの約数を全列挙する
    std::vector<int> divisors;
    divisors.emplace_back(1);
    divisors.emplace_back(n);
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            divisors.emplace_back(i);
            if (i * i != n) {
                divisors.emplace_back(n / i);
            }
        }
    }
    return divisors;
}

int solve(int n) {
    // nの約数の総和からnを引いたものを返す
    auto divisors = calc_divisors(n);
    /*
    std::cout << n << "divisors: ";
    for (auto d : divisors) {
        std::cout << d << " ";
    }
    std::cout << std::endl;
    */
    int sum = 0;
    for (auto d : divisors) {
        sum += d;
    }
    return sum - n;
}

int main() {
    int n;
    std::cin >> n;
    for (int i = 1; i <= n; i++) {
        int ans;
        ans = solve(i);
        if (ans > i) {
            std::cout << i << " " << ans << std::endl;
        }
    }
}