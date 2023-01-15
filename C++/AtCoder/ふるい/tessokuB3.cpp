// copyright
#include<iostream>
#include<vector>
using namespace std;

int main() {
    // input
    int n;
    cin >> n;
    auto a_list = vector<int>(n);
    for (int i = 0; i < n; i++) {
        cin >> a_list[i];
    }

    for (int i1 = 0; i1 < n; i1++) {
        for (int i2 = 0; i2 < n; i2++) {
            if (i1 == i2) continue;
            for (int i3 = 0; i3 < n; i3++) {
                if (i1 == i3) continue;
                if (i2 == i3) continue;

                auto a1 = a_list[i1];
                auto a2 = a_list[i2];
                auto a3 = a_list[i3];
                auto sum_ = a1 + a2 + a3;
                if (sum_ == 1000) {
                    cout << "Yes" << endl;
                    return 0;
                }
            }
        }
    }
    cout << "No" << endl;
    return 0;
}