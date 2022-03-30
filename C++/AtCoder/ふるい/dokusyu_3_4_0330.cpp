// copyright
#include<iostream>

class vector3d{
    float x;
    float y;
    float z;
 public:
    vector3d():x(0), y(0), z(0) {}
    explicit vector3d(float x, float y, float z):x(x), y(y), z(z) {}

    friend vector3d sub(vector3d a, vector3d b) {
        return vector3d(a.x - b.x, a.y - b.y, a.z - b.z);
    }

    void dump() const {
        std::cout << x << " " << y << " " << z << std::endl;
    }
};

int main() {
    auto v1 = vector3d(1, 2, 3);
    auto v2 = vector3d(4, 5, 6);
    auto v3 = sub(v1, v2);
    v3.dump();
}
