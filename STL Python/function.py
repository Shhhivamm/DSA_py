def total(*nums):
    return sum(nums)
print(total(1,2,3,4,5,6,7,8,9))

#this fucntion return key value pairs
def dis_info(**info):
    for key,value in info.items():
        print(key,value)
dis_info(name= "shivam", age= 22, city="ismailabad")

#this function return multiple arguments
def calc(a,b):
    return a+b, a*b
sum_val, prod_val = calc(4,6)
print(sum_val, prod_val)

