// copyright
#include<iostream>
#include<vector>

class product {
    int id = 0;
    std::string name = "";
    int price = 0;

 public:
    explicit product(int id, std::string name, int price)
    : id(id), name(name), price(price) {}
    product() {}
    int get_id() const { return id; }
};

int main() {
    std::vector<product> product_list;
    for (int i = 0; i < 4; i++) {
        product_list.emplace_back(product(i, "product" + std::to_string(i), i * 100));
    }
    std::cout << product_list[3].get_id() << std::endl;
}
