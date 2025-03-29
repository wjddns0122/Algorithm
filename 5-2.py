from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()  # 가장 왼쪽에 있는 원소 삭제
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)  # 먼저 들어오는 순서대로 출력
queue.reverse()
print(queue)  # 나중에 들어온 원소부터 출력