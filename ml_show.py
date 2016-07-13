from random import randint
from matplotlib import pyplot as pp
def getMed(arr):
        i,j = 0,0
        while i < len(arr):
                while j < len(arr):
                        if i == j:
                                j += 1
                                pass
                        if arr[i][0] == arr[j][0]:
                                arr.append((arr[i][0],(arr[i][1]+arr[j][1])/2))
                                del arr[j]
                                del arr[i]
                                
                        
                        j += 1
                
                i += 1
        return arr
def go(i=10,**kwargs):
    array = kwargs.get('array',[False])
    if not array[0]:
            del array[0]
            for t in range(kwargs.get('x',4)):
                array.append((randint(0,i),randint(0,i)))
                
    dets = []
    bs = []

    
    array = getMed(array)
    for point in array:
        for point2 in array:
            if point != point2:
                #(point[0] != point2[0]),'Bad numbers....'
                if point[0] == point2[0]:
                        array = getMed(array)
                        continue
                dets.append((point[1]-point2[1])/(point[0]-point2[0]))
                bs.append(point[1]-(dets[-1]*point[0]))
    
    return sum(dets)/len(dets),sum(bs)/len(bs)
def k(x,m,n,data):
	p = lambda i: m*i + n
	pp.axis((0,20,0,20))
	a,y =[],[]
	for i in data: a.append(i[0]),y.append(i[1])
	pp.plot(a,y,'bo')
	pp.plot(x,p(x),'k')
	pp.show()

if __name__ == "__main__":
        import numpy as _
        x = _.arange(0,10,0.01)
        data = ((1,2),(5,4),(8,5))
        m,n = go(array=data)
        k(x,m,n,data)

