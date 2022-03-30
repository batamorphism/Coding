// copyright
#include<bits/stdc++.h>
int main() {
    int n_max;
    std::cin >> n_max;

    std::vector<bool> is_prime(n_max + 1, true);
    is_prime[0] = false;
    is_prime[1] = false;
    for (int i = 2; i <= n_max; i++) {
        if (is_prime[i]) {
            for (int j = i * i; j <= n_max; j += i) {
                is_prime[j] = false;
            }
        }
    }

    std::vector<std::pair<int, int>> ans_list;
    for (int n = 6; n <= n_max; n++) {
        if (is_prime[n] && is_prime[n-6]) {
            ans_list.emplace_back(std::make_pair(n, n-6));
        }
    }

    for (auto p : ans_list) {
        std::cout << p.second << " " << p.first << std::endl;
    }

    return 0;
}
