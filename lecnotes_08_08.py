#Tuples

# Tuples are like list are structure in python , we can store list of item in tuples

# But in tuples , we can not add or remove items - Tuples are immutables

# lists are stored in [] - square bracket but tuples get stored in () - paranthesis

# numbers= (1,2,3)
# print(numbers[2])






#unpacking

numbers = ( 1 , 2 , 3 )

# x = numbers[0]
# y=numbers[1]
# z= numbers[2]



# to achieve similar thing in python as above we can use unpacking

# x  , y ,z = numbers
# print(x, y  )


# unpacking is not limited to tuples only we can this in list also








# Dictionary

# Dictionary is used when we have to store multiple information of a single entity in key-value pair form

# { } - curly braces are used to create a dictionary

# each key should be unique

# value could be anything - string , number , boolean , list etc

customer = {
    "name" : "John Smith",
    "email": "ab@gmail.com",
    "is_verified": True,
    "age": 30
}

# print(customer["name"])
# print(customer.get("age"))

# we can use get to aceess values from dictionries

# if somekey is missing or not present then we can add this using get after checking presense

#None will be returned by a get if key is missing

# None is an object which indicate absense of a value
#
# print(customer.get("birthday"))
# print(customer.get("birthday","24 dec 1996"))
# print(customer.get("birthday"))



#split() - this accepts a seperator and returns a list


# str = "devesh"
# w=str.split(" ")
# print(w)




#number to string mapping

# numbers = input("Number > ")
#
# digit_mapping = {
#     "1":"one",
#     "2":"two",
#     "3":"three",
#     "4":"four"
# }
# outcome=""
# for number in numbers:
#     outcome=outcome+digit_mapping.get(number,"!") + " "

# print(outcome)

#emoji - ctrl + alt + ;


# Words to emoji converter

user_input = input("Please add you input from here")
user_input_list = user_input.split(" ")

emoji_coverstion = {
    "happy":"😊",
    "sad":"😌"
}
outcome = ""
for word in user_input_list :
    outcome=outcome+emoji_coverstion.get(word,word)+ " "

print(outcome)