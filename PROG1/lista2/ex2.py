def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if(nums[i] + nums[j] == target):
                return([i,j])
    return("Nao existem a,b em nums satisfazendo a+b = target")            

"""
print(two_sum([1,2,3,4,10,20,8], 31))
print(two_sum([3,3,3,1,3,3,3], 2))
"""