def great(num, num2):
    if num >= num2:
        return True
    return False

import json
n = int(input())
author_dict = {}
for _ in range(n):
    json_file = input()
    js = json.loads(json_file)
    authors = js['authors']['authors'] #the list of dictionary
    citing = js['citing_paper_count']
    for i in range(len(authors)):
        author_name = authors[i]['full_name'] #get the full name of one author
        if author_name not in author_dict:
            author_dict[author_name] = [citing]
        else:
            author_dict[author_name].append(citing)

for name, citing in author_dict.items():
    num_cite = min(min(citing), len(citing))
    flag = True
    while flag == True:
        total = 0
        for i in range(len(citing)):
            if citing[i] >= num_cite:
                total+=1
        if total < num_cite:
            flag = False
        else:
            num_cite +=1
    num_cite -= 1
    author_dict[name] = num_cite
    
author_list = list(author_dict.items())
author_list.sort(key = lambda x: x[0])
author_list.sort(key = lambda x: x[1], reverse = True)

for i in range(len(author_list)):
    print(author_list[i][0], author_list[i][1])
