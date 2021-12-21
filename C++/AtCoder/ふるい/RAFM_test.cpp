// copyright
#include<bits/stdc++.h>

void write_log(clock_t st, clock_t en) {
    double time = static_cast<double> (en - st) / CLOCKS_PER_SEC;
    std::cout << time << " sec" << std::endl;
}

int64_t myfnc(int64_t bit1, int64_t bit2) {
    return bit1 ^ bit2;
}

int64_t myfnc_with_var(int64_t bit1, int64_t bit2) {
    std::vector<int64_t> s(100);
    return bit1 ^ bit2;
}

int64_t myfnc_rec(int64_t i) {
    if (i == 0) {
        return 0;
    }
    return myfnc_rec(i-1)+1;
}

/**
 * @brief LookUpKeyが文字列の時と整数の時の比較
 * 
 * @param i_end 
 */
void section1(int64_t i_end) {
    std::cout << "Section 1" << std::endl;
    {
        std::cout << "int vs int" << std::endl;
        clock_t start = clock();
        bool flg;
        int test = 1;
        for (int64_t i = 0; i < i_end; i++) {
            flg = (test == 1);
        }
        clock_t end = clock();
        write_log(start, end);
    }
    {
        std::cout << "str vs str, len=4, true" << std::endl;
        clock_t start = clock();
        bool flg;
        std::string test = "TEST";
        for (int64_t i = 0; i < i_end; i++) {
            flg = (test == "TEST");
        }
        clock_t end = clock();
        write_log(start, end);
    }
    {
        std::cout << "str vs str, len=4, false" << std::endl;
        clock_t start = clock();
        bool flg;
        std::string test = "TEST";
        for (int64_t i = 0; i < i_end; i++) {
            flg = (test == "ABCD");
        }
        clock_t end = clock();
        write_log(start, end);
    }
    {
        std::cout << "str vs str, len=100, true" << std::endl;
        clock_t start = clock();
        bool flg;
        std::string test = "ABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDE";
        for (int64_t i = 0; i < i_end; i++) {
            flg = (test == "ABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDE");
        }
        clock_t end = clock();
        write_log(start, end);
    }
}

/**
 * @brief external functionとinlineの確認
 * 
 * @param i_end 
 */
void section2(int64_t i_end) {
    std::cout << "Section 2" << std::endl;
    {
        std::cout << "call other procedure" << std::endl;
        clock_t start = clock();
        int64_t ans = -1;
        for (int64_t i = 0; i < i_end; i++) {
            ans = myfnc(i, ans);
        }
        clock_t end = clock();
        write_log(start, end);
    }
    {
        std::cout << "calc inline" << std::endl;
        clock_t start = clock();
        int64_t ans = -1;
        for (int64_t i = 0; i < i_end; i++) {
            ans = ans & i;
        }
        clock_t end = clock();
        write_log(start, end);
    }
    {
        std::cout << "call other procedure with local variables" << std::endl;
        clock_t start = clock();
        int64_t ans = -1;
        for (int64_t i = 0; i < i_end; i++) {
            ans = myfnc_with_var(i, ans);
        }
        clock_t end = clock();
        write_log(start, end);
    }
    {
        std::cout << "call inline with local variables" << std::endl;
        clock_t start = clock();
        int64_t ans = -1;
        for (int64_t i = 0; i < i_end; i++) {
            std::vector<int64_t> s(100);
            ans = myfnc_with_var(i, ans);
        }
        clock_t end = clock();
        write_log(start, end);
    }
}

/**
 * @brief Table+vuk vs array
 * 
 * @param i_end 
 */
void section3(int64_t i_end) {
    std::cout << "Section 3" << std::endl;
    std::map<int64_t, double> table1;
    std::unordered_map<int64_t, double> table2;
    std::vector<double> table3(1000);
    double table4[1000];
    std::map<std::string, double> table5;
    // setup table
    for (int64_t key = 0; key < 1000; key++) {
        table1[key] = key+0.5;
        table2[key] = key+0.5;
        table5[std::to_string(key)] = key+0.5;
    }

    {
        std::cout << "look up table" << std::endl;
        clock_t start = clock();
        double ans = 0;
        for (int64_t i = 0; i < i_end; i++) {
            ans += table1[i%1000];
        }
        clock_t end = clock();
        write_log(start, end);
    }

    {
        std::cout << "look up hash table" << std::endl;
        clock_t start = clock();
        double ans = 0;
        for (int64_t i = 0; i < i_end; i++) {
            ans += table2[i%1000];
        }
        clock_t end = clock();
        write_log(start, end);
    }

    {
        std::cout << "look dynamic array" << std::endl;
        clock_t start = clock();
        double ans = 0;
        for (int64_t i = 0; i < i_end; i++) {
            ans += table3[i%1000];
        }
        clock_t end = clock();
        write_log(start, end);
    }
    {
        std::cout << "look static array" << std::endl;
        clock_t start = clock();
        double ans = 0;
        for (int64_t i = 0; i < i_end; i++) {
            ans += table4[i%1000];
        }
        clock_t end = clock();
        write_log(start, end);
    }
    {
        std::cout << "look up table with string" << std::endl;
        clock_t start = clock();
        double ans = 0;
        for (int64_t i = 0; i < i_end; i++) {
            ans += table5[std::to_string(i%1000)];
        }
        clock_t end = clock();
        write_log(start, end);
    }
}

/**
 * @brief 再帰とforの比較
 * 
 * @param i_end 
 */
void section4(int64_t i_end) {
    std::cout << "Section 4" << std::endl;
    {
        std::cout << "calc recursion" << std::endl;
        clock_t start = clock();
        int64_t ans = 0;
        ans = myfnc_rec(i_end);
        clock_t end = clock();
        write_log(start, end);
    }
    {
        std::cout << "calc for loop" << std::endl;
        clock_t start = clock();
        double ans = 0;
        for (int64_t i = 0; i < i_end; i++) {
            ans += 1;
        }
        clock_t end = clock();
        write_log(start, end);
    }
}

int main() {
    int64_t i_end = 100000000;  // 10**8
    section1(i_end);
    section2(i_end);
    section3(i_end);
}
