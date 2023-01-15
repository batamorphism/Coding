// copyright ehekatlact
// 焼く?
#include<iostream>
#include<vector>
#include<array>
#include<string>
#include<algorithm>
#include<map>
using namespace std;

double calc_score(const array<array<int, 10>, 10>& grid, const double& div);

constexpr int SIM_TERM = 100;

class UnionFind {
 public:
    vector <int> par;  // 各元の親を表す配列
    vector <int> siz;  // 素集合のサイズを表す配列(1 で初期化)

    // Constructor
    explicit UnionFind(int sz_): par(sz_), siz(sz_, 1) {
        for (int i = 0; i < sz_; ++i) par[i] = i;  // 初期では親は自分自身
    }
    void init(int sz_) {
        par.resize(sz_);
        siz.assign(sz_, 1);  // resize だとなぜか初期化されなかった
        for (int i = 0; i < sz_; ++i) par[i] = i;  // 初期では親は自分自身
    }

    // Member Function
    // Find
    int root(int x) {  // 根の検索
        while (par[x] != x) {
            x = par[x] = par[par[x]];  // x の親の親を x の親とする
        }
        return x;
    }

    // Union(Unite, Merge)
    bool merge(int x, int y) {
        x = root(x);
        y = root(y);
        if (x == y) return false;
        if (siz[x] < siz[y]) swap(x, y);
        siz[x] += siz[y];
        par[y] = x;
        return true;
    }

    bool issame(int x, int y) {  // 連結判定
        return root(x) == root(y);
    }

    int size(int x) {  // 素集合のサイズ
        return siz[root(x)];
    }
};

array<array<int, 10>, 10> operation(const array<array<int, 10>, 10>& grid, string ori) {
    array<array<int, 10>, 10> moved_grid = grid;
    array<array<int, 10>, 10> pre_moved_grid = grid;
    map<string, pair<int, int>> drdc_of = {
        {"U", {-1, 0}},
        {"D", {1, 0}},
        {"L", {0, -1}},
        {"R", {0, 1}}
    };
    // 変動が無くなるまで、itemを左にずらす
    bool moved = true;
    while (moved) {
        moved = false;
        auto [dr, dc] = drdc_of[ori];

        for (int r = 0; r < 10; r++) {
            for (int c = 0; c < 10; c++) {
                if (pre_moved_grid[r][c] == -1) continue;  // アイテムが無い
                int nr = r + dr;
                int nc = c + dc;
                if (nr < 0 || nr >= 10 || nc < 0 || nc >= 10) continue;
                if (moved_grid[nr][nc] == -1) {
                    moved_grid[nr][nc] = pre_moved_grid[r][c];
                    moved_grid[r][c] = -1;
                    moved = true;
                }
            }
        }
        // 値渡しでmoved_gridにpre_moved_gridの値を入れる
        pre_moved_grid = moved_grid;
    }
    // 左に傾ける
    return moved_grid;
}

array<array<int, 10>, 10> sim(array<array<int, 10>, 10> grid, int first_step, const vector<int>& item_list, const double& div, const int depth) {
    auto put_item = [&](int cur_step) {
        // gridが開いている場所にランダムにアイテムを置く
        vector<pair<int, int>> open_pos;
        for (int r = 0; r < 10; r++) {
            for (int c = 0; c < 10; c++) {
                if (grid[r][c] == -1) {
                    open_pos.push_back({r, c});
                }
            }
        }
        if (open_pos.size() == 0) return;
        auto [r, c] = open_pos[rand() % open_pos.size()];
        auto item = item_list[cur_step];
        grid[r][c] = item;
    };
    // simするターン数を決める
    int sim_term = min(SIM_TERM, 100 - first_step);
    array<array<int, 10>, 10> ret;
    // depthが5になるまでは再帰
    if (depth < 0) {
        double best_score = 0;
        string best_mode = "";
        put_item(first_step);
        for (auto ori : {"L", "R", "F", "B"}) {
            auto moved_grid = operation(grid, ori);
            auto simed_grid = sim(moved_grid, first_step + 1, item_list, div, depth + 1);
            auto score = calc_score(moved_grid, div);
            if (score > best_score) {
                best_score = score;
                best_mode = ori;
                ret = moved_grid;
            }
        }
        return ret;
    }

    // depthが5になったら、sim_term回シミュレーションする
    // スコアが安定しないので、複数回繰り返し、中央値のgridを返す
    using Grid = array<array<int, 10>, 10>;
    vector<pair<double, Grid>> score_grid_list;
    for (int j = 0; j < 15; j++) {
        auto cur_grid = grid;
        for (int i = 0; i < sim_term; i++) {
            auto cur_step = first_step + i;
            // gridが開いている場所にランダムにアイテムを置く
            put_item(cur_step);

            // 4方向に動かし、最もスコアが良いものを採用
            // さらにSIMを重ねる
            double best_score = -1;
            string best_mode = "";
            for (auto ori : {"L", "R", "F", "B"}) {
                auto moved_grid = operation(grid, ori);
                double score = 0;
                score = calc_score(moved_grid, div);
                if (score > best_score) {
                    best_score = score;
                    best_mode = ori;
                }
            }
            cur_grid = operation(cur_grid, best_mode);
        }
        auto cur_score = calc_score(cur_grid, div);
        score_grid_list.push_back({cur_score, cur_grid});
    }
    sort(score_grid_list.begin(), score_grid_list.end());

    return score_grid_list[7].second;
}

