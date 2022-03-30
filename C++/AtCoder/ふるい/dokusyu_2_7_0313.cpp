// copyright
#include<iostream>

struct vector2d {
    float x;
    float y;
};

int sub(int a, int b) {
    return a - b;
}

vector2d sub(vector2d a, vector2d b) {
    vector2d ret = {a.x - b.x, a.y - b.y};
    return ret;
}

int main() {
    std::cout << sub(10, 20) << std::endl;

    vector2d a = {-10, 30};
    vector2d b = {5, 10};
    auto v = sub(a, b);
    std::cout << v.x << " " << v.y << std::endl;
}