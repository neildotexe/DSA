class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = 0 
        n = start ^ goal 
        while n:
            res += n & 1
            n = n >> 1
        
        return res

class Solution:
  def minBitFlips(self, start: int, goal: int) -> int:
      res = 0 
      n = start ^ goal 
      # Brian Kernighan's Algorithm
          # 1 1 0 0 - 1 = 1 0 1 1
          # 1 0 1 1 & 1 1 0 0(original number) = 1 0 0 0
      while n:
        n = n & (n - 1)
        res += 1
      return res
