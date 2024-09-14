def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        for n in arr:
            prefix.append(prefix[-1] ^ n)
            # prefix[-1] gives us the last entry in the array 
            # same as prefix[len(prefix)-1]

        res = []
        for left, right in queries:
            res.append(prefix[right+1] ^ prefix[left])
            # a ^ b ^ a = b
        
        return res
