// copyright
#include<iostream>

class Float {
    float value = 0.0f;

 public:
    Float() {}
    explicit Float(float f) : value(f) {}
    Float operator+(const Float& other) {
        return Float(value + other.value);
    }
    Float operator-(const Float& other) {
        return Float(value - other.value);
    }
    Float& operator+() {
        return *this;
    }
    Float operator-() {
        return Float(-value);
    }
    Float operator++() {
        // 前置
        std::cout << "bef" << std::endl;
        return *this;
    }
    Float operator++(int) {
        std::cout << "aft" << std::endl;
        return *this;
    }
    float get_value() {
        return value;
    }
};

int main() {
    Float a(1.0f);
    Float b(2.0f);
    Float c = -(a + b);
    std::cout << c.get_value() << std::endl;
    return 0;
}