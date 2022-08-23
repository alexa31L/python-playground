from hashlib import shake_128


def donuts(count):
  # +++your code here+++
  if count < 10:
    return f"Number of donuts: {count}"
  else: 
    return "Number of donuts: many"



# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
def both_ends(s):
    if len(s) <= 1:
        return ""
    first_two = s[:2]
    print(first_two)
    last_two = s[-2:]
    print(last_two)

def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print (f"{prefix} got: {repr(got)} expected: {repr(expected)}")

  # C. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.
def fix_start(s):
    start = s[0]
    rest = s[1:]
    rest = rest.replace(start, '*')
    return start + rest



#   # Each line calls donuts, compares its result to the expected for that call.
# test(donuts(4), 'Number of donuts: 4')
# test(donuts(9), 'Number of donuts: 9')
# test(donuts(10), 'Number of donuts: many')

# test(both_ends('spring'), 'spng')
# test(both_ends('Hello'), 'Helo')
# test(both_ends('a'), '')
# test(both_ends('xyz'), 'xyyz')

#test(fix_start('babble'), 'ba**le')
#test(fix_start('aardvark'), 'a*rdv*rk')
#test(fix_start('google'), 'goo*le')
#test(fix_start('donut'), 'donut') 

test(mix_up('mix', 'pod'), 'pox mid')
test(mix_up('dog', 'dinner'), 'dig donner')
test(mix_up('gnash', 'sport'), 'spash gnort')
test(mix_up('pezzy', 'firm'), 'fizzy perm')

# D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.

def mix_up(a, b):
  a_swapped = b[:2] + a[2:]
  b_swapped = a[:2] + b[2:]
  return a_swapped + ' ' + b_swapped
 

