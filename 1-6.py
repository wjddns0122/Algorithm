# n, m = list(map(int, input().split()))

# for i in range(n):
#     for j in range(m):
#         print("*", end=" ")
#     print()

# n = int(input())

# for i in range(n, 0, -1):
#     print("* " * i)

# n = int(input())

# for i in range(1, n + 1):
#     for _ in range(1,i * 2):
#         print('*',end='')
#     print()

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i * j, end=" ")
#     print()

# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if j < n:
#             print(f"{i} * {j} = {i*j}",end=", ")
#         else:
#             print(f"{i} * {j} = {i*j}",end="")
#     print()

# n = int(input())

# for i in range(1, n + 1):
#     for j in range(0, i):
#         print(i, end=" ")
#     print()
    

# a, b = list(map(int, input().split()))

# while a <= b:
#     print(a, end=" ")

#     if a % 2 == 1:  # 홀수일 때
#         if a * 2 <= b:
#             a *= 2
#         else:
#             break
#     elif a % 2 == 0:  # 짝수일 때
#         if a + 3 <= b:
#             a += 3
#         else:
#             break   


# n = int(input())


# for _ in range(n):
#     a, b = map(int, input().split())
#     total = 0
#     for i in range(a, b + 1):
#         if i % 2 == 0:
#             total += i

#     print(total)

start, end = list(map(int, input().split()))
# count = 0


# divisorsList = []

# for i in range(1, start + 1):
#     if (start % i == 0) :
#         divisorsList.append(i)

#     if len(divisorsList) == 3:
#         count += 1

# print(count)


# 변수 선언 및 입력:
# inp = input()
# arr = inp.split()
# start, end = int(arr[0]), int(arr[1])

# ans = 0
# for curr_num in range(start, end + 1):
#     # Step 1:
#     divisor_cnt = 0
#     for divisor in range(1, curr_num + 1):
#         if curr_num % divisor == 0:
#             divisor_cnt += 1
#     # Case 1:
#     if divisor_cnt == 3:
#         ans += 1

# print(ans)
