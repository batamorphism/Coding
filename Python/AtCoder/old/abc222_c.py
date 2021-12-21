import heapq as hq


def main():
    n, m = map(int, input().split())
    A = []
    for _ in range(2*n):
        A.append(list(input()))
    ranking = []
    for human in range(2*n):
        score = 0
        hq.heappush(ranking, (0, -score, human))

    for round in range(m):
        for _ in range(n):
            cnt1, score1, human1 = hq.heappop(ranking)
            cnt2, score2, human2 = hq.heappop(ranking)
            score1 = score1*-1
            score2 = score2*-1
            a1 = A[human1][round]
            a2 = A[human2][round]
            if a1 == 'G' and a2 == 'C':
                score1 += 1
            elif a1 == 'G' and a2 == 'P':
                score2 += 1
            elif a1 == 'C' and a2 == 'P':
                score1 += 1
            elif a1 == 'C' and a2 == 'G':
                score2 += 1
            elif a1 == 'P' and a2 == 'G':
                score1 += 1
            elif a1 == 'P' and a2 == 'C':
                score2 += 1
            else:
                pass
            cnt1 += 1
            cnt2 += 1
            hq.heappush(ranking, (cnt1, -score1, human1))
            hq.heappush(ranking, (cnt2, -score2, human2))

    ranking.sort()
    for _, _, human in ranking:
        print(human+1)


main()
