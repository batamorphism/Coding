// copyright
#include<bits/stdc++.h>
int main() {
    std::string S;
    std::cin >> S;
    std::string ans;
    ans = S.substr(1, S.length()-1) + S[0];
    std::cout << ans << std::endl;
}
