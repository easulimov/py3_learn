types_of_people = 10
# declare a variable of string type that include an integer variable
x = f"There are {types_of_people} types of people"

# declare string variables
interpret = "Python"
do_not = "No"

# declare a variable of string type that includes two integer variables
y = f"Those who understand {interpret} and those who {do_not}"


# display x and y
print(x)
print(y)

# display formatted string with included variables x and y
print(f"I said: {x}")
print(f"And I said more: {y}")


# declare a bool variable
hilarious = True

# curly braces {} must be used for variable substitution
joke_evaluation = "Isn't it funny?!.. {}"

# Using a formatted string variable with method format()
print(joke_evaluation.format(hilarious))

# declare string variables
w = "This is part of the line on the left"
e = " and this is on the right"

# concatenate and display string variables with w and e
print(w + e)