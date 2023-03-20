class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        if len(nums) == 1 and target == nums[0]:
            return 0
        if target == nums[-1] :
            return len(nums)-1
        if target > nums[-1] :
            return len(nums)
        if target <= nums[0]:
            return 0
        while(left <= right):
            mid = (left +right)// 2
            if nums[mid] == target and nums[mid+1] > target :
                return mid
            elif  target > nums[mid] :
                left = mid+1
            else:right = mid-1
        return right+1
    
    def searchInRotatedArray(self, nums, target):
        left = 0    
        right = len(nums)-1
    
        while(left <= right):
            mid = (left + right)// 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid+1
            else:
                right = mid-1
                
                
                
                
    
        
            
    
        