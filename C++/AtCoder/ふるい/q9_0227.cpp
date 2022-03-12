// copyright
#include<bits/stdc++.h>
int div_of(int n) {
    for (int m = 2; m * m <= n; m++) {
        if (n % m == 0) {
            return m;
        }
    }
    return n;
}

int main() {
    int n;
    std::cin >> n;
    std::vector<int> ans_list;

    while (n > 1) {
        int div = div_of(n);
        n /= div;
        ans_list.emplace_back(div);
    }
    for (auto ans : ans_list) {
        std::cout << ans << std::endl;
    }
    return 0;
}
