// copyright
#include<bits/stdc++.h>
int main() {
    std::string x;
    std::cin >> x;
    int pos_of_period = x.find('.');
    std::cout << x.substr(0, pos_of_period) << std::endl;
}
