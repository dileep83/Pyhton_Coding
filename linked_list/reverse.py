# import sys
# sys.path.append('../') why we can't import without this ?

from list.twosum import solution
if __name__ == '__main__':
    nums = [1,56,2,1,45,33,78,435,56,76,57,57]
    target = 3
    s = solution(nums,target)
    print(s.twoSum2(nums , target))