// copyright
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    vector<int> A(n);
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }

    // しゃくとり法
    deque<int> deq;
    int64_t ans = 0;
    for (const auto& a : A) {
        deq.push_back(a);
        // deqのminとmaxの差がk以下になるまで、deqの先頭をpop
        while (deq.back() - deq.front() > k) {
            deq.pop_front();
        }
        // 追加したaを片方選ぶパターン数はn-1
        auto n = deq.size();
        ans += (n-1);
    }
    cout << ans << endl;

    return 0;
}
