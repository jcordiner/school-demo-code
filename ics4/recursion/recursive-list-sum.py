# summing a list

# [1,2,3,4,5]
def summer(nums):
  
  if len(nums) == 2:
    # base case
    # reduce the problem - just two things left, add them
    return nums[0] + nums[1] 
  else:
    # reduce the problem - add first thing to rest of list
    # recursive call
    return nums[0] + summer(nums[1:])
      
print summer([1,2,3,4,5])