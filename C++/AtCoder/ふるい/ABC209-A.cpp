// copyright
#include<bits/stdc++.h>

int solver(int a, int b) {
    if (b >= a) {
        return b-a+1;
    }
    return 0;
}

int main() {
    // input
    int a, b;
    std::cin >> a >> b;
    int ans;
    ans = solver(a, b);
    std::cout << ans << std::endl;
}
