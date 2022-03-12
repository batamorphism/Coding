// copyright
#include<bits/stdc++.h>
int main() {
    int n;
    std::cin >> n;

    int64_t sum_ = 0;
    for (int x = 1; x <= n; x++) {
        if (x % 3 == 0 || x % 5 == 0) {
            sum_ += x;
        }
    }
    std::cout << sum_ << std::endl;
    return 0;
}
