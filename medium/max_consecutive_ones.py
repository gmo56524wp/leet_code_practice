# sliding window algorithm
k = input()  # integer
nums = input()  # array of integer
begin = 0
end = 0
while end < len(nums):
    if nums[end] == 0:
        k -= 1
    if k < 0:
        if nums[begin] == 0:
            k += 1
        begin += 1
    end += 1
print(end-begin)
    
        
