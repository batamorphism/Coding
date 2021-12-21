// Copyright
# include<bits/stdc++.h>

int func1() {
    return 0;
}

int func2(int t) {
    if (t == 0) {
        return 0;
    }
    return func2(t-1);
}

int main() {
    int n = 1001001001;  // 10億回

    clock_t start = clock();
    for (int i = 0; i < n; i++) {
        func1();
    }
    clock_t end = clock();
    std::cout << static_cast<double>(end - start) / CLOCKS_PER_SEC << "sec.\n";

    clock_t start2 = clock();
    for (int i = 0; i < n/1200; i++) {
        func2(1200);
    }
    clock_t end2 = clock();
    std::cout << static_cast<double>(end2 - start2) / CLOCKS_PER_SEC << "sec.\n";
}
