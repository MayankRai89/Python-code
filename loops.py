# num = int(input("Enter any number you want to print multiplication tabale of: "))
# i = 1
# while i <= 10:
#   print(num*i)
#   i+=1

# num = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# print(len(num))
# while i <= len(num)-1:
#     print(num[i])
#     i+=1

# num = (1,4,9,16,25,36,49,64,81,100)
# n = 36
# i = 0
# while i < len(num):
#     if(num[i] == n):
#      print("Found at indx ", i)
#      break
#     else:
#        print('Finding......')
#     i+=1

#  if  & else
# name = "Mayank rai"
# for char in name:
#     if(char == " "):
#         break

#     print(char)



# range

# set = range(6)
# for i in set:
#     print(i)

# for i in range(10):#range(start, stop)
#     print(i)

# for i in range(1, 10, 2):
#     print(i)

# for i in range(100, 0, -1):
#     print(i)

# n = int(input("Enter any value: "))
# for i in range(1,11):
#     print(n*i)


# Questions

# n = int(input("Enter the range: "))
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print("Total sum is ", sum)

# i = 1
# while i<=n:
#     sum+=i
#     i +=1
# print(sum)


n = int(input("Enter the number you want to calculate the factorial of: "))
fact = 1
i = 1
while i<=n:
    fact*= i
    i+=1
print(fact)
