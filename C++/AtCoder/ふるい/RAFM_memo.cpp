// copyright
#include<bits/stdc++.h>

void write_log(clock_t st, clock_t en) {
    double time = static_cast<double> (en - st) / CLOCKS_PER_SEC;
    std::cout << time << " sec" << std::endl;
}


double myfnc(int i, int j, int k) {
    static std::unordered_map<std::string, double> memo_myfnc;
    std::string key;
    key = std::to_string(i) + "|"
        + std::to_string(j) + "|"
        + std::to_string(k) + "|";
    if (memo_myfnc.count(key)) {
        // already calced
        return memo_myfnc[key];
    }

    // calc logic ここに重たいロジックを入れる
    // 計算されているか確認するときは、下のコメントアウトを取る
    // std::cout << "calc" << i << j << k << std::endl;
    double ans = i+j+k;

    // write memo
    memo_myfnc[key] = ans;
    return ans;
}

int main() {
    // start test
    std::cout << myfnc(1, 2, 3) << std::endl;
    // 2回目は計算されない
    std::cout << myfnc(1, 2, 3) << std::endl;
    // 計算される
    std::cout << myfnc(2, 2, 3) << std::endl;
    std::cout << myfnc(2, 2, 4) << std::endl;
    // 最初に計算してあるからもう計算されない
    std::cout << myfnc(1, 2, 3) << std::endl;

    // 負荷テスト
    clock_t start = clock();
    for (int i = 0; i < 100; i++) {
        for (int j = 0; j < 100; j++) {
            for (int k = 0; k < 100; k++) {
                myfnc(i%10, j%10, k%10);
            }
        }
    }
    clock_t end = clock();
    write_log(start, end);
}
