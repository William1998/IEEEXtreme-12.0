import sys

n = int(input())
string = "Q "+n*(str(0)+' ')
print(string[:-1])
sys.stdout.flush()
i = 0
result = int(input())

list = []
for j in range (n):
    list.extend([0])

if result == n:
    string = "A "
    for item in list:
        string += str(item) + ' '
    print (string[:-1])
    sys.stdout.flush()
    n=1    
    get_input = 1

for i in range (n-1):
    flag = False
    list[i] = 1
    string = "Q "
    for item in list:
        string += str(item) + ' '
    print (string[:-1])
    sys.stdout.flush()
    get_input = int(input())
    if get_input == n:
        string = "A "
        for item in list:
            string += str(item) + ' '
        
        print (string[:-1])
        sys.stdout.flush()
        flag = True
    if get_input < result:
        list[i] = 0
    else:
        result = get_input
    if flag == True:
        break

if get_input != n:
    list [n-1] = 1
    string = "A "
    for item in list:
        string += str(item) + ' '
    print (string[:-1])
    sys.stdout.flush()