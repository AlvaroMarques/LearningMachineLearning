from re import findall,sub
from random import randint
from sys import argv
def findWords(word,text):
        f = findall(r"%s([\W]+\w+)"%sub("\W+",'',word),text)
        l = len(f)-1
        return f[randint(0,l)] if l != -1 else None
file = open("input.txt","r")
read = file.read()
file.close()
del file
text = ''
word = argv[1] if len(argv)>=1 else 'fight'
for i in range(100 if  len(argv) < 2 else int(argv[2])):
        if not word: break
        text +='%s'%word
        word = findWords(word,read)

print(text)        
out = open("output.txt","w")
out.write(text)
out.close()

