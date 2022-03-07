line='python is a powerful and general purpose programming language'
words=line.split()
print(words)
stuff=[[w.upper(),w.lower(),len(w)] for w  in words]
for i in stuff:
       print(i)
