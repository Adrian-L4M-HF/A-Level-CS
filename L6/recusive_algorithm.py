def calcSum(n):
    total = 0
    if n == 1:
        n = 1
    else:
        total = n + calcSum(n-1)
    return total
print(f"{calcSum(5)=}")

def sum_(*nums):
    if len(nums) == 1:
        return nums[0]
    return nums[0] + sum_(*nums[1:])
print(f"{sum_(3,6,9,10,9)=}")            
        

        