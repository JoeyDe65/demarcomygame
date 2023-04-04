# built in python function /// \\\
print("Hello world")

# var = 5
# assign the value 5 (which is an integer) to the label x
x = 5
# assign the value "Fred" (which is a string) to the label my_name
# quotes mean string; strings mean letters but not just
my_name = "Joey"
my_age = "47"
# assign integer to her age...
her_age = 43
player_hitpoints = 100
playing = True
# reassigning x with a string value of awesome
x = "awesome"

#scope of x is inside the function only when assigned inside the function
def myfunc(lang, adj):
    print (lang + " is " + adj)

    print ("Python is " + x) 

# call the function myfunc
myfunc("Spanish", "super!")
myfunc("Phython", "radical!")
myfunc("Bellarmine", "wonderful!")

print(x)

#runs a loop until it breaks or until playing == False
while playing:
    print("ooooooopppppsss")
    break

def check_the_type(x):
    return "The data type of the thing is", type(x)

    print(check_the_type(555))
    print(check_the_type("duder"))
    print(check_the_type(True))
# this will error because you are trying to concatenate two different data types
# specifically a string valur and an integer value
# print(my_age + her_age)
