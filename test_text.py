from re import findall
from random import randint
def findWords(word,text):
        f = findall(r"%s[\s||\n||\?||!||\,]+(\w+)"%word,text)
        l = len(f)-1
        return f[randint(0,l)] if l != -1 else None
file = open("input.txt","r")
read = file.read()
file.close()
del file
text = ''
word = 'kill'
for i in range(100):
        if not word: break
        text +='%s '%word
        word = findWords(word,read)
        
out = open("output.txt","w")
out.write(text)
out.close()
