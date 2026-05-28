class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carData = []
        stack = []

        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            carData.append([position[i], time])
        carData = sorted(carData, key=lambda x: x[0], reverse=True)
        
        print(carData)
        for _, t in carData:
            if not stack or t > stack[-1]:
                stack.append(t)
            
        return len(stack)