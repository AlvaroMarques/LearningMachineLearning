import random

class Chromossome:
    def __init__(self,code=''):
        self.code = code
        self.cost = 0
    def randomize(self,l):
        string = ''
        while l:
            l -= 1
            string += chr(random.randint(0,127))
        self.code = string
    def Mutate(self):
        pos = random.randint(0,len(self.code))
        if pos == 0:
            self.code = chr(random.randint(0,127))+self.code[1:]
            return self.code
        if pos == len(self.code):
            self.code = self.code[:-1]+chr(random.randint(0,127))
            return self.code
        else:
            self.code =  self.code[:pos]+chr(random.randint(0,127))+self.code[pos+1:]
            return self.code
    def getCost(self,y:str)->int:
        self.cost = sum(abs(ord(self.code[i])-ord(y[i])) for i in range(len(self.code)))
        return self.cost
    def Match(self,other,p):
        halfString = int(len(self.code)/2)
        a=  Chromossome(self.code[:halfString]+other.code[halfString:]), Chromossome(other.code[:halfString]+self.code[halfString:])
        b = []
        for i in a:
            if not random.random()>p:
                i.Mutate()
        return a
class Population:
    def __init__(self,str_goal,genSize,p=0.1):
        self.genSize = genSize
        self.str = str_goal
        self.gen = 0
        self.p = p
        self.pop = []
        self.notYet = True
        for i in range(genSize):
            j = Chromossome()
            j.randomize(len(str_goal))
            self.pop.append(j)
    def delShitChromossomes(self):
        return list(sorted(self.pop,key=lambda x: x.getCost(self.str)))[:self.genSize]
    def goal(self):
        while self.notYet:
            self.notYet = False if any(i.getCost(self.str) == 0 for i in self.pop) else True
            matched = []
            for i in self.pop:
                for j in self.pop:
                    print(j.code)
                    for x in i.Match(j,self.p): matched.append(x)
                    
            for i in matched: self.pop.append(i)
            self.gen += 1
            self.pop = self.delShitChromossomes()
        print(self.pop[0].code)        
            

x = Population('hello world hello bitches',10)
x.goal()
