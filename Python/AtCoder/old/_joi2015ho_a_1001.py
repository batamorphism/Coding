from collections import namedtuple

Edge = namedtuple('Edge', ['a', 'b', 'c'])


def main():
    n, m = map(int, input().split())
    trip_list = list(map(int, input().split()))
    for i in range(m):
        trip_list[i] -= 1
    train_list = []
    # train_list[i]はiとi+1をつなぐ
    for _ in range(n-1):
        a, b, c = map(int, input().split())
        edge = Edge(a, b, c)
        train_list.append(edge)

    imos = [0]*n
    # count_how_many_use_train
    for trip_from_i in range(m-1):
        trip_to_i = trip_from_i+1
        trip_from = trip_list[trip_from_i]
        trip_to = trip_list[trip_to_i]
        lo = min(trip_from, trip_to)
        hi = max(trip_from, trip_to)
        imos[lo] += 1
        imos[hi] -= 1

    cost = 0
    cnt = 0
    for i in range(n-1):
        edge: Edge
        edge = train_list[i]
        cnt += imos[i]
        cost_of_i = calc_cost(edge.a, edge.b, edge.c, cnt)
        cost += cost_of_i

    print(cost)


def calc_cost(a, b, c, cnt):
    return min(a*cnt, b*cnt+c)


main()
