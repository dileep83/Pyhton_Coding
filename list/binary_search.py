from Bs_application import Solution
def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == item:
            return mid
        elif list[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == '__main__':
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,543,64568,7859]
    print(binary_search(list, 543))
    s = Solution()
    print(s.searchInsert([1,3],3)) 
    