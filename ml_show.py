from random import randint
from PIL import Image
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
x = Image.new("RGB",(20,20),"white")
l = []
data = ((5,2),(4,5),(6,3),(7,9))
m,n = go(array=data)
y = lambda x: m*x+n
for i in range(10):
        if y(i) < 0: continue
        l.append((i,round(y(i))))
for t in l:
        print(t)
        x.putpixel(t,(0,0,0))
for t in data:
        x.putpixel(t,(255,0,0))
