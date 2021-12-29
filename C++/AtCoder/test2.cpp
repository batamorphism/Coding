// copyright
# include <bits/stdc++.h>
int main() {
    int n;
    double x = 0.75;
    n = x*100;
    double ans = 0.;
    ans = n / 100;  // <-これは切り捨て除算
    std::cout << ans << std::endl;
    return 0;
}
