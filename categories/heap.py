# -*- coding: utf-8 -*-

# 1. http://javayhu.me/blog/2014/05/08/python-data-structures---c3-data-structures/
# 2. http://interactivepython.org/runestone/static/pythonds/Trees/BinaryHeapImplementation.html#lst-heap3

class Bin_Heap():    # 小顶堆
    def __init__(self):
        self.a = []
        self.cur_size = -1

    # ----- 建堆 ----
    def build_heap(self, a_list):
        self.a = [0] + a_list    # 0 占位，不计数
        self.cur_size = len(a_list)
        i = self.cur_size / 2  # 不包括占位符
        while i > 0:
            self.perc_down(i)
            i -= 1

    # 下调
    def perc_down(self, i):
        while i*2 <= self.cur_size:
            min_child_idx = self.min_child(i)
            if self.a[i] > self.a[min_child_idx]:
                self.a[min_child_idx], self.a[i] = self.a[i], self.a[min_child_idx]
            i *= 2  #错的

    def min_child(self, i):
        if i*2+1 > self.cur_size:
            return i*2
        else:
            if self.a[i*2] < self.a[i*2+1]:
                return i*2
            else:
                return i*2+1

    # ---- 堆排序 ----
    def sort(self):
        while self.cur_size > 0:
            print self.pop_min()

    def pop_min(self):
        val = self.a[1]
        self.a[1] = self.a[self.cur_size]    # 如果只有一个元素，就相当于白做了一次，但也会被pop删除的。
        self.cur_size -= 1
        self.a.pop()
        self.perc_down(1)
        return val


    def insert(self, k):
        self.a.append(k)
        self.cur_size += 1
        self.perc_up(self.cur_size)

    # 上调
    def perc_up(self, i):
        while i/2 > 0:
            if self.a[i] < self.a[i/2]:
                self.a[i], self.a[i/2] = self.a[i/2], self.a[i]
            i /= 2


if __name__ == '__main__':
    pass