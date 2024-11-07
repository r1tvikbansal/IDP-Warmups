exclude = {word for line in open("exclude_include_warmup/exclude.txt") for word in line.split()} #curly brackets
include = set(word for line in open("exclude_include_warmup/include.txt") for word in line.split() if word not in exclude) #or can use set() keyword
print(include)