// copyright
# include<bits/stdc++.h>

int main() {
    std::string x;
    std::cin >> x;
    int pos = 0;
    pos = x.find('.');
    std::cout << x.substr(0, pos) << std::endl;
}
