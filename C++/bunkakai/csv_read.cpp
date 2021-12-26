//copyright
#include<bits/stdc++.h>
#include <Windows.h>

/**
 * @brief 文字列を区切り文字で区切った配列を返す
 *
 * @param input 区切る対象の文字列
 * @param delimiter 区切り文字
 * @return std::vector<std::string> delimiterで区切った文字列を格納したvector
 */
std::vector<std::string> split(const std::string& input, char delimiter) {
    std::istringstream stream(input);
    std::string field;
    std::vector<std::string> result;
    while (getline(stream, field, delimiter)) {
        result.push_back(field);
    }
    return result;
}

/**
 * @brief iostreamを使う方法。
 *
 * @param csv_path 読み込むCSVファイルのフルパス
 */
void ifstream_test(std::string csv_path) {
    DWORD start =  GetTickCount();
    std::ifstream ifs(csv_path);
    std::string line;
    double ans = 0.;
    while (std::getline(ifs, line)) {  // <- 1行ずつ読まれるため、ここは高速
        auto row = split(line, ',');  // <- ここがボトルネック
        ans += std::stod(row.at(2));  // <- 1回しかキャストしていない
    }
    std::cout << ans << std::endl;
    DWORD end =  GetTickCount();
    std::cout << static_cast<double>(end - start) / 1000 << "sec" << std::endl;
}

/**
 * @brief iostreamを使う方法。全行全列に対し型変換を行うケース。
 *
 * @param csv_path 読み込むCSVファイルのフルパス
 */
void ifstream_test_all_cast(std::string csv_path) {
    DWORD start =  GetTickCount();
    std::ifstream ifs(csv_path);
    std::string line;
    double ans = 0.;
    while (std::getline(ifs, line)) {  // <- 1行ずつ読まれるため、ここは高速
        auto row = split(line, ',');  // <- ここがボトルネック
        std::vector<double> row_double(0.);
        for (auto s : row) {
            row_double.push_back(std::stod(s));
        }
        ans += row_double.at(2);
    }
    std::cout << ans << std::endl;
    DWORD end =  GetTickCount();
    std::cout << static_cast<double>(end - start) / 1000 << "sec" << std::endl;
}

/**
 * @brief C言語の標準ライブラリを用いる方法
 *
 * @param csv_path 読み込むCSVファイルのフルパス
 */
void c_lang_lib_test(std::string csv_path) {
    DWORD start =  GetTickCount();
    FILE *fp = fopen(csv_path.c_str(), "r");
    std::vector<char> buffer(1024*1024);

    std::string line;
    double ans = 0.;
    while (fgets(buffer.data(), buffer.size(), fp) != NULL) {
        std::string row_str(buffer.data());
        auto row = split(row_str, ',');  // <-ここがボトルネック
        ans += std::stod(row.at(2));
    }
    fclose(fp);
    std::cout << ans << std::endl;
    DWORD end =  GetTickCount();
    std::cout << static_cast<double>(end - start) / 1000 << "sec" << std::endl;
}

int main() {
    auto csv_path = "D:\\Users\\Takanori\\Documents\\bunkakai\\dataset_small.csv";
    std::cout << "ifstream_test" << std::endl;
    ifstream_test(csv_path);
    std::cout << "ifstream_test_all_cast" << std::endl;
    ifstream_test_all_cast(csv_path);
    std::cout << "c_lang_lib_test" << std::endl;
    c_lang_lib_test(csv_path);
    return 0;
}
