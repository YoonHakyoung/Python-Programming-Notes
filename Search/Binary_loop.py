def binary_search (array, target, start, end):
    while (start <= end):
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None
    
n, target = map(int, input().split())
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None: 
    print("찾는 결과가 없습니다.")
else : 
    print("해당 값은 {}번째 위치에 있습니다.".format(result+1))