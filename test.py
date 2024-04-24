notdragon = [1000,1241,22,44,66,77,888]
ndonum = 2
dragon = notdragon + notdragon[:ndonum]
del dragon[:ndonum]

def binary_search(num, target):
    lo = 0
    hi = len(num) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if num[mid] > target:
            hi = mid - 1
            
        elif num[mid] < target:
            lo = mid + 1
            
        elif num[mid] == target:
            return mid + ndonum
        

