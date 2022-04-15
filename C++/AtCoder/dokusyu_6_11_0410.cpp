// copyright
# include<iostream>

class Float {
 public:
    float value = 0.f;
    Float() {}
    explicit Float(float f) : value(f) {}
    Float operator=(const Float& f) {
        std::cout << "test" << std::endl;
        value = f.value;
        return *this;
    }
};

int main() {
    Float f1(1.f);
    auto f2 = f1;
    std::cout << f2.value << std::endl;
}
