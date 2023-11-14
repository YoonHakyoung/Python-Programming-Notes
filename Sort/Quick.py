array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    # 원소 길이가 1
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    # 엇갈리기 전까지
    while (left <= right): #<=
        # 왼쪽에서부터 피벗보다 큰 값 찾기
        while (left <= end) and (array[left] <= array[pivot]): # array[left]<=array[pivot]
            left += 1
        while (right > start) and (array[right] >= array[pivot]):
            right -= 1
        # 엇갈렸으면 위치 바꾸기
        if left > right : 
            array[pivot], array[right] = array[right], array[pivot] #right : 작은 데이터
        # 아니면 작은 값이랑 큰 값 바꾸기
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

def quick_sort2(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_array = [x for x in tail if x <= pivot]
    right_array = [x for x in tail if x > pivot]

    return quick_sort2(left_array) + [pivot] + quick_sort2(right_array) #[pivot]

quick_sort(array, 0, len(array) - 1)
print("quick_sort :", array)

print("quick_sort2 :", quick_sort2(array))

'''
quick_sort 함수에서 리스트를 직접 조작하는 이유는 
파이썬에서 리스트는 mutable(가변)한 객체이기 때문입니다. 
함수에 전달된 mutable한 객체(리스트)를 변경하면 해당 객체는 원본의 변경을 반영합니다.

여기서 quick_sort 함수에 전달된 array는 원본 리스트를 가리키는 참조이기 때문에, 
함수 내에서 리스트를 변경하면 호출자(caller)에게도 영향을 미칩니다. 
이러한 특성은 함수 내에서 리스트를 조작하여 정렬할 때 편리하게 사용됩니다.

quick_sort2 함수에서는 리스트를 새로운 객체로 생성하고 반환하므로, 호출자에게 영향을 주지 않습니다. 
이는 함수형 프로그래밍 스타일에서 불변성(Immutability)을 지향하는 경우에 유용할 수 있습니다. 
불변성은 코드의 예측 가능성과 디버깅을 향상시킬 수 있습니다.
'''