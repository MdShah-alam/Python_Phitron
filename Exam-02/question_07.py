
# class Set:
#     def fun1(self,s1):
#         return self.fun2([],sorted(s1))
#     def fun2(self,curr, s1):
#         if s1:
#             return self.fun2(curr,s1[1:])+self.fun2(curr+[s1[0]],s1[1:])
#         return curr
# set=[4, 5, 6]
# print(Set().fun1(set))
 
class sub:  
    def f1(self, s1):  
        return self.f2([], sorted(s1))  
 
    def f2(self, curr, s1):  
        if s1:  
            return self.f2(curr, s1[1:]) + self.f2(curr + [s1[0]], s1[1:])  
        return [curr]  
a=[4, 5, 6]
print(sub().f1(a))