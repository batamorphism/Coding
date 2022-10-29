// copyright
#include<iostream>
#include<string>
using namespace std;

int main() {
    int n;
    cin >> n;

    string ans = "";
    for (int i = 0; i < 10; i++) {
        if (n % 2 == 1) {
            // 左端に1を追加
            ans = "1" + ans;
        } else {
            // 左端に0を追加
            ans = "0" + ans;
        }
        n /= 2;
    }
    cout << ans;
}
