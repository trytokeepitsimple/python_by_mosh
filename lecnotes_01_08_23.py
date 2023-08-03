#logical operators - and , or , not

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    user_number = int(input("Guess "))
    guess_count += 1
    if (user_number==secret_number):
        print("You Win")
        break
else:
    print("Sorry, You Failed")


#else at while level
#In Python, a while loop may have an optional else block.

# Here, the else part is executed after the condition of the loop evaluates to False
#
# counter = 0
#
# while counter < 3:
#     print('Inside loop')
#     counter = counter + 1
# else:
#     print('Inside else')
#
#     Note: The else block will not execute if the while loop is terminated by a break statement.
