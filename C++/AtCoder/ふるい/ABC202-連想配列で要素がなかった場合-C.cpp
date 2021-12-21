# include<bits/stdc++.h>

/**
 * @brief 
 * A[i] = B[C[j]]となるものを求めよ
 * n<=10**5
 * @param n 
 * @param A 
 * @param B 
 * @param C 
 */
void solver(int n,
            std::vector<int> A,
            std::vector<int> B,
            std::vector<int> C) {
    // 各A[i]
    // B[C[i]]をBC[i]としておく
    // BC[i], iからなる連想配列を作成しておく
    std::vector<int> BC(n);
    for (int i = 0; i < n; i++) {
        BC[i] = B[C[i]];
    }
    std::map<int, std::vector<int>> BC_ind_of;
    for (int i = 0; i < n; i++) {
        BC_ind_of[BC[i]].push_back(i);
    }
    int64_t ans = 0;
    for (int i = 0; i < n; i++) {
        std::vector<int> k_list;
        auto found = BC_ind_of.find(A[i]);
        if (found != BC_ind_of.end()) {
            k_list = found->second;
        }
        ans += k_list.size();
    }
    std::cout << ans << std::endl;
}

int main() {
    // input
    int n;
    std::cin >> n;
    std::vector<int> A(n);
    std::vector<int> B(n);
    std::vector<int> C(n);
    for (int i = 0; i < n; i++) {
        int foo;
        std:: cin >> foo;
        A[i] = foo;
    }
    for (int i = 0; i < n; i++) {
        int foo;
        std:: cin >> foo;
        B[i] = foo;
    }
    for (int i = 0; i < n; i++) {
        int foo;
        std:: cin >> foo;
        C[i] = foo-1;
    }
    solver(n, A, B, C);
}

// https://zenn.dev/nariakiiwatani/articles/33152127379b3e
int test() {
    std::map<int, int> m;
    // 要素を追加や編集するとき
    // 存在しない場合は追加、存在する場合は無視
    m.insert(std::make_pair(0, 10));
    // m.findは遅いので使わない
    // 例えば、if(m.find(0) == end(m))とするのは遅い

    // 存在しない場合は無視、存在する場合は上書き
    auto found = m.find(0);
    if(found != end(m)) {
        found->second = 10;
    }

    // 存在しない場合は追加、存在する場合は上書き
    m[0] = 10;

    // 要素にアクセスするとき
    // キーが存在する場合はその値を、しない場合は指定の値を使用
    // (指定の値を追加しない)
    auto found = m.find(0);
    int default_value = 0;
    int ret = 0;
    if (found == end(m)) {
        ret = default_value;
    }
    ret = found->second;
    // []は使わない

    // キーが存在する場合はその値を、しない場合はデフォルト値を返す
    // map::mapped_typeがデフォルトコンストラクタを持つ場合のみ
    ret = m[0]; // 実際は、intには初期値がないのであかんと思う

}