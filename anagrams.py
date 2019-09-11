import load_dict
word_list = load_dict.load('DIC.txt')
name = input("enter any name:")
name_sort = sorted(name)
anagram = []
for word in word_list:
    if word != name:
        if sorted(word) == name_sort:
            anagram.append(word)

if len(anagram) == 0:
    print("need a bigger dictionary or word is rare")
else:
    print("The anagrams of {} are ".format(name),*anagram,sep='\n')            
