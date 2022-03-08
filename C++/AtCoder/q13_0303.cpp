// copyright
#include <bits/stdc++.h>
template <typename E = std::mt19937,
          typename D = std::uniform_int_distribution<>>
double compute_pi(E& engine, D& dist, int64_t const samples = 10000000) {
    auto hit = 0;
    for (int64_t i = 0; i < samples; i++) {
        auto x = dist(engine);
        auto y = dist(engine);
        if (x * x + y * y <= 1) {
            hit++;
        }
    }
    return 4.0 * hit / samples;
}

int main() {
    std::random_device rd;
    auto seed_data = std::array<int, std::mt19937::state_size>{};
    std::generate(std::begin(seed_data), std::end(seed_data), std::ref(rd));
    std::seed_seq seq(std::cbegin(seed_data), std::cend(seed_data));
    auto eng = std::mt19937{seq};
    auto dist = std::uniform_int_distribution<>{0, 1};
    for (auto j = 0; j < 10; j++) {
        std::cout << compute_pi(eng, dist) << std::endl;
    }
}