double calc_score(const array<array<int, 10>, 10>& grid, const double& div) {
    // gridの連結成分の大きさと、各キャンディーの味がいくつあるかを調べる
    // UnionFind
    UnionFind uf(100);
    for (int r = 0; r < 10; r++) {
        for (int c = 0; c < 10; c++) {
            if (grid[r][c] == -1) continue;  // アイテムが無い
            if (r < 9 && grid[r + 1][c] == grid[r][c]) {
                uf.merge(r * 10 + c, (r + 1) * 10 + c);
            }
            if (c < 9 && grid[r][c + 1] == grid[r][c]) {
                uf.merge(r * 10 + c, r * 10 + c + 1);
            }
        }
    }
    // 各連結成分の大きさを調べる
    vector<int> component_size;
    for (int pos = 0; pos < 100; pos++) {
        if (grid[pos / 10][pos % 10] == -1) continue;
        auto root = uf.root(pos);
        if (root == pos) {
            component_size.push_back(uf.size(pos));
        }
    }

    double score = 0;
    for (auto size : component_size) {
        score += size * size;
    }
    score /= div;
    score *= 1000000;
    return score;
}

int main() {
    bool debug = false;
    vector<int> item_list(100, -1);
    for (int i = 0; i < 100; i++) {
        cin >> item_list[i];
        item_list[i]--;
    }

    // create grid[10][10]
    array<array<int, 10>, 10> grid;
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            grid[i][j] = -1;
        }
    }

    array<int, 3> item_count = {0, 0, 0};
    double div = 0;
    for (auto item : item_list) {
        item_count[item]++;
    }
    for (int count : item_count) {
        div += count * count;
    }

    auto show_grid = [&]() {
        for (int r = 0; r < 10; r++) {
            for (int c = 0; c < 10; c++) {
                cout << grid[r][c] << " ";
            }
            cout << endl;
        }
    };

    array<string, 100> debug_ans;
    for (int i = 0; i < 100; i++) {
        // get position and set item to grid
        int pos;
        auto item = item_list[i];
        cin >> pos;
        pos--;
        // 左上からgridの空いている場所に順に0, 1, 2, ...と割り当てられている
        int cnt = 0;
        bool setted = false;
        for (int r = 0; r < 10; r++) {
            for (int c = 0; c < 10; c++) {
                if (grid[r][c] == -1) {
                    if (cnt == pos) {
                        grid[r][c] = item;
                        setted = true;
                        break;
                    }
                    cnt++;
                }
            }
            if (setted) break;
        }
        if (debug) {
            show_grid();
        }
        // 4方向に動かして、最もスコアが良かった操作を採用
        double best_score = -1;
        string best_mode = "";
        for (auto ori : {"L", "R", "F", "B"}) {
            auto moved_grid = operation(grid, ori);
            // 1回操作したから、i+1
            auto sim_grid = sim(moved_grid, i+1, item_list, div, 0);
            auto score = calc_score(sim_grid, div);
            if (score > best_score) {
                best_score = score;
                best_mode = ori;
            }
        }
        grid = operation(grid, best_mode);
        best_score = calc_score(grid, div);

        if (debug) {
            debug_ans[i] = best_mode;
            cout << best_score << endl;
        } else {
            cout << best_mode << endl;
            cout << flush;
        }
    }

    if (debug) {
        for (int r = 0; r < 10; r++) {
            for (int c = 0; c < 10; c++) {
                cout << grid[r][c] << " ";
            }
            cout << endl;
        }
        for (auto s : debug_ans) {
            cout << s << endl;
        }
    }
}
