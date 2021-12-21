// copyright
# include<bits/stdc++.h>

int main() {
    int n, k;
    std::cin >> n >> k;
    int64_t x;
    x = n;
    for (int i = 0; i < k; i++) {
        if (x%200 == 0) {
            x = x/200;
        } else {
            x = x*1000+200;
        }
    }
    std::cout << x << std::endl;
}
