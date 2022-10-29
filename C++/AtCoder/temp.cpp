#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
    // 配るDP
    int n;
    const int int_max = 1000000000;
    cin >> n;
    // A[i] = iからi+1へのコスト
    // B[i] = iからi+2へのコスト
    vector<int> A(n+2, int_max), B(n+2, int_max);
    vector<int> DP(n+2, int_max);
    for (int i = 2; i <= n; i++) {
        cin >> A[i-2];
    }
    for (int i = 3; i <= n; i++) {
        cin >> B[i-3];
    }
    DP[0] = 0;
    for (int i = 0; i < n; i++) {
        DP[i+1] = min(DP[i+1], DP[i] + A[i]);
        DP[i+2] = min(DP[i+2], DP[i] + B[i]);
    }
    cout << DP[n-1] << endl;
    return 0;
}