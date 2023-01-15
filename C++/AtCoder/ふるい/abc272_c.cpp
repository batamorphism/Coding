// copyright

#include<iostream>
#include<map>
using namespace std;

int main() {
    int n, a;
    map<int, int> mp;

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a;
        mp[a]++;
    }

    for (auto it = mp.rbegin(); it != mp.rend(); it++) {
        cout << it->second << endl;
    }
    for (int i = 0; i < n-mp.size(); i++) {
        cout << 0 << endl;
    }
}
