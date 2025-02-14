# 0인덱스와 1인덱스의 원소 고치기
array = [3, 5]
array[0], array[1] = array[1], array[0]

print(array)  # [5, 3]

# if C++ code is written in Python, it will be like this:
# int main() {
#     int a = 3;
#     int b = 5;
#     // 스와프 진행
#     int temp = a;
#     a = b;    b = temp;