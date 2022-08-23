for i in range(100):
 print(i)


list = [1, 2, 3, 4]
list.append(5)
print (list)

list = []
list.append("a")
list.append("b")
print(list)

list = ["a", "b", "c", "d"]
print(list[1:-1])
list[0:2] = "z"
print(list)

# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.

def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print (f"{prefix} got: {repr(got)} expected: {repr(expected)}")

def match_ends(words):
    count = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            count = count + 1
    return count 


test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
    x_list = []
    rest_list = []
    for element in words:
        if element[0] == 'x':
            x_list.append(element) 
        else:
         rest_list.append(element)
    x_list.sort()
    rest_list.sort()
    return x_list + rest_list

test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
       ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
       ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
       ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])


# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
def sort_last(tuples):
    def f(x):
        return x[1]
    tuples.sort(key=f)
    # tuples.sort(key= lambda x : x[1])
    return tuples

test(sort_last([(1, 3), (3, 2), (2, 1)]),
       [(2, 1), (3, 2), (1, 3)])
test(sort_last([(2, 3), (1, 2), (3, 1)]),
       [(3, 1), (1, 2), (2, 3)])
test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
       [(2, 2), (1, 3), (3, 4, 5), (1, 7)])
