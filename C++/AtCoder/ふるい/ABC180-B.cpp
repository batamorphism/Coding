// copyright
#include<bits/stdc++.h>

double manhattan(std::vector<int> x) {
    double ret = 0.;
    for (int point : x) {
        ret += abs(point);
    }
    return ret;
}

double euclid(std::vector<int> x) {
    double sum_square = 0.;
    for (int point : x) {
        sum_square += pow(point, 2);
    }
    return pow(sum_square, 0.5);
}

double chebyshev(std::vector<int> x) {
    double ret = -INFINITY;
    for (int point : x) {
        if (ret < abs(point)) {
            ret = abs(point);
        }
    }
    return ret;
}

int main() {
    // input
    int n;
    std::cin >> n;
    std::vector<int> x(n);
    for (int i = 0; i < n; i++) {
        int foo = 0;
        std::cin >> foo;
        x[i] = foo;
    }
    double ans1, ans2, ans3;
    ans1 = manhattan(x);
    ans2 = euclid(x);
    ans3 = chebyshev(x);
    std::cout << std::setprecision(14) << ans1 << std::endl;
    std::cout << std::setprecision(14) << ans2 << std::endl;
    std::cout << std::setprecision(14) << ans3 << std::endl;
}
