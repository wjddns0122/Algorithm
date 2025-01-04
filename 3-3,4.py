# 숫자 카드 게임
# 숫자 카드들이 N x M 형태로 놓여있다. 이때 N은 행의 개수를 의미하며 M은 열의 개수를 의미한다.
# 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
# 그 다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야한다.
# 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있는 전략을 세워야한다.
# • 입력 조건 : 첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여 각각 자연수로 주어진다. (1 <= N,M <=100)
# 둘째 줄 부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1 이상 10000 이하의 자연수이다.
# • 출력 조건 : 첫째 줄에 게임의 룰이 맞게 선택한 카드에 적힌 숫자를 출력한다

# • 입력 예시1 : 3 3        •출력 예시1:2
#              3 1 2
#              4 1 4
#              2 2 2
# • 입력 예시2 : 2 4        •출력 예시2:3
#              7 3 1 8
#              3 3 3 4

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
  data = list(map(int, input().split()))
  # 현재 줄에서 '가장 작은 수' 찾기
  min_value = min(data)
  # '가장 작은 수'들 중에서 가장 큰 수 찾기
  result = max(result, min_value)

print(result)


# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
  data = list(map(int, input().split()))
  # 현재 줄에서 '가장 작은 수' 찾기
  min_value = 10001
  for a in data:
    min_value = min(min_value, a)
  # '가장 작은 수'들 중에서 가장 큰 수 찾기
  result = max(result, min_value)

print(result)