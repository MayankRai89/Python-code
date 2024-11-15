# dictonary
# info={
# "name" : "Mayank Rai",
# "cgpa" : " 7.15",
# "marks" : [1,2,3,4,5],
# "age" : 20,
# "is adult": True,
# }
# print(info) 
# print(info["name"])
# info["name"] = "manish"
# info["surname"] = " tiwari"
# print(info)
# print(type(info))


# student= {
#     "name" : "Mayank rai",
#     "subject" : {
#         "physics" : 56,
#         "maths" : 78,
#         "chemestry" : 80,
#     }
# }
# print(student)
# print(student["subject"])
# print(list(student.keys()))
# print(student.items())
# new_item = { "name" : "varun Rai", "age": 17}
# student.update(new_item)
# print(student)


# sets

# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add("me")
# # collection.remove(3)
# print(collection)
# set1 = {1,2,3,4}
# set2 = {2,3,5,6}
# print(set1.union(set2))
# print(set1.intersection(set2))




#   QUESTIONS

# dictionary = {
#     "cat" : "a small animal",
#     "table" : ["a piece of furniture", " list of facts and figures"]

# }
# print(dictionary)


# subject = {"python","java","c++","python","javascrpt", "java","python","java","c++","c"}
# print(subject)
# print(len(subject))

marks={}

x= int(input("enter maths: "))
marks.update({"maths": x})

x= int(input("enter physics: "))
marks.update({"physics": x})

x= int(input("enter chemestry: "))
marks.update({"chemestry": x})
print(marks)


