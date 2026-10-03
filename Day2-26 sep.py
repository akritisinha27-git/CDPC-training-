
#1 class Student:
#      def __init__(self):
#         print("i am constructor i always called first")
#      def msg(self):
#         print("hellworld")
#  constructor is called automatically when we create object of class. It is called only once.
# obj = Student()     # obj hamesha class ke bahar rehta hai isliye constructor hamesha call hota hai
# print(obj)
# obj.msg()
# obj2 = Student()

#eg: constructor
# class Student:
#      def __init__(self):
#         print("i am constructor i always called first")
#      def msg(self):
#         print("hellworld")
# # constructor is called automatically when we create object of class. It is called only once.
# obj = Student()     # obj hamesha class ke bahar rehta hai isliye constructor hamesha call hota hai
# print(obj)
# obj.msg()
# obj2 = Student()


#2 class HOD:
#    def __init__(self,name,age,rollno):
#       self.name = name
#       self.age = age
#       self.rollno = rollno
#    def show(self):
#       print("name =",self.name)            
#       print("age = "self.age)
#       print("rollno = "self.rollno)
# obj = HOD("Akrit", 20, 101)
# obj.show() 



#3 create class name of student and accept personal info like name, mobile no. , emailed and create method to display the personal info
# class Students:
#     def __init__(self, name, mobileno, email):
#         self.name = name
#         self.mobileno = mobileno
#         self.email = email
#     def info(self):
#         print("name =", self.name)
#         print("mobileno =", self.mobileno)
#         print("email =", self.email)
# obj = Students("Akriti", "9876543210", "akriti@gmail.com")
# obj.info()  




#4 declaring instance variable inside a constructor by using self variable
# class Student:
#     def __init__(self):  # constructor
#         self.s_name = "prashant"
#         self.l_name = "jha"       # instance variable
#         self.s_rollno = 101
#         self.s_branch = "CS"
#         self.s_mb = 0000000000
# obj = Student()
# print(obj.__dict__)   

 
#5 IMP 
# import sys
# class Stack:
 # def __init__(self):
 #     self.stackSize = 5
 #     self.myStack = []       
        
#     def isFull(self):
#         if len(self.myStack) == self.stackSize:
#             return True
#         else:
#             return False
        
#     def isEmpty(self):
#         if self.myStack == []:
#            return True
#         else:
#             return False
    
#     def push(self, data):
#         if self.isFull():
#             print("stack is full")
#         else:
#             self.myStack.append(data)# append se data stack me jayega 
#             print("Element pushed") 
            
#     def pop(self):
#         if self.isEmpty():
#             print("stack is empty")
#         else:
#             print(self.myStack.pop())
            
#     def peek(self):
#         if self.isEmpty():
#             print("stack is empty")
#         else:
#             print("Top element =",self.myStack[-1])  # jo bhi top element hoga usko display karega                       
    
#     def deleteStack(self):
#         self.myStack = []
#         print("Delete stack done")
    
#     def displayStack(self):
#         if self.isEmpty():
#             print("stack is empty")
#         else:
#             print(self.myStack)

# size = int(input("enter the size of stack:")) # execution will start  
# obj = Stack(size)     
# while True:      
#     print("1. Push Operation:")
#     print("2. Pop Operation:")
#     print("3. Peek Operation:")
#     print("4. isEmpty Operation:")
#     print("5. isFull Operation:")
#     print("6. Delete Operation:")
#     print("7. Display stack:")
#     print("8. Exit")
#     choice = int(input(" enter your choice:"))
#     if choice == 1:
#         value = int(input("enter the value to push in stack:"))  # push operation
#         obj.push(value)
#     elif choice == 2:
#         obj.pop() 
#     elif choice == 3:
#         obj.peek()
#     elif choice == 4:
#         print(obj.isEmpty())
#     elif choice == 5:
#         print(obj.isFull())
#     elif choice == 6:
#         obj.deleteStack()
#     elif choice == 7:
#         obj.displayStack()
#     else:
#         sys.exit()
   


#6 Implement a max stack:(1)Create a Python stack that supports the push,pop,top,and get_max operations in O(1)time.
#(2)Use an additional stack to keep track of the maximum element at any given time.
# class Stack:
#     def __init__(self, size):
#         self.size = size
#         self.mystack = []
#         self.max_stack = []

#     def push(self, data):
#         if self.isFull():
#             print("Stack is full")
#         else:
#             self.mystack.append(data)

#             if len(self.max_stack) == 0:
#                 self.max_stack.append(data)
#             elif data >= self.max_stack[-1]:
#                 self.max_stack.append(data)
#             else:
#                 self.max_stack.append(self.max_stack[-1])

#     def pop(self):
#         if len(self.mystack) == 0:
#             print("Stack is empty")
#         else:
#             self.mystack.pop()
#             self.max_stack.pop()

#     def top(self):
#         if len(self.mystack) == 0:
#             return None
#         return self.mystack[-1]

#     def get_max(self):
#         if len(self.max_stack) == 0:
#             return None
#         return self.max_stack[-1]

#     def isFull(self):
#         return len(self.mystack) == self.size

# obj = Stack(5)
# obj.push(10)
# obj.push(20)
# obj.push(5)
# obj.push(30)
# print("Stack:", obj.mystack)
# print("Top:", obj.top())
# print("Maximum:", obj.get_max())
# obj.pop()
# print("After pop:", obj.mystack)
# print("Maximum:", obj.get_max())



#7 Factorial sol:
# def factorial(num):    #num=1
#     if num <= 1:
#         return 1
#     return num* factorial(num-1)   # recursion call
# print(factorial(4))    # 4*factorial(3),  3* fact(2)  , 2*fact(1),  = 4*3*2*1=24 


#8 
# def power(base, exponent):    #2,4
#     if exponent == 0:         #base condition 4==0
#         return 1
#     return base * power(base, exponent-1)     #recursion
# print(power(2,0))  #1 =2^0
# print(power(2,2))  #4 =2^2
# print(power(2,4))  #16 =2^4
# output= 2*(2,1) 
#2*(2,0)
#1 # 2*2*1=4




#9 reverse sol
# def reverse(strng): 
#     if len(strng) <= 1:
#         return strng
#     return strng[len(strng)-1] + reverse(strng[0:len(strng)-1])  
# print(reverse("python"))