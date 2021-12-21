// Copyright
#include<bits/stdc++.h>

void solver(int a, int b) {
    double ans;
    ans = (a-b)/3.+b;
    std::cout << std::setprecision(10) << ans << std::endl;
}


int main() {
    // input
    int a, b;
    std::cin >> a >> b;
    solver(a, b);
}
