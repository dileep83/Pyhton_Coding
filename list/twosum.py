import time

class solution(object):
    def __init__(self,nums,target):
        self.nums=nums
        self.target=target
        
    def twoSum(self,nums,target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if self.nums[i]+ self.nums[j] == target:
                    return [i,j]
        return "no two numbers found for target"
                
                
    def twoSum2(self,nums,target):
        s= {}
        for i in range(len(nums)):
            if target-nums[i] in s:
                return [i,s[target-nums[i]]]
            else:
                s[nums[i]]= i
        
        
        
if __name__=="__main__":              
    s = solution([1,23,236,45,37,456,3756,567,8,5,2,567],7)
    
    print(s.twoSum2(s.nums,s.target))
    
    
    
    
