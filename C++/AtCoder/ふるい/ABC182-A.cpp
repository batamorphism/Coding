// Copyright
#include<bits/stdc++.h>

void solver(int a, int b) {
    int max_num;
    int ans = 0;
    max_num = 2*a+100;
    ans = max_num-b;
    std::cout << ans << std::endl;
}

int main() {
    // input
    int a, b;
    std::cin >> a >> b;
    solver(a, b);
}
