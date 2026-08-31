class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        
        stack = list()
        ret_list = [0] * len(temperatures)

        for i in range(len(temperatures)):

            while stack and (temperatures[i] > temperatures[stack[-1]]):

                index = stack.pop()
                ret_list[index] = i - index

            stack.append(i)
        
        return ret_list


