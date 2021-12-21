// Copyright
#include<bits/stdc++.h>

void solver(int n, std::vector<std::vector<int>> a) {
    // rbeginとrendにすると降順になる
    std::sort(a.rbegin(), a.rend());
    std::cout << a[1][1] << std::endl;
}

int main() {
    // input
    int n;
    std::cin >> n;
    std::vector<std::vector<int>> a(n, std::vector<int>(2));
    int j;
    for (int i =0; i < n; i++) {
        std::cin >> j;
        a[i] = {j, i+1};
    }

    solver(n, a);
}
