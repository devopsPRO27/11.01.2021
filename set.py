s1={1,2,3,4,5,6,7,89,10,10,5,3,21,1}
'''lsit=[,,,,,]
fun()
dic{k:v,:,}
set{,,,,,}'''
'''print(s1)
s2=list(reversed(list(s1)))
print(s2)
s1.add(9)
print(s1)
s1.add(9)
print(s1)'''
'''list=[100,50,78,100,78,100,50,90,78,100,78]
s2=set(list)
print(s2)'''

dic1={1:'o',2:'t',3:'t',4:'f',5:'f',6:'s',7:'s',8:'e',9:'n'}
repeatDict={}
listOfValues=list(dic1.values())
print(listOfValues)
set1=set(listOfValues)
print(set1)

for x in set1:
    print(f'{x} : {listOfValues.count(x)} times')
    repeatDict[x]=listOfValues.count(x)

print(repeatDict)
