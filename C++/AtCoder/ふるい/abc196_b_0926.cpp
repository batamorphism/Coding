// copyright
#include<bits/stdc++.h>
int main() {
    std::string x;
    std::cin >> x;
    int find_ind = x.find('.');
    std::string ans;
    ans = x.substr(0, find_ind);
    std::cout << ans << std::endl;
}
