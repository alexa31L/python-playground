h = {}
h['word'] = 'garfield'
h['count'] = 42
s = 'I want %(count)d copies of %(word)s' % h  # %d for int, %s for string
# 'I want 42 copies of garfield'
