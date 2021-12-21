// copyright
#include<bits/stdc++.h>

void solver(int n, std::vector<int> A, std::vector<int> B);

int main() {
    // input
    int n;
    std::cin >> n;
    // 変数を使って配列の長さを変えたい場合は、vector型にする
    std::vector<int> A(n);
    std::vector<int> B(n);
    for (int i = 0; i < n; i++) {
        std::cin >> A[i] >> B[i];
    }
    solver(n, A, B);
}

void solver(int n, std::vector<int> A, std::vector<int> B) {
    /**
     * @brief
     * 高橋君はn回操作し、黒板に整数を書く
     * i回目の操作では、A[i]以上B[i]以下の整数すべてを1個ずつ書く
     * n回の操作を終えたときの合計の数を求めよ
     */
    int64_t ans = 0;
    for (int i = 0; i < n; i++) {
        ans += static_cast<int64_t>((A[i]+B[i])/2.*(-A[i]+B[i]+1));
    }
    std::cout << ans << std::endl;
}
