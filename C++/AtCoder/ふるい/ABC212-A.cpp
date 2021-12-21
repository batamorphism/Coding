// Copyright
#include<bits/stdc++.h>

void solver(int a, int b) {
    std::string ans;
    if (0 < a && b == 0) {
        ans = "Gold";
    } else if (a == 0 && 0 < b) {
        ans = "Silver";
    } else {
        ans = "Alloy";
    }
    std::cout << ans << std::endl;
}

int main() {
    int a, b;
    std::cin >> a >> b;
    solver(a, b);
}