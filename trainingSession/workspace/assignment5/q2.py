import re


paragraph = '''The National Stock Exchange of India Limited (NSE) is the leading stock exchange of India, located in Mumbai. The NSE was established in 1992 as the first demutualized electronic exchange in the country. NSE was the first exchange in the country to provide a modern, fully automated screen-based electronic trading system which offered easy trading facility to the investors spread across the length and breadth of the country. Vikram Limaye is Managing Director & Chief Executive Officer of NSE.'''

# create regex patterns for all vowels
aP = r'[aA]'
eP = r'[eE]'
iP = r'[iI]'
oP = r'[oO]'
uP = r'[uU]'
# initialize the dictionary
counts = {"a":0,"e":0,"i":0,"u":0,"o":0}

# match the pattern and increment count
for i in paragraph:
    if re.match(aP, i):
        counts["a"]+=1
    if re.match(eP, i):
        counts["e"]+=1
    if re.match(iP, i):
        counts["i"]+=1
    if re.match(oP, i):
        counts["o"]+=1
    if re.match(uP, i):
        counts["u"]+=1

print(counts)