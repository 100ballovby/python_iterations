from itertools import *

print(*permutations('ЯБГ', 2))
print(*combinations('ЯБГ', 2))

print(*combinations_with_replacement(
        ['red', 'white', 'blue'], 4
))