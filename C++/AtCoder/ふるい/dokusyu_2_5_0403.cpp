// copyright
#include<iostream>

class Float {
 public:
    float value = 0.0f;
    Float() {}
    Float(float f) : value(f) {}
    Float operator+(Float rhs) const {
        return Float(value + rhs.value);
    }
    Float operator-(Float rhs) const {
        return Float(value - rhs.value);
    }
    Float operator+() const {
        return Float(value);
    }
    Float operator-() const {
        return Float(-value);
    }
    void operator++() {
        std::cout << "test1" << std::endl;
    }
    void operator++(int) {
        std::cout << "test2" << std::endl;
    }
};

int main() {
    Float a(1.0f);
    Float b(2.0f);
    Float c = -b;
    std::cout << c.value << std::endl;
    c++;
    ++c;
    return 0;
}