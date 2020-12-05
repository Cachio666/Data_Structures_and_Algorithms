def max_heapify(A, n, i):
    """
    对堆的第i个结点进行最大堆维护
    :param A: 需要实现的堆
    :param n: 需要操作的堆数据的长度
    :param i: 需要维护的堆结点的位置
    :return:None
    """
    left = 2 * (i + 1) - 1  # 左子结点
    right = left + 1  # 右子结点
    # largest用来标记局部最大值
    if left < n and A[left] > A[i]:
        largest = left
    else:
        largest = i
    if right < n and A[right] > A[largest]:
        largest = right
    if largest != i:
        # 维护最大堆性质
        A[i], A[largest] = A[largest], A[i]
        # 对子结点进行最大堆维护
        max_heapify(A, n, largest)


def build_max_heap(A, n):
    """
    建立最大堆
    :param A: 需要建立堆的原始数组
    :param n: 数组长度
    :return: None
    """
    for i in range(n // 2, -1, -1):
        # 对堆的每个非叶结点进行最大堆维护
        max_heapify(A, n, i)


def heap_sort(A):
    """
    堆排序——原址排序
    :param A: 需要排序的数组
    :return: None
    """
    n = len(A)
    build_max_heap(A, n)
    for i in range(n - 1):
        A[n-1], A[0] = A[0], A[n-1]
        n -= 1
        max_heapify(A, n, 0)


