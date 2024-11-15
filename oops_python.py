# class student:
     
#     # # default construcrtors
#     #  def __init__(self):
#     #     pass

#     # parameterized constructors
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in Database...")


# s1 = student("karan", 97,)
# print(s1.name, s1.marks) 



# class car:
#     colour = "blue"
#     brand = "mahindra"

# cl = car()
# print(cl.colour) 
# print(cl.brand) 


# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum+=val
#         print("hi", self.name,"your avg score is:",sum/3)


#     @staticmethod
#     def hello():
#         print("hello")

        
# s1 = student("tony",[98, 99, 97])
# s1.get_avg()
# s1.hello()


class  account:
    def __init__(self,bal,acc):
       self.balance = bal
       self.account_no = acc

    # debit method
    def debit(self, amount):
        self.balance -= amount
        print("RS",amount ,"was debited")
        print("Total balance is: ",self.get_balance)

    def credit(self, amount):
        self.balance += amount
        print("RS", amount," is credited form your account")
        print("Total balance amount is : ",self.get_balance)

    def get_balance(self):
        return self.balance 
    
acc1 = account(10000,12345)
acc1.debit(100)
acc1.credit(500)
acc1.credit(5000)