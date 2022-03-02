// copyright
#include<bits/stdc++.h>

int gcd(int a, int b) {
    return b ? gcd(b, a % b) : a;
}

int lcm(int a, int b) {
    return a / gcd(a, b) * b;
}

int main() {
    int n;
    std::cin >> n;
    std::vector<int> number_list(n);
    for (int i = 0; i < n; i++) {
        std::cin >> number_list[i];
    }
    int ans = std::accumulate(number_list.begin(), number_list.end(), 1, lcm);
    std::cout << ans << std::endl;
    return 0;
}
