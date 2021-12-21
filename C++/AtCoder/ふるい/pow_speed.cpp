// copyright namekawa
#include <bits/stdc++.h>

double powint(double a, int64_t n) {
    if (a == 0. && n == 0) {
        // 0^0問題
        return 1.;
    }
    double ret = 1.;
    while (n != 0) {
        if (n & 1) {
            ret *= a;
        }
        a *= a;
        n >>= 1;
    }
    return ret;
}

void empty_function() {
    return;
}

int main() {
    // calc speed of pow
    // a**nを計算するのにかかる時間を計測する
    // コンパイル最適化を回避するために、x, yは外部から入力する
    clock_t start;
    clock_t end;
    double a;
    int64_t n;
    std:: cin >> a >> n;
    // for文は遅いので、intvectorを使う
    int loop_end = 10000000;
    std::vector<int> iter(loop_end);

    std::cout << "case1 C pow(double, double)" << std::endl;
    // castは遅いので、先にdoubleにする
    double d_a = static_cast<double>(a);
    double d_n = static_cast<double>(n);
    start = clock();
    for (int i : iter) {
        pow(d_a, d_n);
    }
    end = clock();
    std::cout << static_cast<double>(end - start) / CLOCKS_PER_SEC << std::endl;
    //std::cout << pow(d_a, d_n) << std::endl;

    std::cout << "case2 std::pow(double, double)" << std::endl;
    start = clock();
    for (int i : iter) {
        std::pow(d_a, d_n);
    }
    end = clock();
    std::cout << static_cast<double>(end - start) / CLOCKS_PER_SEC << std::endl;
    //std::cout << std::pow(d_a, d_n) << std::endl;

    std::cout << "case3 pow_int(double, int)" << std::endl;
    start = clock();
    for (int i : iter) {
        powint(d_a, n);
    }
    end = clock();
    std::cout << static_cast<double>(end - start) / CLOCKS_PER_SEC << std::endl;
    //std::cout << powint(d_a, n) << std::endl;

    std::cout << "case4 simple" << std::endl;
    start = clock();
    for (int i : iter) {
        d_a *= d_a;
    }
    end = clock();
    std::cout << static_cast<double>(end - start) / CLOCKS_PER_SEC << std::endl;
    //std::cout << powint(d_a, n) << std::endl;

    std::cout << "case5 call func" << std::endl;
    start = clock();
    for (int i : iter) {
        empty_function();
    }
    end = clock();
    std::cout << static_cast<double>(end - start) / CLOCKS_PER_SEC << std::endl;
    //std::cout << powint(d_a, n) << std::endl;

    return 0;
}
