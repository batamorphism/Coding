// copyright
#include<bits/stdc++.h>

int div_sum(int num) {
    int ans = 0;
    for (int i = 1; i*i <= num; i++) {
        if (num % i == 0) {
            ans += i;
            if (i != num / i) {
                ans += num / i;
            }
        }
    }
    return ans;
}

int main() {
    int n_end;
    std::cin >> n_end;
    n_end++;

    for (int i = 1; i < n_end; i++) {
        int ds;
        ds = div_sum(i);
        if (ds > i*2) {
            std::cout << i << " " << ds << std::endl;
        }
    }

    return 0;
}
