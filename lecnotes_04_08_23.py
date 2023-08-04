
#For Loop

# for item in "string'

# item here is known as loop variable and in each iteration this holds a new value of list.

# for item in 'python':
#     print(item)
#
# for item in ['a', 'b', 'c','d']:
#     print(item)







# We can user range function to generate numbers for iteration

# for item in range(10):
#     print(item)
#
# this will print 10 numbers which starts from here by default , given number is excluded







# for item in range(5, 10):
#     print(item)
#

# start index and last index - which will be excluded






# for item in range (5 , 10 , 2):
#     print(item)
# we can optionally pass third argument in range function which is used to alter the default increment of one



# Total value of cart

# prices = [100, 200 , 300, 700 , 410 ]
# cart_value = 0
#
# for item in range(len(prices)):
#     cart_value = cart_value + prices[item]
#
# print(cart_value)










# NESTED LOOPS

# like co-ordinates - > ( x , y )
# ( 0 , 0 ) , ( 0 , 1 ) , ( 0 , 2 ) , ( 1, 0 ) , ( 1 , 1 ) , ( 1 , 2 ) etc


# for x in range(4):
#     for y in range(5):
#         print(f'The given co-ordinates are {x} , {y}')






numbers = [5 , 2 , 5 , 2 , 2]

for item in numbers:
    print(" * " * item)