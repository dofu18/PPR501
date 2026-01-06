import re

string = 'hello 12 hi 89. Howdy 34'
pattern = r'\d+'

results = re.findall(pattern, string)
print(results)