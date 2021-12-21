// copyright

#include <bits/stdc++.h>
int main() {
    int n, k, p;
    std::cin >> n >> k >> p;

    int64_t A[n];
    for (int i = 0; i < n; i++) {
        std::cin >> A[i];
    }

    int64_t A1[n/2];
    int64_t A2[n-n/2];
    int n1 = n/2;
    int n2 = n-n/2;

    for (int i = 0; i < n/2; i++) {
        A1[i] = A[i];
    }
    for (int i = 0; i < n-n/2; i++) {
        A2[i] = A[i+n/2];
    }

    std::vector<std::pair <int64_t, int64_t>> pat_list1;
    std::vector<std::pair <int64_t, int64_t>> pat_list2;

    int64_t bit_all1 = 1 << n1;
    int64_t a1_end = n1;
    for (int64_t bit = 0; bit < bit_all1; bit++) {
        int64_t cnt = 0;
        int64_t val = 0;
        for (int a_i = 0; a_i < a1_end; a_i++) {
            if (bit & (1 << a_i)) {
                cnt++;
                val += A1[a_i];
            }
        }
        pat_list1.push_back(std::make_pair(cnt, val));
    }

    int64_t bit_all2 = 1 << n2;
    int64_t a2_end = n2;
    for (int64_t bit = 0; bit < bit_all2; bit++) {
        int64_t cnt = 0;
        int64_t val = 0;
        for (int a_i = 0; a_i < a2_end; a_i++) {
            if (bit & (1 << a_i)) {
                cnt++;
                val += A2[a_i];
            }
        }
        pat_list2.push_back(std::make_pair(cnt, val));
    }

    std::sort(pat_list1.begin(), pat_list1.end());
    std::sort(pat_list2.begin(), pat_list2.end());

    std::vector<int64_t> val2_of[41];
    for (auto cnt_val2 : pat_list2) {
        val2_of[cnt_val2.first].push_back(cnt_val2.second);
    }

    for (auto val2_list : val2_of) {
        std::sort(val2_list.begin(), val2_list.end());
    }

    int64_t ans = 0;
    int cnt = 0;
    for (auto cnt1_val1 : pat_list1) {
        cnt++;
        if (cnt % 10000 == 0) {
            std::cout << cnt << ans << std::endl;
        }
        int64_t cnt1 = cnt1_val1.first;
        int64_t val1 = cnt1_val1.second;
        int64_t cnt2 = k - cnt1;
        int64_t val2_max = p - val1;
        if (cnt2 < 0) {
            continue;
        }
        if (val2_max < 0) {
            continue;
        }
        auto val2_list = val2_of[cnt2];
        // binary search
        int64_t ok = -1;
        int64_t ng = val2_list.size();
        while (abs(ok - ng) > 1) {
            int64_t mid = (ok + ng) / 2;
            if (val2_list[mid] <= val2_max) {
                ok = mid;
            } else {
                ng = mid;
            }
        }
        ans += ok+1;
    }

    std::cout << ans << std::endl;
}
