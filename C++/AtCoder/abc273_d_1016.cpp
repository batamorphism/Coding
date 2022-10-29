// copyright
#include<iostream>
#include<map>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
    // get_input
    int r_end, c_end, cur_r, cur_c, n;
    cin >> r_end >> c_end >> cur_r >> cur_c >> n;
    cur_r--;
    cur_c--;

    // make map
    // wall_r_of[r] = r行目にある壁の座標の配列
    map<int, vector<int>> wall_r_of;
    map<int, vector<int>> wall_c_of;
    for (int i = 0; i < n; i++) {
        int r, c;
        cin >> r >> c;
        r--;
        c--;
        wall_r_of[r].push_back(c);
        wall_c_of[c].push_back(r);
    }
    // sort wall
    for (auto& [r, wall_r] : wall_r_of) {
        sort(wall_r.begin(), wall_r.end());
    }
    for (auto& [c, wall_c] : wall_c_of) {
        sort(wall_c.begin(), wall_c.end());
    }

    // read query
    int q_end;
    cin >> q_end;
    using query_t = pair<string, int>;
    vector<query_t> query_list;
    for (int i = 0; i < q_end; i++) {
        int step;
        string dir;
        cin >> dir >> step;
        query_t query = {dir, step};
        query_list.push_back(query);
    }

    // solve
    for (auto [dir, step] : query_list) {
        if (dir == "U") {
            // move up
            auto lb = -1;
            const auto& walls = wall_c_of[cur_c];
            if (walls.size() > 0) {
                // cur_r以上の最小の座標を得た後、その座標の一つ前の座標を得る
                // 1つ前が無い場合は、-1のまま
                auto it = lower_bound(walls.begin(), walls.end(), cur_r);
                if (it != walls.begin()) {
                    it--;
                    lb = *it;
                }
            }
            cur_r = max(lb+1, cur_r-step);
        } else if (dir == "D") {
            auto lb = r_end;
            const auto& walls = wall_c_of[cur_c];
            if (walls.size() > 0) {
                // cur_r以上の最小の座標を得る
                auto it = lower_bound(walls.begin(), walls.end(), cur_r);
                if (it != walls.end()) {
                    lb = *it;
                }
            }
            cur_r = min(lb-1, cur_r+step);
        } else if (dir == "L") {
            auto lb = -1;
            const auto& walls = wall_r_of[cur_r];
            if (walls.size() > 0) {
                auto it = lower_bound(walls.begin(), walls.end(), cur_c);
                if (it != walls.begin()) {
                    it--;
                    lb = *it;
                }
            }
            cur_c = max(lb+1, cur_c-step);
        } else if (dir == "R") {
            auto lb = c_end;
            const auto& walls = wall_r_of[cur_r];
            if (walls.size() > 0) {
                auto it = lower_bound(walls.begin(), walls.end(), cur_c);
                if (it != walls.end()) {
                    lb = *it;
                }
            }
            cur_c = min(lb-1, cur_c+step);
        }
        cout << cur_r+1 << " " << cur_c+1 << endl;
    }
}
