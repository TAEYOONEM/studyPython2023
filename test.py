class Statis():
    def __init__(self) -> None:
        self.n = int(input())
        self.m = []
        self.cnt = 0 
        self.max_cnt = 0
        self.ii = 0
        self.mm = []

        for i in range(self.n) :
            self.m .append(int(input()))
        self.m.sort()
    
    def mean(self) : 
        return round(sum(self.m) / self.n)

    def median(self) :
        if self.n % 2 == 0 :
            return (self.m[self.n/2-1] + self.m[self.n/2])/2
        else :
            return self.m[self.n//2]

    def mode(self) :
        if self.n == 1 :
            self.mm.append(self.m[0])
        for i in range(self.n-1) : 
            if self.m[i] == self.m[i+1] :
                self.cnt += 1
            if self.cnt > self.max_cnt :
                self.max_cnt = self.cnt
                self.cnt = 0
                self.mm = []
                self.mm.append(self.m[i])
            if self.cnt == self.max_cnt :
                self.mm.append(self.m[i])
        if len(self.mm) == 1:
            return self.mm[0]
        else :
            return self.mm[1]
    
    def ran(self) :
        return self.m[self.n-1] - self.m[0]

a = Statis()
print(a.mean(),a.median(),a.mode(),a.ran())
