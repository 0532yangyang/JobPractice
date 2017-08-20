# -*- coding: utf-8 -*-




# 二分查找
def binary_search(a, low, high, target):
    if low > high:
        return False
    while low <= high:
        mid = low + (high-low)/2
        if a[mid] > target:
            high = mid-1
        elif a[mid] < target:
            low = mid+1
        else:
            return mid
    return False


if __name__ == '__main__':
    a = [1,2,3,4,5]
    target = 8
    print binary_search(a,0,len(a)-1, target)
