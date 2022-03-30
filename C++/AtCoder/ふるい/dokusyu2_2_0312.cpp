// copyright
#include<iostream>

class product {
    int id;
    int price;
    int stook;

 public:
 /*
    int get_id();
    void set_id(int new_id);
    int get_price();
    void set_price(int new_price);
    int get_stook();
    void set_stook(int new_stook);
*/
    int get_id() {
        return id;
    }

    void set_id(int new_id) {
        if (new_id < 0) {
            std::cout << "error" << std::endl;
            return;
        }
        id = new_id;
    }

    int get_price() {
        return price;
    }

    void set_price(int new_price) {
        if (new_price < 0) {
            std::cout << "error" << std::endl;
            return;
        }
        price = new_price;
    }

    void get_stock(int new_stock) {
        if (new_stock < 0) {
            std::cout << "error" << std::endl;
            return;
        }
        stook = new_stock;
    }

    void set_all(int id, int price, int stook) {
        set_id(id);
        set_price(price);
        get_stock(stook);
    }
};

int main() {
    product pen;
    pen.set_all(1, 100, 10);

    product* ptr = &pen;
    std::cout << ptr->get_id() << std::endl;
}
