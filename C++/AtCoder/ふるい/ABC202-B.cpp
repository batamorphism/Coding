// Copyright
#include<bits/stdc++.h>

int main() {
    std::string s;
    std::cin >> s;
    std::string ans;
    ans = s;
    int n;
    n = s.length();
    for (int i = 0; i < n; i++) {
        char foo;
        foo = s[i];
        if (foo =='6') {
            foo = '9';
        } else if (foo =='9') {
            foo = '6';
        }
        ans[n-i-1] = foo;
    }
    std::cout << ans << std::endl;
}
