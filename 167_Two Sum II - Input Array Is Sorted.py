# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    left_pointer=0
    right_pointer=len(numbers)-1
    while left_pointer<right_pointer:
        total=numbers[left_pointer]+numbers[right_pointer]
        if total>target:
            right_pointer-=1
        elif total<target:
            left_pointer+=1
        else:
            return [left_pointer+1, right_pointer+1]

if __name__=='__main__':
    nums = [3,2,4]
    target = 6
    twoSum(nums, target)
    






