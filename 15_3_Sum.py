# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and 
# j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    combinations = []
    nums.sort() # n log n
    
    N = len(nums)
    for i in range(0, N-2):
        left_ind = i + 1
        right_ind = N-1
        
        while (left_ind < right_ind):
            x, y, z = nums[i], nums[left_ind], nums[right_ind]
            triplet = x + y + z
            if triplet == target:
                combinations.append((x,y,z))
                left_ind+=1
                right_ind-=1
            elif triplet < target:
                left_ind += 1
            elif triplet > target:
                right_ind -= 1
    return list(set(combinations)) 



if __name__=='__main__':
    nums = [-2,0,1,1,2]
    target=0
    threeSum(nums, 0)




    
