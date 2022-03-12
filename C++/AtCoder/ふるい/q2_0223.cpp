// copyright
#include<bits/stdc++.h>

int gcd(int a, int b) {
    return b ? gcd(b, a % b) : a;
}

int main() {
    int n, m;
    std::cin >> n >> m;
    int ans = gcd(n, m);
    std::cout << ans << std::endl;
    return 0;
}
