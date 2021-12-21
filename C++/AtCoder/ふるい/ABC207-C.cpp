// copyright
#include<bits/stdc++.h>

void solver(int n, std::vector<std::vector<int>> section_list) {
    // 現在見ている数直線上の数値に、いくつ区間があるか
    int cnt = 0;
    // 現在処理したところまでで、いくつ区間が重複していたか
    int ans = 0;
    std::sort(section_list.begin(), section_list.end());

    int pre_x = -1;
    int pre_cnt = 0;
    int pre_left_open_cnt = 0;
    for (std::vector<int> section : section_list) {
        if (section[0] != pre_x) {
            // 次の座標に移った場合の処理
            // cntは、前の座標から0.1増やした場合のグラフの個数
            cnt += pre_cnt;
            for (int i=1; i <= pre_left_open_cnt; i++) {
                ans += cnt-i;
            }
            pre_x = section[0];
            pre_cnt = 0;
            pre_left_open_cnt = 0;
        }
        if (section[1] == 0) {
            // rightの場合の処理
            if (section[2] == 2 || section[2] == 4) {
                // [l, r)系なので、現時点ですでに抜けている
                cnt -= 1;
            } else {
                // [l,r]系なので、次の座標に移った直後に抜ける
                pre_cnt -= 1;
            }
        } else {
            // leftの場合の処理
            if (section[2] == 1 || section[2] == 2) {
                // [l, r)系なので、現時点ですでにかぶっている
                cnt += 1;
                ans = ans + (cnt-1);
            } else {
                // (l,r]系なので、次の座標に移った直後にかぶる
                // 次に移った瞬間の追加個数は(l,r]系がいくつあったかに依存するので、
                // pre_left_open_cntに保持する
                pre_cnt += 1;
                pre_left_open_cnt += 1;
            }
        }
    }
    std::cout << ans << std::endl;
}

int main() {
    int n;
    std::cin >> n;
    // [座標, rならば0, t]からなるリスト
    std::vector<std::vector<int>> section_list;
    for (int i = 0; i < n; i++) {
        int t, l, r;
        std::vector<int> section(3);
        std::cin >> t >> l >> r;
        section[0] = r;
        section[1] = 0;
        section[2] = t;
        section_list.push_back(section);
        section[0] = l;
        section[1] = 1;
        section[2] = t;
        section_list.push_back(section);
    }
    solver(n, section_list);
}