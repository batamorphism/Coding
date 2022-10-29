// copyright
#include<iostream>
#include<vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> A(n);
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }

    int q;
    cin >> q;
    using query_t = pair<int, int>;
    vector<query_t> query_list(q);
    for (int i = 0; i < q; i++) {
        int l, r;
        cin >> l >> r;
        l--;
        r--;
        query_list[i] = {l, r};
    }

    // accum
    for (int i = 1; i < A.size(); i++) {
            A[i] += A[i-1];
    }

    for (auto [l, r] : query_list) {
        int true_cnt = 0;
        if (l == 0) {
            true_cnt = A[r];
        } else {
            true_cnt = A[r] - A[l-1];
        }
        auto false_cnt = (r - l + 1) - true_cnt;
        if (true_cnt == false_cnt) {
            cout << "draw" << endl;
        } else if (true_cnt > false_cnt) {
            cout << "win" << endl;
        } else if (true_cnt < false_cnt) {
            cout << "lose" << endl;
        }
    }
}
