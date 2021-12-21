// Copyright
#include<bits/stdc++.h>

void solver(int n, int a, int x, int y) {
    /**
     * @brief 
     * キャベツ1個x円
     * ただし、a+1個目以降は1個y円
     */
    int ans = 0;
    if (n <= a) {
        ans = n*x;
    } else {
        ans = a*x+(n-a)*y;
    }
    std::cout << ans << std::endl;
}

int main() {
    // input
    int n, a, x, y;
    std::cin >> n >> a >> x >> y;
    solver(n, a, x, y);
}