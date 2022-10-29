// copyright
#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main() {
    // input
    int r_end, c_end, cur_r, cur_c, n;
    cin >> r_end >> c_end >> cur_r >> cur_c >> n;
    cur_r--;
    cur_c--;

    // wall_r_of[r]
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
    // sort
    for (auto& p : wall_r_of) {
        auto& wall = p.second;
        sort(wall.begin(), wall.end());
    }
    for (auto& p : wall_c_of) {
        auto& wall = p.second;
        sort(wall.begin(), wall.end());
    }

    int q;
    cin >> q;
    for (int i = 0; i < q; i++) {
        string dir;
        int step;
        cin >> dir >> step;
        if (dir == "U") {
            auto lb = -1;
            auto it = wall_c_of.find(cur_c);
            if (it != wall_c_of.end()) {
                auto& wall = it->second;
                auto it = lower_bound(wall.begin(), wall.end(), cur_r);
                if (it != wall.begin()) {
                    it--;
                    lb = *it;
                }
            }
            cur_r = max(lb+1, cur_r-step);
        } else if (dir == "L") {
            auto lb = -1;
            auto it = wall_r_of.find(cur_r);
            if (it != wall_r_of.end()) {
                auto& wall = it->second;
                auto it = lower_bound(wall.begin(), wall.end(), cur_c);
                if (it != wall.begin()) {
                    it--;
                    lb = *it;
                }
            }
            cur_c = max(lb+1, cur_c-step);
        } else if (dir == "D") {
            auto lb = r_end;
            auto it = wall_c_of.find(cur_c);
            if (it != wall_c_of.end()) {
                auto& wall = it->second;
                auto it = lower_bound(wall.begin(), wall.end(), cur_r);
                if (it != wall.end()) {
                    lb = *it;
                }
            }
            cur_r = min(lb-1, cur_r+step);
        } else {
            auto lb = c_end;
            auto it = wall_r_of.find(cur_r);
            if (it != wall_r_of.end()) {
                auto& wall = it->second;
                auto it = lower_bound(wall.begin(), wall.end(), cur_c);
                if (it != wall.end()) {
                    lb = *it;
                }
            }
            cur_c = min(lb-1, cur_c+step);
        }
        cout << cur_r+1 << " " << cur_c+1 << endl;
    }
    return 0;
}