// copyright
#include<bits/stdc++.h>
int end = 10000010;
int m = static_cast<int>(pow(10000010, 0.5))+10;
bool is_prime[10000010];
int div_num[10000010];

int cnt_factor(int num) {
    std::set<int> factor;
    while (num != 1) {
        factor.emplace(div_num[num]);
        num = num / div_num[num];
    }
    return factor.size();
}

int main() {
    int n, k = 0;
    std::cin >> n >> k;
    for (int i = 0; i < end; i++) {
        div_num[i] = i;
        is_prime[i] = true;
    }

    is_prime[0] = false;
    is_prime[1] = false;

    for (int num = 0; num < m; num++) {
        if (is_prime[num]) {
            for (int not_prime = num*num; not_prime < end; not_prime += num) {
                is_prime[not_prime] = false;
                div_num[not_prime] = std::min(num, div_num[not_prime]);
            }
        }
    }

    int ans = 0;
    for (int num = 2; num < n+1; num++) {
        if (cnt_factor(num) >= k) {
            ans++;
        }
    }
    std::cout << ans << std::endl;
}
