from random import randint
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
file = open("input.txt",'r')
txt = file.read().lower()
file.close()
del file
new_txt = 'ford '
word = 'ford'
for i in range(100):
    if not findWords: break
    words_moment = findWords(word,txt)
    le = len(words_moment)-1
    word_moment = words_moment[randint(0,le)] if le>1 else words_moment[0]
    new_txt += word_moment + ' '
    word = word_moment
open("output.txt","w").write(new_txt)