# runtime: 773ms
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1

        return self.fib(n - 1) + self.fib(n - 2)

# runtime: 46ms      
class Solution:
    def fib(self, n: int) -> int:
        f0 = 0
        f1 = 1
        if n == 0 or n == 1:
            return n

        res = 0
        for i in range(n - 1):
            res = f0 + f1
            f0 = f1
            f1 = res
            
        return res      
      
# runtime: 43ms      
class Solution:
    def fib(self, n: int) -> int:
        def fibnum(x, dic):
            if x in [0, 1]:
                return x
            elif x not in dic:
                dic[x] = fibnum(x - 1, dic) + fibnum(x - 2, dic)
            
            return dic[x]
            
        mapping = {}
        return fibnum(n, mapping)      
