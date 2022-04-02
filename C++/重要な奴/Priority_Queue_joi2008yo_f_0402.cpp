// copyright
// ダイクストラ
#include<iostream>
#include<vector>
#include<array>
#include<limits>
#include<queue>

static const int64_t INF = std::numeric_limits<int64_t>::max()/2;
using NeiOf = std::vector<std::vector<std::array<int64_t, 2>>>;


int64_t dijkstra(const NeiOf &nei_of, const int64_t fr, const int64_t to, const int64_t node_end) {
    // frからtoへの最短距離を求める
    std::vector<int64_t> dist(node_end, INF);
    dist.at(fr) = 0;

    // node, costからなるpair
    using NodeCost = std::pair<int64_t, int64_t>;
    std::priority_queue<NodeCost, std::vector<NodeCost>, std::greater<NodeCost>> que;
    que.push({0, fr});

    while (que.size() > 0) {
        const auto [pre_d, pre] = que.top();
        que.pop();
        if (pre_d > dist[pre]) {
            continue;
        }
        for (auto [cur, cost] : nei_of[pre]) {
            auto cur_d = pre_d + cost;
            if (cur_d >= dist[cur]) {
                continue;
            }
            dist.at(cur) = cur_d;
            que.push({cur_d, cur});
        }
    }
    auto ans = dist.at(to);
    return ans;
}


int main() {
    int64_t node_end, k;
    std::cin >> node_end >> k;

    std::vector<std::vector<int64_t>> query_list;
    for (int i = 0; i < k; i++) {
        std::vector<int64_t> query;
        int64_t t;
        std::cin >> t;
        if (t == 0) {
            int64_t fr, to;
            std::cin >> fr >> to;
            fr--;
            to--;
            query.push_back(t);
            query.push_back(fr);
            query.push_back(to);
        } else {
            int64_t fr, to, cost;
            std::cin >> fr >> to >> cost;
            fr--;
            to--;
            query.push_back(t);
            query.push_back(fr);
            query.push_back(to);
            query.push_back(cost);
        }
        query_list.push_back(query);
    }
    // nei_of[node] = nodeに隣接するnodeへの{node, cost}からなるvector
    NeiOf nei_of(node_end);

    for (auto query : query_list) {
        auto t = query[0];
        if (t == 0) {
            auto fr = query[1];
            auto to = query[2];
            auto ans = dijkstra(nei_of, fr, to, node_end);
            if (ans == INF) {
                ans = -1;
            }
            std::cout << ans << std::endl;
        } else {
            auto fr = query[1];
            auto to = query[2];
            auto cost = query[3];
            nei_of[fr].push_back({to, cost});
            nei_of[to].push_back({fr, cost});
        }
    }
}