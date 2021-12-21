// Copyright
#include<bits/stdc++.h>

bool is_on_same_line(
    std::vector<int> point1,
    std::vector<int> point2,
    std::vector<int> point3
    ) {
    /**
     * @1brief
     * rx = (point3[0]-point1[0])/(point2[0]-point1[0])
     * これがryと同じである
     * すなわち、
     * (point3[0]-point1[0])*(point2[1]-point1[1])
     * (point3[1]-point1[1])*(point2[0]-point1[0])
     * の2つが一致
     */
    return (point3[0]-point1[0])*(point2[1]-point1[1])
        == (point3[1]-point1[1])*(point2[0]-point1[0]);
}

void solver(std::vector<std::vector<int>> points, int n) {
    bool is_no = true;
    for (int i = 0; i < n-2; i++) {
        for (int j = i+1; j < n-1; j++) {
            for (int k = j+1; k < n; k++) {
                if (is_on_same_line(points[i], points[j], points[k])) {
                    is_no = false;
                }
            }
        }
    }
    if (is_no) {
        std::cout << "No" << std::endl;
    } else {
        std::cout << "Yes" << std::endl;
    }
}

int main() {
    // input
    int n;
    std::cin >> n;
    std::vector<std::vector<int>> points(n, std::vector<int>(n));
    int x, y;
    for (int i = 0; i < n; i++) {
        std::cin >> x >> y;
        points[i][0] = x;
        points[i][1] = y;
    }
    solver(points, n);
}
