// copyright
#include<bits/stdc++.h>

template< typename flow_t>
struct Dinic {
    const flow_t INF;

    struct edge {
        int64_t to;
        flow_t cap;
        int64_t rev;
        bool isrev;
        int64_t idx;
    };

    /**
     * @brief 
     * graph[fr] でfrを始点とするedge_listを返す。
     * auto edge_list = graph[fr];
     * for (auto edge : edge_list) {
     *      //ここでedge.toやedge.capを使用する
     * }
     */
    std::vector<std::vector<edge>> graph;
    std::vector<int64_t> min_cost, iter;

    /**
     * @brief Construct a new Dinic object
     *  Dinic<int64_t> G(v_end+1); の形で宣言
     * @param V node数
     */
    Dinic(int64_t V) : INF(std::numeric_limits<flow_t>::max()), graph(V) {}

    /**
     * @brief 有向のedgeを追加する
     * 
     * @param from 始点
     * @param to 終点
     * @param cap 最大流量
     * @param idx 
     */
    void add_edge(int64_t from, int64_t to, flow_t cap, int64_t idx = -1) {
        graph[from].emplace_back((edge) {to, cap, (int64_t) graph[to].size(), false, idx});
        graph[to].emplace_back((edge) {from, 0, (int64_t) graph[from].size() - 1, true, idx});
    }

    bool bfs(int64_t s, int64_t t) {
        min_cost.assign(graph.size(), -1);
        std::queue< int64_t > que;
        min_cost[s] = 0;
        que.push(s);
        while (!que.empty() && min_cost[t] == -1) {
            int64_t p = que.front();
            que.pop();
            for (auto &e : graph[p]) {
                if (e.cap > 0 && min_cost[e.to] == -1) {
                    min_cost[e.to] = min_cost[p] + 1;
                    que.push(e.to);
                }
            }
        }
        return min_cost[t] != -1;
    }

    flow_t dfs(int64_t idx, const int64_t t, flow_t flow) {
        if (idx == t) return flow;
        for (int64_t &i = iter[idx]; i < graph[idx].size(); i++) {
            edge &e = graph[idx][i];
            if (e.cap > 0 && min_cost[idx] < min_cost[e.to]) {
                flow_t d = dfs(e.to, t, std::min(flow, e.cap));
                if (d > 0) {
                    e.cap -= d;
                    graph[e.to][e.rev].cap += d;
                    return d;
                }
            }
        }
        return 0;
    }

    /**
     * @brief 始点から終点までflowを流し、最大流量を計算する。
     * 
     * @param s 始点を指すノード
     * @param t 終点を指すノード
     * @return flow_t 最大流量
     */
    flow_t max_flow(int64_t s, int64_t t) {
        flow_t flow = 0;
        while (bfs(s, t)) {
            iter.assign(graph.size(), 0);
            flow_t f = 0;
            while ((f = dfs(s, t, INF)) > 0) flow += f;
        }
        return flow;
    }

    /**
     * @brief デバッグ用にmax_flow後のグラフの状態を確認する
     * 始点, 終点, 流量/上限で出力される
     */
    void output() {
        for (int64_t i = 0; i < graph.size(); i++) {
            for (auto &e : graph[i]) {
                if (e.isrev) continue;
                auto &rev_e = graph[e.to][e.rev];
                std::cout << i << "->" << e.to << " (flow: " << rev_e.cap << "/" << e.cap + rev_e.cap << ")" << std::endl;
            }
        }
    }
};

int main() {
    int64_t n, t;
    std::cin >> n >> t;
    std::vector<std::pair<int64_t, int64_t>> A(n);
    std::vector<std::pair<int64_t, int64_t>> B(n);
    for (int64_t i = 0; i < n; i++) {
        std::cin >> A[i].first >> A[i].second;
    }
    for (int64_t i = 0; i < n; i++) {
        std::cin >> B[i].first >> B[i].second;
    }
    int64_t dx[8] = {t, t, 0, -t, -t, -t,  0,  t};
    int64_t dy[8] = {0, t, t,  t,  0, -t, -t, -t};
    int64_t start = 2*n;
    int64_t end = 2*n+1;
    Dinic<int64_t> G(end+1);

    // add_edges
    for (int64_t node = 0; node < n; node++) {
        G.add_edge(start, node, 1);
        G.add_edge(n+node, end, 1);
    }

    std::map<int64_t, int64_t> B_map;
    for (int64_t i = 0; i < n; i++) {
        auto b = B[i];
        int64_t b_xy;
        b_xy = b.first*1000000000+b.second;
        B_map[b_xy] = i;
    }
    for (int64_t i = 0; i < n; i++) {
        for (int64_t k = 0; k < 8; k++) {
            auto a = A[i];
            int64_t a_xy = (a.first+dx[k])*1000000000+a.second+dy[k];
            if (B_map.find(a_xy) != B_map.end()) {
                int64_t j = B_map[a_xy];
                G.add_edge(i, n+j, 1);
            }
        }
    }

    // solve
    int64_t cnt = G.max_flow(start, end);
    if (cnt == n) {
        std::cout << "Yes" << std::endl;
    } else {
        std::cout << "No" << std::endl;
        return 0;
    }

    G.output();
    std::vector<int64_t> b_of(n);
    for (int64_t i = 0; i < G.graph.size(); i++) {
        for (auto &e : G.graph[i]) {
            if (e.isrev) continue;
            if (e.cap == 0 && i != start && e.to != end) {
                b_of[i] = e.to-n;
            }
        }
    }

    for (int64_t i = 0; i < n; i++) {
        auto b = B[b_of[i]];
        auto a = A[i];
        int64_t ax = a.first;
        int64_t bx = b.first;
        int64_t ay = a.second;
        int64_t by = b.second;
        for (int64_t j = 0; j < 8; j++) {
            if (ax+dx[j] == bx && ay+dy[j] == by) {
                std::cout << j+1 << std::endl;
            }
        }
    }
    return 0;
}