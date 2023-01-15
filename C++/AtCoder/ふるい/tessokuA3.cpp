// copyright
#include<iostream>
#include<vector>
using namespace std;

int main() {
    // 全探索
    int n, k;
    cin >> n >> k;
    auto red_card_list = vector<int>(n);
    auto blue_card_list = vector<int>(n);

    for (int i = 0; i < n; i++) {
        cin >> red_card_list[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> blue_card_list[i];
    }

    for (auto red_card : red_card_list) {
        for (auto blue_card : blue_card_list) {
            auto sum_ = red_card + blue_card;
            if (sum_ == k) {
                cout << "Yes" << endl;
                return 0;
            }
        }
    }
    cout << "No" << endl;
    return 0;
}