// copyright
// #include<bits/stdc++.h>
#include<tuple>
#include<vector>
#include<map>
#include<iostream>


std::vector<int> calc(int i, int j) {
    // 引数をtupleにしてメモ化する
    // tupleは複数の型でも行けるので、引数は型が混ざっていてもよい
    static std::map<std::tuple<int, int>, std::vector<int>> memo;
    auto key = std::make_tuple(i, j);
    if (memo.count(key)) {
        return memo[key];
    }
    // 初めて計算する場合
    std::cout << "calc_first" << std::endl;
    for (int y = 0; y <= 10; y++) {
        memo[std::make_tuple(i, j)].push_back(i+j);
    }
    return memo[std::make_tuple(i, j)];
}

int main() {
    for (int n = 0; n < 10; n++) {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                std::vector<int> ret = calc(i, j);
                for (auto x : ret) {
                    std::cout << x << " ";
                }
                std::cout << std::endl;
            }
        }
    }
    std::cout << "end" << std::endl;
}
