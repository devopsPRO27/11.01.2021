'''dict1={'TEL AVIV':200000 ,'KFAR YONA':20000,\
       'LONDON':3000000 ,'BERLIN':50000000}
#city=input("please \n enter your city\n")
#print(f'{city} population is: {dict1.get(city.upper())}')
#print(dict1[city.upper()])
json={"firstName": "John","lastName": "Smith","isAlive": True}
print(json.get("lastName"))'''

#dictionary
myDict={1:'moshe',2:'erez',3:'dana'}
print(myDict)
def doesKeyExist(d,k):
       '''
       checks if key in dictionary
       :param d: dictionary
       :param k: key
       :return: True f exist
       '''
       if k in d.keys():
              return True
       else:
              return False
def tryAddValue(d,k,v):
       '''
       add [key:value] to dictionary if k does not exist in dictionary
       :param d: dictionary
       :param k: key
       :param v: value
       :return: True if k:v was added to the d
       '''
       if doesKeyExist(d,k)==False:
              d[k]=v #myDict[19]='Dan'
              return True
       else:
              return False

def printDictionary(d):
       '''
       this func will print the dictionary in new format
       :param d: dictionary
       :return: None
       '''
       for k,v in d.items():
              print(f'the value {v} stored by the {k} key')

'''if doesKeyExist(myDIct,3)==False:
       myDict[3]='anat'''
if tryAddValue(myDict,19,'Dan')==True:
       print('item added !!!')
else:
       print('this key is taken')

print(myDict)
printDictionary(myDict)
print(myDict.items())
print(myDict.values())
print(myDict.keys())

















