// Copyright
#include<bits/stdc++.h>

int main() {
    // input
    std::vector<int> a(3);
    std::cin >> a[0] >> a[1] >> a[2];
    std::sort(a.begin(), a.end());
    if (a[2]-a[1] == a[1]-a[0]) {
        std::cout << "Yes" << std::endl;
    } else {
        std::cout << "No" << std::endl;
    }
}
