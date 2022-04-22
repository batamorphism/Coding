// copyright
#include<iostream>
#include<vector>
#include<array>
#include<queue>
#include<limits>

using NodeCost = std::array<int64_t, 2>;
using Node = int64_t;
using Dist = std::vector<Node>;

Dist dijkstra(Node node_end, std::vector<std::vector<NodeCost>> nei_of, Node st) {
    const int64_t INF = std::numeric_limits<int64_t>::max()/2;
    Dist dist(node_end, INF);
    dist[st] = 0;
    std::priority_queue<NodeCost, std::vector<NodeCost>, std::greater<NodeCost>> que;
    que.push(NodeCost{0, st});

    while (!que.empty()) {
        auto [pre_cost, pre_node] = que.top();
        que.pop();
        for (auto [cur_node, cost] : nei_of[pre_node]) {
            auto cur_cost = pre_cost + cost;
            if (dist[cur_node] > cur_cost) {
                dist[cur_node] = cur_cost;
                que.push(NodeCost{cur_cost, cur_node});
            }
        }
    }
    return dist;
}

int main() {
    int64_t node_end, edge_end;
    std::cin >> node_end >> edge_end;

    // nei_of[fr] = {{to, cost}, ...}
    std::vector<std::vector<NodeCost>> nei_of(node_end);
    for (int i = 0; i < edge_end; i++) {
        Node fr, to;
        int64_t cost;
        std::cin >> fr >> to >> cost;
        fr--;
        to--;
        nei_of[fr].emplace_back(NodeCost{to, cost});
        nei_of[to].emplace_back(NodeCost{fr, cost});
    }

    // stからの距離と、enからの距離を前計算
    // ダイクストラ
    Node st = 0;
    Node en = node_end-1;
    auto dist_st = dijkstra(node_end, nei_of, st);
    auto dist_en = dijkstra(node_end, nei_of, en);

    for (Node k = 0; k < node_end; k++) {
        auto ans = dist_st[k] + dist_en[k];
        std::cout << ans << std::endl;
    }

    return 0;
}
