# 비트마스크의 이용
# 1, 3, 5 방문했다면
# visited[1][0][1][0][1] = 1
# visited[10101] = 1
# 2^5 개의 노드 관리 가능.

# memo[cur][visited] = 현재 i 도시에 있고,
# 이 도시에서 visited 노드들을 거쳐 0으로 향하는 경로 중 최소값
# memo[cur][visited] = min(w[cur][next]+memo[next][방문 안한 남은거])

# << 오른쪽에 0을 추가
# >> 왼쪽에 0(0 또는 양의 정수) / 1(음의 정수)를 추가, 가장 오른쪽 1비트 사라짐

# (1 << n) - 1 은 n개의 비트를 모두 켜는 것. 1000000000000 - 1 이런식이니까 다 1이 되겠지?

# 시간복잡도 계산
# 하나의 사이클이 있다면 시작점은 중요하지 않다.
# 즉 현재 방문한 변수(cur)를 n개 돌리고,
# n개의 노드가 방문했는지 안했는지 0과 1로 돌리기에 2^n
# n *(2^n)
import sys
input = sys.stdin.readline

n = int(input())
w = []

for _ in range(n):
    w.append(list(map(int, input().split())))

INF = int(1e9)
VISITED_ALL = (1 << n) - 1
memo = [[None for _ in range(2**n)] for _ in range(n)]


def travel(cur, visited):
    # 전체 방문했다면
    if visited == VISITED_ALL:
        # 마지막 노드에서 0으로 돌아올 수 있다면 그대로 return
        if w[cur][0]:
            return w[cur][0]
        # 돌아올 수 없으면 INF 값 넣기
        else:
            return INF

    # 이미 방문했다면 원래 값 반환
    if memo[cur][visited] is not None:
        return memo[cur][visited]

    # 최소거리 구하기 시작
    min_dist = INF
    for j in range(n):
        # cur에서 j가 연결되어있지 않다면
        if not w[cur][j]:
            continue
        # 이미 방문한 도시면(visited 안에 j가 있으면)
        if visited & (1 << j):
            continue

        # cur부터 j까지의 거리 + travel(j, visited에 j 추가)
        min_dist = min(min_dist, w[cur][j] + travel(j, visited | (1 << j)))

    memo[cur][visited] = min_dist
    return memo[cur][visited]


print(travel(0, 1))
