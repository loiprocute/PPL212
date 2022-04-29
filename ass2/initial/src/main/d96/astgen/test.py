from functools import reduce
def getSubsum(a):
    a=str(a)
    list1=[]
    list1[:0]=a
    list=[int(i) for i in list1]
    return reduce(lambda x,y: x +[x[-1]+y],list[1:],[list[0]])

print(getSubsum(123))
	