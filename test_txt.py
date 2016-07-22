from random import randint
import sys
from os import getcwd
new_txt = sys.argv[1] + ' '
word = new_txt[:-1]
def findWords(word,string,split=' ',start=None,stop=None):
    string_splited = string[start:stop].split(split)
    words = []
    start_fs = 0
    l = len(string_splited)-1
    while word in string_splited[start_fs:]:
        current_index = string_splited[start_fs:].index(word)
        if current_index+1+start_fs > l: break       
        words.append(string_splited[start_fs:][current_index+1])
        start_fs += current_index + 1
    if words == []: return False
    return words
file = open(r"%s/input.txt"%getcwd(),'r')
txt = ''
for line in file:
    txt += line.lower()
file.close()
del file

for i in range(100 if not 2 in argv else argv[2] ):
    if not findWords: break
    words_moment = findWords(word,txt)
    le = len(words_moment)-1
    word_moment = words_moment[randint(0,le)] if le>1 else words_moment[0]
    new_txt += word_moment + ' '
    word = word_moment
file =  open("output.txt","w")
file.write(new_txt)
file.close()
del file
print(new_txt)
