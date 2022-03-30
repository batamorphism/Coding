// copyright
#include <bits/stdc++.h>

struct UnionFind {
    std::vector<int64_t> par;

    explicit UnionFind(int64_t n) : par(n) {
        for (int64_t i = 0; i < n; i++) {
            par[i] = i;
        }
    }

    int64_t find(int64_t x) {
        if (par[x] == x) {
            return x;
        }
        par[x] = find(par[x]);
        return par[x];
    }

    void unite(int64_t p_x, int64_t p_y) {
        auto x = find(p_x);
        auto y = find(p_y);
        if (x == y) {
            return;
        }
        par[x] = y;
    }

    bool same(int64_t p_x, int64_t p_y) {
        return find(p_x) == find(p_y);
    }
};


int main() {
    int n, q;
    std::cin >> n >> q;
    UnionFind uf(n);
    int p, a, b;
    for (int i = 0; i < q; i++) {
        std::cin >> p >> a >> b;
        if (p == 0) {
            uf.unite(a, b);
        } else {
            std::cout << (uf.same(a, b) ? "Yes" : "No") << std::endl;
        }
    }
    return 0;
}
