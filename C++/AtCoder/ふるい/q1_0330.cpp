// copyright
#include<iostream>
int main() {
    int n;
    std::cin >> n;
    int ans = 0;

    for (int val = 0; val <= n; val++) {
        if (val % 3 == 0 || val % 5 == 0) {
            ans += val;
        }
    }
    std::cout << ans << std::endl;
}
