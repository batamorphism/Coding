def main():
    n = int(input())
    A = list(map(int, input().split()))
    edge_list = [tuple(map(int, input().split())) for _ in range(n-1)]


