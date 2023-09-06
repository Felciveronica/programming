class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference=0
    def computeDifference(self):
        for i in range(0,len(self.__elements)):
            for j in range(i,len(self.__elements)):
                x=abs(self.__elements[i]-self.__elements[j])
                if(x>self.maximumDifference):
                    self.maximumDifference=x
        
_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
