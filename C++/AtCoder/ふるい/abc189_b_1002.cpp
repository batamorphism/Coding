// copyright
#include<bits/stdc++.h>
int main() {
    int n, x;
    std::cin >> n >> x;
    int64_t V[n];
    int64_t P[n];
    for (int i = 0; i < n; i++) {
        std::cin >> V[i] >> P[i];
    }
    int64_t drunk = 0;
    int64_t ans = -1;
    for (int i = 0; i < n; i++) {
        drunk += V[i]*P[i];
        if (drunk > x*100) {
            ans = i+1;
            break;
        }
    }
    std::cout << ans << std::endl;
}
