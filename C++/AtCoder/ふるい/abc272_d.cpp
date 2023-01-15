// copyright

// include libraries
#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int r_end, c_end, cur_r, cur_c, n;
    cin >> r_end >> c_end >> cur_r >> cur_c >> n;
    cur_r--;
    cur_c--;

    using wall_t = vector<int>;
    map<int, wall_t> wall_of_r;
    map<int, wall_t> wall_of_c;

    for (int i = 0; i < n; i++) {
        int r, c;
        cin >> r >> c;
        r--;
        c--;
        wall_of_r[r].push_back(c);
        wall_of_c[c].push_back(r);
    }

    // sort walls
    for (auto &it : wall_of_r) {
        sort(it.second.begin(), it.second.end());
    }
    for (auto &it : wall_of_c) {
        sort(it.second.begin(), it.second.end());
    }

    // run query
    int q_end;
    cin >> q_end;
    for (int q = 0; q < q_end; q++) {
        string dir;
        int step;
        cin >> dir >> step;

        if (dir == "L") {
            auto it = wall_of_r.find(cur_r);
            auto lb = -1;  // 壁のある場所 lesser bound
            if (it != wall_of_r.end()) {
                // 壁がある場合は、cur_rより小さい最大の値を探す
                // 壁があるので、wall.begin() != wall.end()
                auto &wall = it->second;
                auto it2 = lower_bound(wall.begin(), wall.end(), cur_c);
                if (it2 != wall.begin()) {
                    it2--;
                    lb = *it2;
                } else {  // cur_rより小さい最大の値が存在しない
                    lb = -1;
                }
            }
            cur_c = max(cur_c - step, lb + 1);
        } else if (dir == "U") {
            auto it = wall_of_c.find(cur_c);
            auto lb = -1;  // 壁のある場所
            if (it != wall_of_c.end()) {
                auto &wall = it->second;
                auto it2 = lower_bound(wall.begin(), wall.end(), cur_r);
                if (it2 != wall.begin()) {
                    it2--;
                    lb = *it2;
                } else {  // cur_rより小さい最大の値が存在しない
                    lb = -1;
                }
            }
            cur_r = max(cur_r - step, lb + 1);
        } else if (dir == "R") {
            auto it = wall_of_r.find(cur_r);
            int ub = c_end;
            if (it != wall_of_r.end()) {
                auto &wall = it->second;
                auto it2 = upper_bound(wall.begin(), wall.end(), cur_c);
                if (it2 != wall.end()) {
                    ub = *it2;
                } else {  // cur_rより大きい最小の値が存在しない
                    ub = c_end;
                }
            }
            cur_c = min(cur_c + step, ub - 1);
        } else if (dir == "D") {
            auto it = wall_of_c.find(cur_c);
            int ub = r_end;
            if (it != wall_of_c.end()) {
                auto &wall = it->second;
                auto it2 = upper_bound(wall.begin(), wall.end(), cur_r);
                if (it2 != wall.end()) {
                    ub = *it2;
                } else {  // cur_rより大きい最小の値が存在しない
                    ub = r_end;
                }
            }
            cur_r = min(cur_r + step, ub - 1);
        }
        cout << cur_r + 1 << " " << cur_c + 1 << endl;
    }

    return 0;
}