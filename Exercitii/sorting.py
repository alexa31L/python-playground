a = [5, 1, 4, 3]
print(sorted(a))
print(a)  

strs = ['ccc', 'aaaa', 'd', 'bb']
print(sorted(strs, key=len))

  ## "key" argument specifying str.lower function to use for sorting
print(sorted(strs, key=str.lower))  ## ['aa', 'BB', 'CC', 'zz']

  ## Say we have a list of strings we want to sort by the last letter of the string.
strs = ['xc', 'zb', 'yd' ,'wa']
def MyFn(s):
    return s[-1]
print(sorted(strs, key=MyFn))  ## ['wa', 'zb', 'xc', 'yd']