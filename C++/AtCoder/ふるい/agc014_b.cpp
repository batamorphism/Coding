// copyright
#include<bits/stdc++.h>
int main() {
    // a, bからなるグラフが、余計な頂点を持たない円環となればよい
    // これは、連結成分ごとに深さ優先探索を行い、開始地点以外の頂点から戻り掛けなければよい
    int node_end, edge_end;
    std::cin >> node_end >> edge_end;

    std::vector<std::vector<int>> nei_of(node_end);
    for (int i = 0; i < edge_end; i++) {
        int a, b;
        std::cin >> a >> b;
        a--;
        b--;
        nei_of[a].push_back(b);
        nei_of[b].push_back(a);
    }

    /*
    std::vector<bool> done(node_end, false);

    bool dfs(int pre, int root) {
        done[pre] = true;
        for (int cur : nei_of[pre]) {
            if (done[cur]) continue;
            dfs(cur, root);
            // 戻り掛けるときに、移動先で円環判定が経っていない場合は、
        }
    }

    for (int root = 0; root < node_end; root++) {
        if (done[root]) continue;
        dfs(root, root);
    }
    */
    // 全ての頂点の次数が偶数ならばよい
    bool is_exist = true;
    for (auto nei : nei_of) {
        if (nei.size() % 2 == 1) {
            is_exist = false;
            break;
        }
    }

    if (is_exist) {
        std::cout << "YES" << std::endl;
    } else {
        std::cout << "NO" << std::endl;
    }

    return 0;
}
