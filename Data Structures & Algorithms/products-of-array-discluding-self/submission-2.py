class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = []
        product = 1
        for i in range(n):
            product *= nums[i]
            prefix.append(product)

        suffix = []
        product = 1
        for i in range(n - 1, -1, -1):
            product *= nums[i]
            suffix.insert(0, product)

        res = []
        for i in range(n):
            product = 1
            if i != 0:
                product *= prefix[i - 1]
            
            if i != n - 1:
                product *= suffix[i + 1]

            res.append(product)
        return res            