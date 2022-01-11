dict1={'TEL AVIV':200000 ,'KFAR YONA':20000,\
       'LONDON':3000000 ,'BERLIN':50000000}
city=input("please \n enter your city\n")
פrint(f'{city} population is: {dict1.get(city.upper())}')
print(dict1[city.upper()])
json={"firstName": "John","lastName": "Smith","isAlive": True}
print(json.get("lastName"))
