num=int(input())
def Factorial(num):
    a=num*2
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    return fact
print(Factorial(num))



# a=int(input())
# b=int(input())
# c=int(input())
# def Maximum (a,b,c):
#     if a>b and a>c:
#         print(a)
#     elif b>a and b>c:
#         print(b)
#     elif c>a and c>b:
#         print(c)
# Maximum(a,b,c)



# str1=input()
# index=int(input())
# def IndeX(str1,index):
#     if index>=len(str1):
#         return ("404 ERROR")
#     else:
#         return str1[index-1]
# print(IndeX(str1,index))


# name=input()
# def data(name,age=12):
#     print("Student name is ",name,"and He/She is",age,"years old")
# data(name)



# n=int(input())
# def decimal(n):
#     length=len(str(n))
#     minvalue=10**(length-1)
#     result=n/minvalue
#     return f"{result:.2f}"
# print(decimal(n))