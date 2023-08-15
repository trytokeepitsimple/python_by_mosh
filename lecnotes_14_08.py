#defining a function

# use def name of function paranthesis :


#function defination
# def greet_user():
#     print("Hi There")
#
# #function calling
# greet_user()


#function_with_parameter

# def user_greetings(name):
#     print(f"Welcome {name}")
#     #we can user { } only with formatted string
#
# user_greetings("Devesh")



#argument is the value that we supply to a function
#in above example user_greetings("Devesh")- devesh is a an argument
#user_greeting(name ) - here name is the parameter - holder for values




#postions in argument do matter

# def user_greetings(first_name,last_name):
#     print(f"Welcome {first_name} {last_name}")
#     #we can user { } only with formatted string
#
# user_greetings("shukla" , "devesh")


#that is why keyword argument is helpfull
# once they are used we dont need to have thing in a particular order


def user_greetings(first_name,last_name):
    print(f"Welcome {first_name} {last_name}")
    #we can user { } only with formatted string

user_greetings(last_name="shukla" ,first_name="devesh")


