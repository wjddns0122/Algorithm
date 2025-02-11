# 큰 수의 법칙
# 예를 들어 순서대로 2, 4, 5, 4, 6으로 이루어진 배열이 있을때 M은 8이고, K가 3이라 가정하자.
# 이 경우 특정한 인덱스의 수가 연속해서 세번까더만 더해질 수 있으므로 큰 수의 법칙에 따라 6+6+6+5+6+6+6+5인 46이된다

# 이 알고리즘을 짜면 ?
# 입력 예시
# 5 8 3
# 2 4 5 4 6

# 출력 예시
# 46


# n, m, k를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# n개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()     # 입력받은 수 정렬
first = data[n - 1]   # 가장 큰 수
second = data[n - 2]    # 두 번째로 큰 수

result = 0

while True:
  for i in range(k):     #가장 큰 수를 k번 더하기
    if m == 0:        #m이 0이면 반복문 탈출
      break
    result += first
    m -= 1       # 더할 때마다 1씩 빼기
  if m == 0:     # m이 0이라면 반복문 탈출
    break
  result += second     # 두 번째로 큰 수를 한번 더하기
  m -= 1       # 더할 때마다 1씩 빼기

print(result)


# 이 방법이 M의 크기가 10000 이하이므로 이방식으로 간단하게 풀 수가 있지만 M의 크기가 100억이상으로 커진다면 시간 초과가 날것이다.
# 그렇다면 반복되는 수열의 길이는 (k+1)
# M을 (k+1)로 나누면 그만큼 수열이 반복된다. 그치만 나눠떨어지지 않을 수도 있으므로 식은 다음과 같다.
# int(m/(k+1)) * k + m % (k + 1)




# n, m, k를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()    # 입력받은 수 정렬
first = data[n-1]     # 가장 큰 수
second = data[n-2]     # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first      # 가장 큰 수 더하기
result += (m - count) * second     # 두 번째로 큰 수 더하기

print(result)