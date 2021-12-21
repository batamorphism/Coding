// copyright
#include<bits/stdc++.h>

int solver(int n, int a, int b) {
    return n-a+b;
}

int main() {
    // input
    int n, a, b;
    std::cin >> n >> a >> b;
    int ans;
    ans = solver(n, a, b);
    std::cout << ans << std::endl;
}