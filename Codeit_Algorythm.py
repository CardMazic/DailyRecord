def binary_search(element, some_list):
    start_index = 0
    last_index = len(some_list) - 1
    while (start_index <= last_index):
        index = (start_index + last_index) // 2
        if(some_list[index] == element):
            return index

        elif (some_list[index] > element):
            # 찾는값보다 찾은값이 크다 탐색한 값보다 왼쪽 탐색한다
            # last_index의 값을 1 감소.
            last_index = index
            last_index -= 1
        else:
            start_index = index
            start_index += 1

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))