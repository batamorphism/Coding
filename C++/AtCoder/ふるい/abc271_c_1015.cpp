// copyright

// include libraries
#include <algorithm>
#include <bitset>
#include <vector>
#include <array>
#include <iostream>
#include <map>
#include <string>
#include <queue>
#include <set>
#include <stack>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <cmath>
#include <deque>

int main() {
    // すでに読んだ本->巻数が大きい本の順番に売っていけばよい
    // deque
    // すでに読んだ巻数を保持して、それより大きくなるまでキューpop_leftする
    // その後巻数が大きい本をpop_rightする。
    // 2冊とった段階で、すでに読んだ巻数+1をpush_leftする
    // キューの左端が、次に読む巻数なら1つ進める
    // input
    int n;
    std::deque<int64_t> deq;
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        int a;
        std::cin >> a;
        deq.push_back(a);
    }
    std::sort(deq.begin(), deq.end());

    // SIM
    int64_t cur_read_num = 0;
    int64_t nex_read_num = cur_read_num+1;
    auto sell_cnt = 0;
    while (deq.size() > 0) {
        // すでに読んだ本はすべて売る
        while (deq.front() <= cur_read_num) {
            sell_cnt++;
            deq.pop_front();
            while (sell_cnt >= 2) {  // まあ遅いけど、、、間に合うか
                deq.push_front(nex_read_num);
                sell_cnt -= 2;
                // 読書判定
                if (deq.front() == nex_read_num) {
                    cur_read_num++;
                    nex_read_num++;
                    deq.pop_front();
                }
            }
        }
        // 読書判定
        while (deq.front() == nex_read_num) {
            cur_read_num = nex_read_num;
            nex_read_num = cur_read_num+1;
            deq.pop_front();
        }
        // 大きい本は売る。一回だけ。
        deq.pop_back();
        sell_cnt++;
    }
    
    std::cout << cur_read_num;
    
    return 0;
}
