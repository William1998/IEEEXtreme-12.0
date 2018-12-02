testcase = int(input())
for _ in range(testcase):
    line1 = input().split() #read line 1
    target = int(line1[0])
    num_item = int(line1[1])
    if num_item <= 1:
        inputter=input()
        print("!OK")
        continue
    array = input().split(' ')

    sums = []
    hashtable = {}
    hashtable[str(array[0])] = int(array[0])

    flag = False
    for i in range (1, len(array)):
        sum_val = target-int(array[i])

        try:
            hashtable[str(sum_val)]
            print (min(hashtable[str(sum_val)], int(array[i])), max(hashtable[str(sum_val)], int(array[i])))
            flag = True
            break
        except:
            hashtable[str(array[i])] = int(array[i])
            continue
        
    if flag == False:
        print ("!OK")

