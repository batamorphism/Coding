// copyright
#include<iostream>

class A {
    using integer = int;
    integer m_value;

 public:
    void setter(integer value) {
        m_value = value;
    }
}

A::integer A::getter() {
    return m_value;
}
