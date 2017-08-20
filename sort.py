# -*- coding: utf-8 -*-

# 直接插入排序
# 将一个数据插入到已经排好序的有序数据中
def insert_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while j>=0 and a[j]>key:
            a[j+1] = a[j]    # 往后挪一个
            j -= 1
        # j=-1时，j+1=插入位置； a[j]<或等于key, 退出（）。
        a[j+1] = key
    return a


# 冒泡排序:
def bubble_sort(a):
    tail = len(a)-1    # tail：无序部分尾端
    while tail >= 0:
        for j in range(0, tail):
            if a[j+1] < a[j]:
                a[j+1], a[j] = a[j], a[j+1]
        tail -= 1
    return a



# 快速排序: 通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小。 递归.
def quick_sort(a, low, high):
    if low >= high:
        return a    # 是有返回值的
    i = low
    j = high
    key = a[i]
    while i<j:
        while i<j and a[j]>=key:    # 等于号
            j-=1
        a[i] = a[j]
        while i<j and a[i] <= key:   # 等于号
            i+=1
        a[j] = a[i]
    a[i] = key
    quick_sort(a, low, i - 1)
    quick_sort(a, i + 1, high)
    return a    # 是有返回值的


# 逆序输出
def heap_sort(a):
    def bulid_heap(a):
        i = len(a)/2
        endNode = len(a)-1
        while i > 0:
            perc_down(a, i, endNode)
            i -= 1

    def perc_down(a, i, endNode):
        while i*2 <= endNode:
            if i*2+1 <= endNode:    # 有右孩子
                smaller = i*2 if a[i*2]<a[i*2+1] else i*2+1
            else:
                smaller = i*2
            if a[smaller] < a[i]:
                a[i], a[smaller] = a[smaller], a[i]
                i = smaller
            else: break

    a = [None] + a
    bulid_heap(a)
    i = len(a)-1
    while i>=2:
        a[i], a[1] = a[1], a[i]
        perc_down(a, 1, i-1)
        i-=1
    return a[1:]


if __name__ == '__main__':
    a = [5,2,1,3,4]
    a = [5,0,1,4,2,3]
    print heap_sort(a)