// copyright
#include<bits/stdc++.h>
int main() {
    // 3桁のナルシシスト数
    for (int dgt1 = 1; dgt1 < 10; dgt1++) {
        for (int dgt2 = 0; dgt2 < 10; dgt2++) {
            for (int dgt3 = 0; dgt3 < 10; dgt3++) {
                int val1 = dgt1*dgt1*dgt1;
                int val2 = dgt2*dgt2*dgt2;
                int val3 = dgt3*dgt3*dgt3;
                int val = val1+val2+val3;
                int target_val = 100*dgt1 + 10*dgt2 + dgt3;
                if (val == target_val) {
                    std::cout << target_val << std::endl;
                }
            }
        }
    }
}
