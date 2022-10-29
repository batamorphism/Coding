// copyright
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    auto ans = false;
    for (int val = a; val <= b; val++) {
        if (100 % val == 0) ans = true;
    }

    cout << (ans ? "Yes" : "No") << endl;
}
