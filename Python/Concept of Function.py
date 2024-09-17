# Why function is necessary 
# 1. more readable
# 2. more efficient
# 3. more maintainable
# 4. reusable
# 5. extensible


# function
def welcome(msg)->str:
    return msg

msg = welcome("Hello")
print( msg + " Let's learn python")


# function to add even and odd number
def even_odd_sum(lst):

    even_sum=0
    odd_sum=0
    for i in lst:
        if i%2==0:
            even_sum+=i
        else:
            odd_sum+=i
    return even_sum,odd_sum

sum1,sum2=even_odd_sum([1,2,3,45,6,677,7,8,8,54,4,3,5,6])
print("The sum of even numbers {} & the sum of odd numbers {}".format(sum1,sum2))

# concept of positional and keyword type arguments
def hello(*args,**kwargs):
    print(args)
    print(kwargs)

# here we see the positional and keyword argument
hello("Krish","Naik",age=32,dob=1989)
print("----------")

hello("Krish","NAik","1","2","1989",age=10,dob=1990)
print("----------")

# lets pass a list as positional and dict as keyword argument
lst=list(('Krish', 'Naik'))
dict_val={'age': 32, 'dob': 1989}

hello(*lst,**dict_val)

