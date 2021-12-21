// Copyright
#include<bits/stdc++.h>

int main() {
    std::string s;
    std::cin >> s;
    int ans=0;
    for (int i = 0; i < 10000; i++) {
        std::vector<bool> is_exist(10);
        int x = i;
        for (int j = 0; j < 4; j++) {
            is_exist[x%10] = true;
            x = x/10;
        }
        bool is_ok = true;
        for (int j = 0; j < 10; j++) {
            if (s[j] == 'o') {
                if (!is_exist[j]) {
                    is_ok = false;
                }
            } else if (s[j] == 'x') {
                if (is_exist[j]) {
                    is_ok = false;
                }
            }
        }
        if (is_ok) {
            ans += 1;
        }
    }
    std::cout << ans << std::endl;
}


