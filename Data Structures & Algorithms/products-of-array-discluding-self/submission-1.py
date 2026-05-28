class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        prefix = []
        for i in range(len(nums)):
            product *= nums[i]
            prefix.append(product)
        
        product = 1
        postfix = [0 for i in range(len(nums))]
        for i in range(len(nums)-1, -1, -1):
            product *= nums[i]
            postfix[i] = product

        output = []
        for i in range(len(nums)):
            product = 1
            if i != 0:
                product *= prefix[i-1]
            
            if i != len(nums) - 1:
                product *= postfix[i+1]
            
            output.append(product)
        
        return output

