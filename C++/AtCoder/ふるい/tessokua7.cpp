// copyright
#include<iostream>
#include<vector>
using namespace std;

int main() {
    int d, n;
    cin >> d >> n;
    vector<int> imos(d+10);
    for (int i = 0; i < n; i++) {
        int l, r;
        cin >> l >> r;
        imos[l]++;
        imos[r+1]--;
    }

    // accum
    for (int i = 1; i < imos.size(); i++) {
            imos[i] += imos[i-1];
    }

    for (int day = 1; day <= d; day++) {
        cout << imos[day] << endl;
    }
}
