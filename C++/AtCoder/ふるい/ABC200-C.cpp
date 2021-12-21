# include<bits/stdc++.h>

int main() {
    int64_t n;
    std::cin >> n;
    std::vector<int64_t> a(n);
    for (int i = 0; i < n; i++) {
        int64_t a_;
        std::cin >> a_;
        a[i] = a_ % 200;
    }
    int64_t ans=0;
    for (int i = 0; i < 200; i++) {
        // mod200上でiとなるaの添え字の数を数える
        int64_t mod200_count=0;
        for (int j = 0; j < n; j++) {
            if (a[j]==i) {
                mod200_count++;
            }
        }
        if (mod200_count >= 2) {
            ans+=mod200_count*(mod200_count-1)/2;
        }
    }
    std::cout << ans << std::endl;
}

