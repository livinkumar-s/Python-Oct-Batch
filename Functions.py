# def greet():
#     print("Hi")
#     print("Hello")
#     print("Welcome")
#     print("---------------")

# greet() #Calling
# greet() #Calling


# def add(a,b):
#     print("Hi")
#     print(a)
#     print(b)
#     print(a+b)

# add(3,4)
# add(30,40)

# def sum(a,b,c=10):
#     print(a)
#     print(b)
#     print(c)
#     print(a+b+c)

# sum(b=15,a=-10,c=100)



# def addAll(*a): 
#     print(sum(a))

# addAll(1,2,3,3,5) 

# def mulAll(*nums): #2,3,4
#     ans=1 #24
#     for i in nums:
#         ans=ans*i
#     print(ans)

# mulAll(3,4,5,6,7)


# def getDetails(**a): 
#     print(a)

# getDetails(name="ken",age=43,gender="male")

# def printSteps():
#     print("Step1")
#     print("Step2")
#     print("Step3")
#     print("Step4")
#     print("Step5")

# a=printSteps() #None
# print(a)


# def mul(a,b):
#     return a*b 

# print(mul(4,mul(9,mul(3,mul(2,3)))))


# def add(a,b):
#     print(a+b) #returns None

# print(add(45,54))


# name() 

# print(56)

# a=input("Enter The number: ") #"Str"
# print(a)

# print()

# a=10

# def hi():
#     print("Hi Leo!")

# a=10  #Global Scoped variable

# def dummy():
#     print(a)
#     def greet():
#         print("Hello")
#         print(a)
#     greet()

# dummy()
# print(a)
# greet()


# age=17

# def inc():
#     global age
#     age+=1 # var age (it is looking for global var)
#     # print(age)

# inc()
# inc()
# inc()
# print(age)

# def grandfather():
#     a=10
#     def father():
#         def child():
#             def grandchild():
#                 nonlocal a
#                 a+=10 #looking for local var a
#             grandchild()
#         child()
#     father()
#     print(a)

# grandfather()


l1=[
    1,
    2,
    3,
    [
        "Four",
        "Five",
        "Six",
        [
            "Seven",
            "Eight",
            "Nine"
        ]
    ]
]

# print(len(l1))
# print(l1[4])
# print(l1[-1][-1][-1][-1])

# person={
#     "name":"Leo",
#     "age":23,
#     "role":"FSD",
#     "isMarried":True,
#     "favFoods":["curd","chicken"],
#     "age":56
# }

# print(person["favFoods"][1])