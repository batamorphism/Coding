// copyright
#include<bits/stdc++.h>
bool is_prime(int val) {
    for (int i = 2; i * i <= val; i++) {
        if (val % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int num;
    std::cin >> num;
    int ans;
    ans = -1;

    for (int x = num; num >= 1; x--) {
        if (is_prime(x)) {
            ans = x;
            break;
        }
    }
    std::cout << ans << std::endl;
    return 0;
}
