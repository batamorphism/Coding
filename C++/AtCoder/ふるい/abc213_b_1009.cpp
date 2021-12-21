// copyright
#include<bits/stdc++.h>
int main() {
    int n;
    std::cin >> n;
    std::vector<std::pair<int, int>> A(n);
    for (int i = 0; i < n; i++) {
        std::cin >> A[i].first;
        A[i].second = i+1;
    }
    std::sort(A.begin(), A.end());
    std::cout << A[n-2].second << std::endl;
}
