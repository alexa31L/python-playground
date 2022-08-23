# The len() function
# Function len() returns a number of characters in a string.

sentence = "Operations on strings"
print(len(sentence))

# The .index() function
# It returns the number of the first character occurrence in a string.

hello = "Hello, World!"
print(hello.index("o"))

# The .count() function
# It returns the number of occurrences for a specific character

hello = "Hello, World!"
print(hello.count("o"))

# String cutting (slicing) 
# The operator [ ] can be used to get few characters at the same time from a string

hello = "Hello, World!"
print(hello[7:12])

# String slicing with some charcaters exclusion
# It gets a substring from a string with a skip happening for each second character

hello = "Hello, World!"
print(hello[7:12:2])

# Reverse string
# By using the specific code with an operator [] we can read a string from the end point.

hello = "Hello, World!"
print(hello[::-1])

# The .upper() function
# Return a string in capital letters

hello = "Hello, World!"
print(hello.upper())

# The .lower() function
# Return a string in lowercase

hello = "Hello, World!"
print(hello.lower())

# The .replace() function
# Exchanges all occurrences of the specific character

hello = "Hello, World"
print(hello.replace("l", "R"))
