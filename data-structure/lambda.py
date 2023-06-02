from functools import reduce

# lambda function

# filter
val = [0, 1, 2, 1, 4, 7, 8, 14, 13, 19, 31, 50]
fil_1 = list(filter(lambda x: x % 2 > 0, val))
fil_2 = list(filter(lambda x: 2**x > 1024, fil_1))

print(fil_1)  # output:[1, 1, 7, 13, 19, 31]
print(fil_2)  # output:[13, 19, 31]


# reduce
val=[1,1,2,92,20,19,31,100,14]
red_1=reduce(lambda x,y: x if x>y else y, val)
print(red_1) #output:100
#利用前兩項進行運算的結果，再跟第三項運算，直到每個元素都用完
#operation:
#val=[1,1,2,92,20,19,31,100,14] -> val=[1,2,92,20,19,31,100,14] 
#-> val=[2,92,20,19,31,100,14] -> val=[92,20,19,31,100,14] ......
#-> val=[92,100,14] -> val=[100,14] -> val=[100]

red_2=reduce(lambda i,j: i*j, range(1,7))
print(fil_2) #output:720 #this method realizes factorial!
#operation:(((((1*2)*3)*4)*5)*6)

# map
base=[2,3,2,6,3,1,3]
w=[4,1,5,2,4,7,3]

mapping_1=map(lambda x: 3*x+2, base)
print(list(mapping_1)) 
#output:[8, 11, 8, 20, 11, 5, 11]

mapping_2=map(lambda x,y: x+y, base, w)
print(list(mapping_2)) 
#output:[6, 4, 7, 8, 7, 8, 6]


# sorted()內建方法利用關鍵字參數key來指定排序的依據，透過Lambda函式就可以自訂要排序的標的。範例中使用car參數來接收串列(List)中的元素，接著回傳元組(Tuple)的第二個元素(也就是價格)，來進行排序。
cars = [
  ("mazda", 2000),
  ("toyota", 3000),
  ("honda", 4000),
]

print(sorted(cars, key=lambda car: car[1]))

d = {'age': 18, 'name': 'eddie'}

if (name := d.get('name')) is not None:
    print(name)  # 輸出：eddie
