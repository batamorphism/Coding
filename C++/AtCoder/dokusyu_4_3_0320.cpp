// copyright
#include<iostream>

class product {
    int price;
 public:
    explicit product(int price);
    inline int get_price() const;
    inline void set_price(int price);
};

product::product(int price) : price(price) {}

int product::get_price() const {
    return price;
}

void product::set_price(int price) {
    this->price = price;
}

int main() {
    product p(10);
    p.set_price(100);
    std::cout << p.get_price() << std::endl;
}
