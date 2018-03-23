# -*- coding:utf-8 -*-

def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    for i in range(n-1):
        count = 0
        for j in range(n-1-i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j+1] = alist[j + 1], alist[j]
                count += 1
        if 0 == count:
            return

def binary_serch(alist, item):
    """二分查找 递归"""
    n = len(alist)
    if n > 0:
        mid = n//2
        print mid
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            print alist[:mid]
            return binary_serch(alist[:mid], item)
        else:
            return binary_serch(alist[mid+1:], item)
    return False

def binary_search_2(alist, item):
    """ 二分查找 ， 非递归"""
    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:
        mid = (first + last)//2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


if __name__ == "__main__":
    li = [1, 6, 3, 2, 4, 5]
    bubble_sort(li)
    print li
    print binary_serch(li, 3)
    print binary_serch(li, 7)
    print 10%3, 10//3