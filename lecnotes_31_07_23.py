# Define string which are of multiple lines

# triple quotes - use triple quotes to write multiple line string

# These quotes either could be a single or double quotes

#Example 1 :

# message = '''
# Hi Customer ,
# Glad to meet you on this
# Thanks ,
# Support Team
# '''
#
# print(message)







# use [] in string to do the various operations in string


#Example 2 :
# course = 'python'
#
# print(course[0]) # access first index value
#
# print(course[-1]) # access last index value
#
# print(course[-2]) # access second last index value







# use [ startIndex : endIndex ] - to access values at indexes
# Value at endIndex will be excluded.

#Example 3 :

#course = 'python'
#
# print(course[0:1]) # will start picking values from first index and exclude values written at endIndex
#
# print(course[0:5])

# if we don't mention endIndex then it will read all values in a string
#print(course[2:])


#similary if we don't mention start index then zero index will be treated as default index value

# course = 'python'
# print(course[:5])


# if we just write [ : ] then whole string will be printed as output

# course = 'python'
# print("Trimmed string - > " + course[:])

# name = "jennifer"
# print(name[1:-1])








#Formatted String

# f''

# user { } to use values of variables

# firstName= "John"
# lastName = "Smith"
# message = f'{firstName} [{lastName}] is a coder'
# print(message)









#String methods

#1 : len() - used to get the length of a strin

# course = "python"
# print(len(course))


# 2 : upper() / lower() - these methods does not affect the original string

# course = 'python'
# print(course.upper())
# print(course)



# 3 : find() - this will return the index of first occurance of character
# if passed character is not matched in given string then -1 will be returned.
# find() -  method is case sensitive
# course = 'POOP'
# print(course.find("O"))
# print(course.find("s"))
# print(course.find("P"))
# print(course.find('p'))



# 4 - replace() - > this will replace the targetted value with the new given value

# replace is also case-sensitive -> if we pass "PYTHON" then nothing will happen
# original string will be returned in this case

# course = 'python'
# print(course)
# #print(course.replace('python','javascript'))
# print(course.replace("PYTHon","OK"))




# 5 - > check existense of character or sequence of characters
# in is used for this purpose - if character or sequence of charcaters are there then True
#will be returned other False

# course = 'python'
# print('python' in course)
# print('p' in course)
# print('P' in course)








#Aritmatic operations - > normal use - >>> + , - , * , /


# / provide us number with decimals
# // provide us integer
# % provide remainder

# print(10/3)
# print(10//3)



# pow - > if we want to do the calculations like 10 to 3 then ** will be used for that purpose

# print(10**3)

#agumented assignment operators
# x = 10
# x = x +3 //13
# we can acheive same thing using this - > x+=3

# x=10
# x+=3
# print(x)




#order of precedence

# parantesis
# expopentiation
# multiplication or divison
# addition or subtraction









# Math functions

# round() - > to get to a round number - nearby integer

# print(round(2.6))

# abs () - is used to get to absolute number  - even if provided number is negative -> result
# will a positive number

# print(abs(-1.4))


# import math library to use complex methods of math


# we just need to write below lines

# import math
# then we can use this math as object to access all defined method
# like math.ceil() , math.floor()  etc


# import math
#
# print(math.floor(2.9))
# print(math.ceil(2.8))










#conditional statement
# using if , else , elif - replacement of else if
# indentation is very important in these cases
# SHIFT+TAB to exit current indentation


# if 10>9:
#     print("wow")

#problem 2 :

# price_house=1000000
# credit='bad'
# if(credit=='good'):
#     print("Down Payment is going to be ->",price_house*.1)
# else:
#     print("Down Payment is going to be - >" , price_house*.2)














