
anagrams=['eat', 'ate', 'done', 'tea', 'soup', 'node']
dic={}
for i in anagrams:
    word="".join(sorted(i))
    if word in dic:
        dic[word]+=' '+i
    else:
        dic[word]=i
        
print(dic)
