# f = open("read.txt","r")
# data = f.read()
# print(data) 
# print(type(data))



# f = open("read.txt","r")
# line1 = f.readline()
# print(line1)
# line2 = f.readline()
# print(line2)



# f = open("read.txt","w")
# f.write("this is the new line")


# f = open("read.txt","a")
# f.write(" from where i have to start to write")

# f = open("samle.txt","w")
# f.write("this is the new text file")



# f = open("samle.txt","a")
# f.write("i have created to test it")


# f = open("read.txt","r+")
# f.write("abc")
# print(f.read())



# f = open("read.txt","w+")
# # f.write("abc")
# print(f.read())


# with open("read.txt","r") as f:
#     data = f.read()
#     print(data)

#     with open("read.txt","w") as f:
#         f.write ("new data")
# f.close()


#  delete a file
# import os
# os.remove("demo.txt")  


# questions

# with open("practice.txt","w") as f:
#    f.write("Hi everyone \n we are learning file I/O\n")
#    f.write(" using python.\nI like programming in python.")


# with open("practice.txt","r") as f:
#     data = f.read()
# # print(data)

# new_data = data.replace("python","java")
# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data) 


# def check_for_word():
#    word = "learning"
#    with open("practice.txt","r") as f:
#         data = f.read()
#         if(data.find(word) != -1):
#           print("Found")
#         else:
#           print("Not found")
     
# check_for_word()

# def check_for_line():
#     word = "programming"
#     data = True
#     line_no = 1
#     with open("practice.txt","r") as f:
#        while data:
#           data = f.readline()
#           if(word in data):
#                print(line_no)
#           line_no += 1


#     return -1


# check_for_line()

# with open("practice.txt", "w") as f:
#     f.write("1,2,3,4,5,6,7,8,9,10")
# with open("practice.txt", "r") as f:
#     data = f.read()
#     print(data)

#     num= ""
#     for i in range(len(data)):
#         if(data[i] == ","):
#             print(int(num))
#             num = " "
#         else:
            # num += data[i]


#  count number of even no in the list
count = 0
with open("practice.txt","r") as f:
    data = f.read()

    num = data.split(",")
    for val in num:
        if(int(val) %2 == 0):
            count += 1
print(count)
