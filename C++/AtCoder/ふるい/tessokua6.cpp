// copyright
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
    int n, q;
    cin >> n >> q;
    vector<int> A(n);
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }

    using query_t = pair<int, int>;
    vector<query_t> query_list(q);
    for (int i = 0; i < q; i++) {
        int l, r;
        cin >> l >> r;
        l--;
        r--;
        query_list[i] = make_pair(l, r);
    }

    // accum
    for (int i = 1; i < A.size(); i++) {
            A[i] += A[i-1];
    }

    for (auto [l, r] : query_list) {
        if (l == 0) {
            cout << A[r] << endl;
        } else {
            cout << A[r] - A[l-1] << endl;
        }
    }
}