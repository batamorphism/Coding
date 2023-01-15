// copyright
#include<iostream>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    auto ans = 0;

    for (int r = 1; r <= n; r++) {
        for (int b = 1; b <= n; b++) {
            auto w = k - r - b;
            if (w > 0 && w <= n) {
                ans += 1;
            }
        }
    }
    cout << ans;
    return 0;
}