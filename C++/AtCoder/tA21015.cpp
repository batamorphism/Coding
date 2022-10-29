// copyright

#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main() {
    int n, x;
    cin >> n >> x;
    vector<int> A(n);
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }

    auto ans = false;
    for (auto a_i : A) {
        if (a_i == x) {
            ans = true;
            break;
        }
    }
    cout << (ans ? "Yes" : "No") << endl;
}
