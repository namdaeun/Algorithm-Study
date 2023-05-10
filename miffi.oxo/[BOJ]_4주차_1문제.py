# 1149. RGB거리

# 첫째 줄에 집의 수 n을 입력
n = int(input())

house = []

# 둘째 줄부터 n개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용을 1번 집부터 한 줄에 하나씩 입력 받아 house 리스트에 저장
for i in range(n):
    r, g, b = map(int, input().split())
    house.append([r, g, b])

# 문제의 조건을 만족하며 모든 집을 칠하는 비용의 최솟값을 구해야 함
# house[i][0] : i번째 집을 빨간색으로 칠할 때의 최소 비용 (빨간색으로 칠하기 위해서는 이전 집을 초록색이나 파란색으로 칠해야 함)
# house[i][1] : i번째 집을 초록색으로 칠할 때의 최소 비용 (초록색으로 칠하기 위해서는 이전 집을 빨간색이나 파란색으로 칠해야 함)
# hosue[i][2] : i번째 집을 파란색으로 칠할 때의 최소 비용 (파란색으로 칠하기 위해서는 이전 집을 빨간색이나 초록색으로 칠해야 함)
for i in range(1, n):
    house[i][0] += min(house[i - 1][1], house[i - 1][2])
    house[i][1] += min(house[i - 1][0], house[i - 1][2])
    house[i][2] += min(house[i - 1][0], house[i - 1][1])

# 위의 과정을 n번 반복하면 house[n - 1][0] ~ house[n - 1][2]에 각각 빨간색, 초록색, 파란색으로 칠했을 때의 최소 비용이 저장됨
# 이 중 가장 작은 값 출력
print(min(house[n - 1]))
