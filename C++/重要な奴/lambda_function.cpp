// copyright
#include <bits/stdc++.h>
int main() {
    auto f = [](int x) { return x * x; };
    auto g = [](int x) { return x + x; };
    auto h = [=](int x) { return f(x)*g(x); };
    std::cout << h(1) << std::endl;
}
