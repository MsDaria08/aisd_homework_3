vec = [4, 3, 2, 1, 2, 2, 7, 8, 9]
# необходимо пофиксить повторяющиеся слова
# vec = [ 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2]
# а как это сделать с учетом минимальной сложности по времени?

def FindMin(vec):
    left = 0
    right = len(vec)
    if right == 1:
        return 0
    if right == 2 and vec[1] > vec[0]:
        return 0
    elif right == 2 and vec[1] < vec[0]:
        return 1
    while left < right:
        mid = (right + left) // 2
        if vec[mid] < vec[mid - 1] and vec[mid] < vec[mid + 1]:
            return mid
        if vec[mid] > vec[mid - 1] and vec[mid] <= vec[mid + 1]:
            right = mid - 1
            continue
        if vec[mid] < vec[mid - 1] and vec[mid] >= vec[mid + 1]:
            left = mid + 1
            continue
        if vec[mid] >= vec[mid - 1] and vec[mid] >= vec[mid + 1]:
            left = mid
            continue
    return left

print(FindMin(vec))


