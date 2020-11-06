def partition(arr, key, low, high):
    '''
    Partitioning the input
    @param arr: list
    @param key: str
    @param low: int
    @param high: int
    @return: (i + 1)
    '''
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        fun1 = getattr(arr[j], 'get_' + key)
        fun2 = getattr(pivot, 'get_' + key)
        if int(fun1()) >= int(fun2()):
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quick_sort(arr, key, low, high):
    '''
    Quick sort
    @param arr: list
    @param key: str
    @param low: int
    @param high: int
    @return:
    '''
    if low < high:
        pi = partition(arr, key, low, high)
        quick_sort(arr, key, low, pi - 1)
        quick_sort(arr, key, pi + 1, high)