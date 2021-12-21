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

    std::vector<std::vector<edge>> graph;
    std::vector<int64_t> min_cost, iter;

    Dinic(int64_t V) : INF(std::numeric_limits<flow_t>::max()), graph(V) {}

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

    flow_t max_flow(int64_t s, int64_t t) {
        flow_t flow = 0;
        while (bfs(s, t)) {
            iter.assign(graph.size(), 0);
            flow_t f = 0;
            while ((f = dfs(s, t, INF)) > 0) flow += f;
        }
        return flow;
    }

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
    int64_t n;
    int64_t t;
    std::cin >> n >> t;
    std::vector<std::pair<int64_t, int64_t>> A(n);
    std::vector<std::pair<int64_t, int64_t>> B_vec(2*n);
    std::map<std::pair<int64_t, int64_t>, int64_t> B;
    for (int i = 0; i < n; i++) {
        std::cin >> A[i].first >> A[i].second;
    }
    for (int i = 0; i < n; i++) {
        std::pair<int64_t, int64_t> b;
        std::cin >> b.first >> b.second;
        B[b] = i+n;
        B_vec[i+n] = b;
    }
    int64_t dx[8] = {t, t, 0, -t, -t, -t, 0, t};
    int64_t dy[8] = {0, t, t, t, 0, -t, -t, -t};

    // make graph and edge
    int64_t st_node = 2*n;
    int64_t go_node = 2*n+1;
    Dinic<int64_t> G(2*n+2);
    for (int a_i = 0; a_i < n; a_i++) {
        auto a = A[a_i];
        for (int i = 0; i < 8; i++) {
            int64_t x = a.first+dx[i];
            int64_t y = a.second+dy[i];
            auto key = std::make_pair(x, y);
            if (B.count(key)) {
                G.add_edge(a_i, B[key], 1);
            }
        }
    }
    for (int i = 0; i < n; i++) {
        G.add_edge(st_node, i, 1);
    }
    for (int i = n; i < 2*n; i++) {
        G.add_edge(i, go_node, 1);
    }

    std::vector<int64_t> match_of(n);
    // make matching
    G.max_flow(st_node, go_node);
    // G.output();
    for (int64_t fr = 0; fr < n; fr++) {
        bool is_exists = false;
        auto edge_list = G.graph[fr];
        for (auto edge : edge_list) {
            if (edge.to == st_node || edge.to == go_node) continue;
            if (edge.cap != 0) continue;
            match_of[fr] = edge.to;
            is_exists = true;
        }
        if (!is_exists) {
            std::cout << "No" << std::endl;
            return 0;
        }
    }

    std::cout << "Yes" << std::endl;
    for (int64_t a_i = 0; a_i < n; a_i++) {
        int64_t b_i = match_of[a_i];
        auto a = A[a_i];
        auto b = B_vec[b_i];
        int64_t x = b.first-a.first;
        int64_t y = b.second-a.second;
        for (int i = 0; i < 8; i++) {
            if (dx[i] == x && dy[i] == y) {
                std::cout << i+1 << std::endl;
            }
        }
    }
    return 0;
}