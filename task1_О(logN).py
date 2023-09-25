vec = [3, 5, 2, 1, 3, 6, 7, 9]

def FindPick(vec):
    left = 0
    right = len(vec) - 1
    while left < right:
        mid = (left + right) // 2
        if vec[mid] > vec[mid - 1] and vec[mid] > vec[mid + 1]:
            return mid
        if vec[mid - 1] > vec[mid]:
            right = mid - 1
            if right == -1:
                return mid
            continue
        if vec[mid + 1] > vec[mid]:
            left = mid + 1
            if left == len(vec) - 1:
                return mid + 1
            continue


print(FindPick(vec))