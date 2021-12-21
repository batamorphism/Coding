// copyright
# include<bits/stdc++.h>

struct Data {
    int height;
    std::string name;
    bool operator<( const Data & other) const {
        return height < other.height;
    }
};

int main() {
    int n;
    std::cin >> n;
    std::vector<std::string> s(n);
    std::vector<int> t(n);
    std::vector<Data> ts(n);
    for (int i = 0; i < n; i++) {
        std::string s_;
        int t_;
        Data d;
        std::cin >> s_;
        std::cin >> t_;
        d.height = t_;
        d.name = s_;
        ts[i] = d;
    }
    std::sort(ts.begin(), ts.end());
    std::cout << ts[n-2].name << std::endl;
}