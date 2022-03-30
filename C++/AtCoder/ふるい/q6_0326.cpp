// copyright
#include<iostream>

int get_div_sum(int n) {
    // nまでの約数の総和
    int sum = 0;
    for (int i = 1; i*i <= n; i++) {
        if (n % i != 0) {
            continue;
        }
        sum += i;
        if (n / i != i) {
            sum += n / i;
        }
    }
    return sum;
}

int main() {
    int n_end;
    std::cin >> n_end;
    n_end++;

    for (int n = 0; n < n_end; n++) {
        int div_sum = get_div_sum(n);
        if (div_sum > 2*n) {
            std::cout << n << " " << div_sum-n << std::endl;
        }
    }
}
