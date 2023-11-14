array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    #가장 작은 원소의 인덱스
	min_index = i

    # 현재 인덱스의 값보다 작은 원소 찾으면 업데이트
	for j in range(i + 1, len(array)):
		if array[min_index] > array[j]:
			min_index = j
	array[i], array[min_index] = array[min_index], array[i]

print(array)