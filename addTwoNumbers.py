class Solution:
    def addTwoNumbers(self, l1: [int], l2: [int]) -> [int]:
        n = ''
        m = ''
        total_s = ''
        for num in range(len(l1)-1,-1,-1):
          n = n + str(l1[num])

        for num in range(len(l2)-1,-1,-1):
          m = m + str(l1[num])
         
        total = int(n) + int(m)
        total_s = total
        new = []
        for num in str(total_s):
          new.append(int(num))
   
        return new[::-1]
    

r  = Solution().addTwoNumbers([2,3,4],[1,2,3])

print(r)