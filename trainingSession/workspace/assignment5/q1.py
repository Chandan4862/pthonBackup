import re
import itertools

name = "Chandan"
pattern = r'^(?!.*rr).*$'

perm = []
# get all permutaions 
for i in itertools.permutations(name, len(name)):
    perm.append("".join(i))

final = []
# select only those permutations that doesn't satisfy the regex
for i in perm:
    mo = re.search(pattern, i)
    if mo:
        final.append(i)
print(final)