// copyright
#include<bits/stdc++.h>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> A(n);  // かかる時間
    std::vector<int> P(n);  // 価格
    std::vector<int> X(n);  // 在庫

    for (int i = 0; i < n; i++) {
        std::cin >> A[i] >> P[i] >> X[i];
    }

    // 購入できるのは、X[i]>A[i]の時
    // この場合のP[i]の最小値を求める
    int cost = 1001001001;
    for (int i = 0; i < n; i++) {
        if (X[i] > A[i]) {
            cost = std::min(cost, P[i]);
        }
    }

    if (cost == 1001001001)
        cost = -1;

    std::cout << cost << std::endl;
}
