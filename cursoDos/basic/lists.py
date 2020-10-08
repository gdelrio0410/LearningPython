myList = [1,2,3,4,5,6]
myList2 = ["a","b","c","d"]
myList3 = [1,"b",2,"d"]

print(myList[0])
print(myList[0:3])

print(len("hola como estas"))
print(len(myList))
print(len(myList2))

myList4 = [1,2,3]
myList4.append(4)

myList5 = [5,6,7]

myList4.append(myList5)

print(myList4)

myList4.pop()

print(myList4)
myList4.pop(0)

print(myList4)

myFirstItem = myList4.pop(0)

print(myList4)
print(myFirstItem)



myList = [1,2,3,4,5,6]

print(myList)
myList.reverse()
print(myList)
print("***********")
myList = [8,2,3,1,4,7,5,6]
print(myList)
myList.sort()
print(myList)
