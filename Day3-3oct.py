
#1 WOP to cal and returnthe sum of distance bwt the adjecent no. in an array of positive integers.
# def sum_of_distances(arr):
#     total_distance = 0

#     for i in range(len(arr) - 1):
#         total_distance += abs(arr[i] - arr[i + 1])  #abs=it makes the difference positive
#     return total_distance
# print(sum_of_distances([10, 11, 7, 12, 14]))


#2 even no check 
# rollno = [3,5,7,1,11,4,5,2]
# for x in rollno:  # x=0:3,x=1:5, x=2:7
#     if x == 2 or x == 4 or x == 6 or x == 8 or x == 10:
#         print("even no is found",x)
#         break


#3 
# for i in range(1,4):  # outter loop= row
#     for j in range(1,4):   # inner loop= col        
#        print(i, end=" ")    #(i,j) end=" " isse values ek hi line mein print hoti hain, beech mein space aata hai.
#     print()


#4
# n = int(input("enter the value of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i), end=" ")  #
#     print()



#5 pattern to desending order
# n = int(input("enter the value of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(n+1-i, end=" ")  #
#     print()  
            
            
#6
# n = int(input("enter the value of rows: "))
# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print(i, end=" ")  
#     print()           


#7
# name = "prashant*is *a*good*programmer"
# newname = ''
# val = ''
# for i in name :
#     if i != '*':
#         newname += i
#     else:
#         val += i
# print(newname)
# print(str(val+newname))    


#8 print max number from each row
# a = [[100,198,333,323],
#       [122,232,221,111],
#        [223,565,245,764]]
# for row in a:
#     print(max(row))


#9 
# pizza = 100
# burger = 50
# coldrink = 20
# val1 = int(input("enter the no. of pizzas bought:"))
# val2 = int(input("enter the no. of burger bought:"))
# val3 = int(input("enter the no. of coldrink bought:"))
# pizza_total = pizza*val1
# burger_total = burger*val2
# coldrink_total = coldrink*val3
# print('--------------------------------')
# print('bill details:')
# print('total no. of pizza:',pizza_total)
# print('total no. of burger:',burger_total)
# print('total no. of coldrink:',coldrink_total)
# print('total bill amount:',pizza_total + burger_total + coldrink_total)
# print('--------------------------------')



#10 WAP check two arrays are compatible(lenght shoud be same)nor not
# A=[]
# B=[]
# n1 = int(input("enter the size of array:"))
# for i in range(n1):
#     A.append(input())
# n2 = int(input("enter the size of array:"))
# for i in range(n2):
#     B.append(input())
# if len(A) == len(B):
#     print('compatible')
# else:
#     print('not compatible')


#11 arrange the no so that all even no comes first and then odd no.
# n = [3,0,5,6,7,8,9,10,11,12,13,14,15]
# even = []
# odd = []
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         even.append(n[i])
#     else:
#         odd.append(n[i])
# print(even + odd)  #even no. first and then odd no.


#12 
# import sys
# class CRUD:
#     def __init__(self):
#         print("student management system")
#         self.studentID = []
#         self.studentName = []
#         self.studentRollno = []
#         self.studentCity = []
#     def add_student(self):
#         id = input("enter student id:")
#         name = input("enter student name:")
#         rollno = input("enter student rollno:")
#         city = input("enter student city:")
#         self.studentID.append(id)
#         self.studentName.append(name)
#         self.studentRollno.append(rollno)
#         self.studentCity.append(city)
#     def show_student(self):
#         if not self.studentID:
#             print("no student details found")
#             return
#         Id_width = max(len("id"), max((len(str(id)) for id in self.studentID), default=0))
#         Name_width = max(len("name"), max((len(name) for name in self.studentName), default=0))
#         Rollno_width = max(len("rollno"), max((len(str(rollno)) for rollno in self.studentRollno), default=0))
#         City_width = max(len("city"), max((len(city) for city in self.studentCity), default=0))
#         total_width = Id_width + Name_width + Rollno_width + City_width + 10
        
