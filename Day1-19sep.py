
#1 WAP to remove duplicates
# name = "akriti"
# #       012345
# newname = ""   #akrit
# for i in name: #i=0,1,2,3,4,5
#     if i not in newname:
#         newname += i  # add the character i to the end of it
# print(newname)

#2 to accept 3 paper marks like M1 , M2, M3 AND CAL total, percentage and check if user is passed in all subject 
# so print pass else print fail and check if % is greater than 65 and user is having one project so print he/she eligible for placement drive else print noe .
# m1 = int(input("Enter marks of M1: "))
# m2 = int(input("Enter marks of M2: "))
# m3 = int(input("Enter marks of M3: "))
# total = m1 + m2 + m3
# percentage = (total / 300) * 100
# print("Total : ", total)
# print("Percentage: ", percentage)
# if m1 >= 40 and m2 >= 40 and m3 >= 40:
#         print("Pass")
# else:
#         print("Fail")


#3 
# a = [1,2,3,4,5,6,7,8,9]
# a[::2] = [10,20,30,40,50,60]
# print(a)

#4
# a = [1,2,3,4,5]
# print(a[3:0:-1])  # 0 means it will stop at index 1 and -1 means it will print in reverse order so output will be [4,3,2]


#5 
# def func(value , values):
#         var = 1
#         values[0] = 44
# t = 3
# v = [1,2,3]
# func(t,v)
# print(t, v[0])

#6
# arr = [[1,2,3,4],    
#        [4,5,6,7],
#        [8,9,10,11],
#        [12,13,14,15]]
# for i in range(0, 4):   #here i is outer loop toh row pe focus hoga ; if j in range hota toh column pe hota
#         print(arr[i].pop())


#7 
# def f(i, values = []):
#         values.append(i)
#         print(values) 
# f(1)  # callinf func
# f(2)
# f(3)

#8
# arr = [1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1] = arr[i]
# for i in range(0,6):
#     print(arr[i], end = " ")


#9
# a = {(1,2):1, (2,3):2, (3,4):3}
# print(a[(1,2)])  # (1,2) is a tuple and it is used as a key in the dictionary.2 is valueof key((1,2))


#10
# a = {'a':1, 'b':2, 'c':3}
# print(a['a','b'])  # a is key and 1 is value of key a


#11
# fruit = {}
# def addone(index):
#         if index in fruit:
#                 fruit[index] += 1
#         else:
#                 fruit[index] = 1
# addone('Apple')
# addone('Banana')
# addone('apple') 
# addone('Apple')
# print(len(fruit))  # 3 because apple and Apple are different keys in dictionary 


#12
# arr = {}
# arr[1] = 1
# arr['1'] = 2
# arr[1] += 1
# print(arr)
# sum = 0
# for k in arr:
#     sum += arr[k]
# print(sum)  # 4 because arr[1] = 2 and arr['1'] = 2


#13
# my_dict = {}  #{1:4, '1':2}
# my_dict[1] = 1
# my_dict['1'] = 2
# my_dict[1.0] = 4
# print(my_dict)
# sum = 0
# for k in my_dict:  #k='1
#     sum += my_dict[k]
# print(sum)  


#14
# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)
# print(my_dict)



#15
# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates))  # 2 because there are 2 keys in crates dictionary


#16
# dict = {'c': 97, 'a': 96, 'b': 98}
# for _ in sorted(dict):
#     print(dict[_])  # a 96 b 98 c 97 because it will sort the keys(a,b,c) in ascending order and print 


#17
# rec = {'name': 'akriti', 'age': 20,}
# r = rec.copy()  # it will create a copy of rec dictionary and store it in r
# print(id(r) ==id(rec))    # it will print False because rec and r are different objects in memory
# print(id(rec))
# print(id(r))  


#18  given an array move all the zeros to the end wwithout changing the order of non zero elements.
# a = [0,1,0,3,12]
# for i in a:
#     if i == 0:
#         a.remove(i)
#         a.append(i)
# print(a)


#19  find second largest number in an array
# a = [7,3,9,2,8]
# a.sort(reverse=True)
# print(a[1])


#20 given an array return an array where each element is the product of all the elements in the array except itself
# a = [1, 2, 3, 4]
# result = []
# for i in range(len(a)):
#     product = 1
#     for j in range(len(a)):
#         if i != j:
#             product = product * a[j]
#     result.append(product)
# print(result)


#21 find the intersection of 3 arrays
# a = [1,2,3]
# b = [2,3,4]
# c = [3,4,5]
# for i in a:
#     if i in b and i in c:
#         print(i)  # 3 because it is present in all three arrays


#22 max consecutive ones in a binary aray
# a = [1,1,0,1,1,1,0,1,1,1,1]
# result = 0
# count = 0
# for i in a:
#     if i == 1:
#         count += 1
#         result = max(result, count)
#     else:
#         count = 0
# print(result)



#23  to accept any single chr and check the entered chr is in upper case lower case or digit or special chr and acc print msg.
# ch = ord(input("Enter a character: "))
# if ch >=654 and ch <=90:
#     print("uppercase")
# elif ch >=97 and ch <=122:
#     print("lowercase")  
# elif ch >=48 and ch <=57:
#     print("digit")
# else:
#     print("special chr") 


#24  i/p = "helpforcode" o/p count of = vowels, count of = consonemts
# ch = input("Enter a string: ")
# vowels = 0
# consonants = 0
# for i in ch:
#     if i in "aeiouAEIOU":
#         vowels += 1
#     elif i.isalpha():  # check if the character is an alphabet
#         consonants += 1 
# print("Count of vowels:", vowels)
# print("Count of consonants:", consonants)


