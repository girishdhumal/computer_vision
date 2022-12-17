import re
from nltk.tokenize import RegexpTokenizer
tk=RegexpTokenizer('\s+',gaps=True)

gfg="MSCIT PART 2 KC COLLEGE"
msc=tk.tokenize(gfg)
print(msc)

sentence="BASKETBALL, HOCKEY, TENNIS GOLF"
print(re.split(';',sentence))
print(re.split(r'[;,s]',sentence))
