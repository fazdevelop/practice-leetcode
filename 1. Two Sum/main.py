# One-pass Hash table solution

def twoSum(nums, target):
    hash_table = {}
    n = len(nums)

    for i in range(n):
        complement = target - nums[i]
        if complement in hash_table:
            return [hash_table[complement], i]
        hash_table[nums[i]] = i

    return [] # No solution found

# test
num_list = [3,4,6,2,14,17,10,21]
num_target = 19
resultado = twoSum(num_list, num_target)
print(resultado)