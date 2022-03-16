// copyright
#include<iostream>

class vector3d {
    float x = 0;
    float y = 0;
    float z = 0;

 public:
    vector3d();
    vector3d(float x, float y);
    vector3d(float x, float y, float z);
    int get_value() {
        return x + y + z;
    }
};

vector3d::vector3d() {}

vector3d::vector3d(float x, float y): x(x), y(y) {}

vector3d::vector3d(float x, float y, float z): x(x), y(y), z(z) {}


int main() {
    vector3d v(1, 2);
    std::cout << v.get_value() << std::endl;
    return 0;
}