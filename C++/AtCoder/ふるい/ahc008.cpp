//copyright
#include <bits/stdc++.h>

double sim(std::vector<std::vector<int>> pet_list, std::vector<std::vector<int>> human_list, std::vector<std::vector<int>> region_list, int human_end, int pet_end) {
    std::vector<std::vector<int>> grid(30, std::vector<int>(30, 0));

    for (int pet = 0; pet < pet_end; pet++) {
        grid[pet_list[pet][0]][pet_list[pet][1]] = 1;
    }

    for (int i = 0; i < 300; i++) {
        // 人間のターン
        for (int human = 0; human < human_end; human++) {
            std::vector<int> region = region_list[human];
            int x = human_list[human][0];
            int y = human_list[human][1];
            int r_x0 = region[0];
            int r_y0 = region[1];
            int r_x1 = region[2];
            int r_y1 = region[3];
            // 外周に達していない場合
            if (x != r_x0 || x != r_x1 || y != r_y0 || y != r_y1) {
                // とりあえず上に行くか
                human_list[human][1]++;
                continue;
            }
            // 外周に達したら時計回り
            if (x == r_x0 && y != r_y1) {  // 左端
                if (i % 2 == 0) {  // 上に移動
                    human_list[human][1]++;
                } else {  // 左にブロックを置く
                    if (x-1 >= 0 && grid[x-1][y] == 0) {
                        grid[x-1][y] = 1;
                    }
                }
            } else if (y == r_y1 && x != r_x1) {  // 上
                if (i % 2 == 0) {  // 右に移動
                    human_list[human][0]++;
                } else {  // 上にブロックを置く
                    if (y+1 < 30 && grid[x][y+1] == 0) {
                        grid[x][y+1] = 1;
                    }
                }
            } else if (x == r_x1 && y != r_y0) {  // 右
                if (i % 2 == 0) {  // 下に移動
                    human_list[human][1]--;
                } else {  // 右にブロックを置く
                    if (x+1 < 30 && grid[x+1][y] == 0) {
                        grid[x+1][y] = 1;
                    }
                }
            } else {  // 下
                if (i % 2 == 0) {  // 左に移動
                    human_list[human][0]--;
                } else {  // 下にブロックを置く
                    if (y-1 >= 0 && grid[x][y-1] == 0) {
                        grid[x][y-1] = 1;
                    }
                }
            }
        }
        // 動物のターン
        for (int pet = 0; pet < pet_end; pet++) {
            int x = pet_list[pet][0];
            int y = pet_list[pet][1];
            int t = pet_list[pet][2];
            if (t <= 5) {  // TODO 犬と猫は一旦やんない
                for (int j = 0; j < t; j++) {
                    // 基本行動をt回行う
                    grid[x][y] = 0;
                    // 乱数を発生させる
                    while (true) {
                        int r = rand() % 4;
                        if (r == 0) {
                            if (x+1 < 30 && grid[x+1][y] == 0) {
                                pet_list[pet][0]++;
                                x++;
                                break;
                            }
                        } else if (r == 1) {
                            if (x-1 >= 0 && grid[x-1][y] == 0) {
                                pet_list[pet][0]--;
                                x--;
                                break;
                            }
                        } else if (r == 2) {
                            if (y+1 < 30 && grid[x][y+1] == 0) {
                                pet_list[pet][1]++;
                                y++;
                                break;
                            }
                        } else {
                            if (y-1 >= 0 && grid[x][y-1] == 0) {
                                pet_list[pet][1]--;
                                y--;
                                break;
                            }
                        }
                    }
                    grid[x][y] = -t;
                }
            }
        }
    }

        // 各region内の動物の数を求める
        double score = 0.;
        for(int human; human < human_end; human++) {
            std::vector<int> region = region_list[human];
            int r_x0 = region[0];
            int r_y0 = region[1];
            int r_x1 = region[2];
            int r_y1 = region[3];
            int cnt_pet = 0;
            for (int x = r_x0; x <= r_x1; x++) {
                for (int y = r_y0; y <= r_y1; y++) {
                    if (grid[x][y] <= -1) {
                        cnt_pet++;
                    }
                }
            }
            double area = (r_x1 - r_x0 + 1) * (r_y1 - r_y0 + 1);
            score += area/900 * std::pow(2, -cnt_pet);
        }

    return score;
}


int main() {
    // 入力
    int pet_end;
    std::cin >> pet_end;
    std::vector<std::vector<int>> pet_list(pet_end, std::vector<int>(3));
    for (int i = 0; i < pet_end; i++) {
        std::cin >> pet_list[i][0] >> pet_list[i][1] >> pet_list[i][2];
        pet_list[i][0]--;
        pet_list[i][1]--;
    }
    int human_end;
    std::cin >> human_end;
    std::vector<std::vector<int>> human_list(human_end, std::vector<int>(2));
    for (int i = 0; i < human_end; i++) {
        std::cin >> human_list[i][0] >> human_list[i][1];
        human_list[i][0]--;
        human_list[i][1]--;
    }

    int r_end, c_end;
    r_end = 30;
    c_end = 30;

    // (region[0], region[1]), (regin[2], region[3])の領域を確保する
    std::vector<std::vector<int>> region_list(human_end, std::vector<int>(4, 0));

    // 初期値として、各人を含む上下左右に2マスずつ確保する
    for (int human = 0; human < human_end; human++) {
        region_list[human][0] = human_list[human][0];
        region_list[human][1] = human_list[human][1];
        region_list[human][2] = human_list[human][0] + 1;
        region_list[human][3] = human_list[human][1] + 1;
    }

    auto score = sim(pet_list, human_list, region_list, human_end, pet_end);

    

    return 0;
}


