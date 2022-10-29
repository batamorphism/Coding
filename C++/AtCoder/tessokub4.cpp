// copyright
#include<iostream>
#include<string>
using namespace std;

int main() {
    string n;
    cin >> n;

    auto ans = 0;
    for (auto c : n) {
        ans *= 2;
        if (c == '1') {
            ans += 1;
        }
    }
    cout << ans;
}
