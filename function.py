# def multiplication(a,b):
#     return a*b

# mul = multiplication(3,5)
# print(mul)

# #  functon

# def calculate(a, b):
#     sum = a+b
#     print(sum)
#     return sum

# calculate(4,7)



# Questions

# num = [1,2,3,4,5]
# cities = ["Delhi", "Mumbai", "pune","chennai"]

# # def listfun(num):
# #     print(len(num))    
# # listfun(num)



# def print_list(list):
#   for item in list:
#     print(item, end=" ")
# print(cities)




# def calc_fact(n):
#   fact = 1
#   for i in range(1,n+1):
#       fact*=i
#   print(fact)

# calc_fact(5)


# def converter(usd_val):
#   inr_val = usd_val*83
#   print(usd_val,"USD = ",inr_val,"INR")

# converter(73)



# def even_odd(n):
#   if(n%2==0):
#     print("EVEN")
#   else:
#     print("ODD") 

# even_odd( 6)


#  recursion
# def show(n):
#   if(n == 0):
#        return
#   print(n)
#   show(n-1)
   

# show(5) 


# factorial
# def fact(n):
#   if(n ==1 or n == 0):
#     return 1
#   else:
#     return fact(n-1)*n
# print(fact(4))


# def sum(n):
#   if(n==0):
#     return 0
#   return sum(n-1)+n

# total = sum(5)
# print(total)



def print_list(list, index):
  if(index == len(list)):
     return
  print(list[index])
  print_list(list, index+1)

fuits = ["MANGO","GUAVA","APPLE","LICHI"]
print_list(fuits,0)