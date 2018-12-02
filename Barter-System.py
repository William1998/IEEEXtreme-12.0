
def backtracking (partialSol, starter, endgoal, checked):
    
    try:
        possible = alist[starter]
    except:
        possible = None
    if len(partialSol) != 0:
        if partialSol[len(partialSol)-1][0] == endgoal:
            global answer
            answer = partialSol[:]
            return
    if(possible):
        for item in possible:
            if item[0] in checked:
                continue
            partialSol.append(item)
            
            checked.append(starter)
            backtracking(partialSol, item[0], endgoal,checked)
            partialSol.pop()
            checked.pop()

num_pairs = int(input())
alist = {}
for i in range(num_pairs):
    pairs = input().split()
    item1 = pairs[0]
    item2 = pairs[1]
    rate = int(pairs[2])
    pos1 = None
    pos2 = None
    
    try:
        alist[item1]
    except KeyError:
        alist[item1] = []

    try:
        alist[item2]
    except KeyError:
        alist[item2] = []

    alist[item1].append([item2, rate])

def search (list, item):
    for i in range(len(list)):
        if list[i] == item:
            return i
    return None

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def modinv(a, m):
    g, x, y = egcd(a, m)
    return x % m

j = int(input())
for _ in range (j):
    [item1, item2] = input().split(' ')
    answer = 0
    backtracking([], item1, item2, [])
    if item1 == item2:
        print("1")
    elif answer == 0:
        backtracking([], item2, item1, [])
        if answer == 0:
            print("-1")
        else:
            real_ans = 1
            for item in answer:
                real_ans *= item[1]
            real_ans %= 998244353
            real_ans=modinv(real_ans, 998244353)
            print(real_ans)
    else:
        real_ans = 1
        for item in answer:
            real_ans *= item[1]
        real_ans %= 998244353
        print(real_ans)

""" for j in range(len(alist)):
        if item1 in alist[j]:
            pos1 = j
        if item2 in alist[j]:
            pos2 = j

    if (pos1 == None) and (pos2 == None): #both new items
        alist.append({item1: 1, item2: rate}) #create new dict
    elif pos2 == None: #only item2 is new
        alist[pos1][item2] = (alist[pos1][item1] * rate) % 998244353 #put item2 into item1's dict
    elif pos1 == None: #only item1 is new
        alist[pos2][item1] = (alist[pos2][item2] / rate) % 998244353 #put item1 into item2's dict
    else: #item1 and item2 in different dictionary
        for key, value in alist[pos2].items(): #iterate through item2's dict
            alist[pos1][key] = (value * rate) % 998244353
        del alist[pos2] #delete item2's dict

print(alist)
num_query = int(input())
for i in range(num_query):
    pairs = input().split()
    item1 = pairs[0]
    item2 = pairs[1]
    pos1 = None
    pos2 = None

    if item1 == item2:
        print(1)
        continue
    
    for j in range(len(alist)):
        if item1 in alist[j]:
            pos1 = j
        if item2 in alist[j]:
            pos2 = j

    if pos1 == None or pos2 == None: #item1 or 2 never appears
        print(-1)
        continue
        
    if pos1 != pos2: #item1 and 2 in different dict
        print(-1)
        continue
    else: #item1 and 2 in same dict
        value1 = alist[pos1][item1]
        value2 = alist[pos1][item2]
        result = (value2 + 998244353) / value1 % 998244353
        
        print(result)
        
    
    
        
        
 """