#         print("student details:")
#         print(f"{'id'.ljust(Id_width)} | {'name'.ljust(Name_width)} | {'rollno'.ljust(Rollno_width)} | {'city'.ljust(City_width)}")
#         print("-" * total_width)
#         for i in range(len(self.studentID)):
#             print(f"{self.studentID[i].ljust(Id_width)} | {self.studentName[i].ljust(Name_width)} | {self.studentRollno[i].ljust(Rollno_width)} | {self.studentCity[i].ljust(City_width)}")
#         print("-" * total_width)
            
#     def update_student(self):
#         id = input("enter student id to update:")
#         if id in self.studentID:
#             index = self.studentID.index(id)
#             name = input("enter new student name:")
#             rollno = input("enter new student rollno:")
#             city = input("enter new student city:")
#             self.studentName[index] = name
#             self.studentRollno[index] = rollno
#             self.studentCity[index] = city
#         else:
#             print("student id not found")
#     def delete_student(self):
#         id = input("enter student id to delete:")
#         if id in self.studentID:
#             index = self.studentID.index(id)
#             del self.studentID[index]
#             del self.studentName[index]
#             del self.studentRollno[index]
#             del self.studentCity[index]
#         else:
#             print("student id not found")
#     def start(self):
#         while True:
#             print("1. Add student")
#             print("2. Show student")
#             print("3. Update student")
#             print("4. Delete student")
#             print("5. Exit")
#             choice = input("enter your choice:")
#             if choice == '1':
#                 self.add_student()
#             elif choice == '2':
#                 self.show_student()
#             elif choice == '3':
#                 self.update_student()
#             elif choice == '4':
#                 self.delete_student()
#             elif choice == '5':
#                 sys.exit()
#             else:
#                 print("invalid choice")
                        
# if __name__ == "__main__":
#     obj = CRUD()
#     obj.start()




#QUEUE:is a data structure that stores the First In First Out (FIFO). A queue can be implemented using lists, linked lists, or other data structures.
# import sys

# class Queue:
#     def __init__(self, size):
#         self.queueSize = size
#         self.myQueue = []    #implementing queue using list
#     def isFull(self):
#         if len(self.myQueue) == self.queueSize:
#             return True
#         else:
#             return False
#     def isEmpty(self):
#         if self.myQueue == []:
#             return True
#         else:
#             return False  
#     def enqueue(self, data):
#         if self.isFull():
#             print("Queue is full")
#         else:
#             self.myQueue.append(data)      
#     def dequeue(self):
#         if self.isEmpty():
#             print("Queue is empty")
#         else:
#             print(self.myQueue.pop(0))  #pop(0) removes the first element from the list
#     def peekFrontElement(self):
#         if self.isEmpty():
#             print("Queue is empty")
#         else:
#             print(self.myQueue[0])  #peek() returns the first element of the list without removing it
#     def deleteQueue(self):
#         self.myQueue = []  #deleteQueue() deletes the entire queue permenently
#         print("Entire Queue deleted successfully")    
#     def displayQueue(self):
#         if self.isEmpty():
#             print("Queue is empty")
#         else:
#             print(self.myQueue)  #displayQueue() displays the entire queue
# size = int(input("enter the size of queue:"))
# obj = Queue(size)     #constructor of Queue class is called and size is passed as an argument
# while True:
#     print("1. Enqueue")
#     print("2. Dequeue")
#     print("3. Peek front element")
#     print("4. Check if queue is empty")
#     print("5. Check if queue is full")
#     print("6. Delete entire queue")
#     print("7. Display entire queue")
#     print("8. Exit")
#     ch = int(input("enter your choice:")) 
#     if ch == 1:
#         data = input("enter the element to enqueue:")
#         obj.enqueue(data)
#     elif ch == 2:
#         obj.dequeue()
#     elif ch == 3:
#         obj.peekFrontElement()
#     elif ch == 4:
#         print("Queue is empty:", obj.isEmpty())
#     elif ch == 5:
#         print("Queue is full:", obj.isFull())
#     elif ch == 6:
#         obj.deleteQueue()
#     elif ch == 7:
#         obj.displayQueue()
#     else:
#         sys.exit()
        
        