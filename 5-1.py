stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)  # 최종 스택 상태: [5, 2, 3, 1]
print(stack[::-1])  # 스택에 저장된 원소 출력(역순으로)