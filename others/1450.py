# 무게와 가치가 주어지고 가치의 최댓값을 구하는 문제 -> nk 이므로 1000만
# 무게만 주어지고 넣는 방법의 수 다 구하는 문제 -> 넣거나 안넣거나 2, 물건 30개이므로 2^30? 너무 크다!
# 사실상 부분집합을 구하되, 무게제한이 있는 문제
# meet in the middle 알고리즘
# 1. 집합을 두개로 나눈다
# 2. 왼쪽 집합에서 뽑을 수 있는 경우의 수들의 합을 구한다.
# 3. 오른쪽 집합에서 뽑을 수 있는 경우의 수들의 합을 구한다.
# 4. 두개를 합쳤을 때 최댓값보다 작은 숫자의 개수를 구한다
from itertools import combinations

n, W = map(int, input().split())
weigh = list(map(int, input().split()))

if n == 1:
    if weigh[0] <= W:
        print(2)
    else:
        print(1)

else:
    list_left = weigh[:n//2]
    list_right = weigh[n//2:]

    sum_left = []
    sum_right = []
    # 왼쪽에서 0개의 합 ~ n개의 합 구하기 (같은 무게여도 다른 물건임)
    for i in range(len(list_left)+1):
        for subset in combinations(list_left, i):
            sum_left.append(sum(subset))

    # 오른쪽에서 0개의 합 ~ n개의 합 구하기
    for i in range(len(list_right)+1):
        for subset in combinations(list_right, i):
            sum_right.append(sum(subset))

    # 오른쪽 배열 정렬
    sum_right.sort()

    # 왼쪽 배열 값을 순회하면서, 각 item마다 오른쪽 배열 순회
    # 오른쪽 배열의 item과 더했을 때 기준값 넘어가면 안됨.
    # 이미 오른쪽 배열을 정렬했으니, 직접 다 더해보지 않더라도 이 경계값을 찾으면 개수를 구할 수 있음

    cnt = 0
    for item_left in sum_left:
        # 이미 왼쪽만으로도 넘어가는 경우는 제외
        if item_left > W:
            continue

        left = 0
        right = len(sum_right) - 1

        while left <= right:
            mid = (left+right)//2

            if item_left + sum_right[mid] <= W:
                left = mid + 1
            else:
                right = mid - 1

        # right 값은 item_left 한 개에서 만들 수 있는 조건을 만족하는 최댓값의 인덱스
        cnt += (right+1)

    print(cnt)
