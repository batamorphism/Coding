// copyright
#include<bits/stdc++.h>
int main() {
    double a, b;
    std::cin >> a >> b;
    double ans;
    ans = (1.-b/a)*100.;
    std::cout << std::setprecision(16) << ans << std::endl;
}
