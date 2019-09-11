import load_dict
word_list = load_dict.load('DIC.txt')
palin = []

for x in word_list:
    if len(x)>1 and x == x[::-1]:
        palin.append(x)

print("no of palindromes = {}".format(len(palin)))        
print(*palin,sep = "\n")