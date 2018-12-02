get_input = input()
length = len(get_input)
if length % 4 != 0:
    print('impossible')
elif get_input[0] == ']' or get_input[0] == ')':
    print('impossible')
else:
    s1 = []
    s2 = []
    s1_counter = length / 4
    s1_done = s1_counter
    string = ''
    for i in range(length):
        if get_input[i] == '(':
            if s1_counter > 0:
                s1.append('(')
                string += '1' + ' '
                s1_counter -= 1
                continue
            else:
                s2.append('(')
                string += '2' + ' '
                continue
        elif get_input[i] == '[':
            if s1_counter > 0:
                s1.append('[')
                string += '1' + ' '
                s1_counter -= 1
                continue
            else:
                s2.append('[')
                string += '2' + ' '
                continue
                
        elif get_input[i] == ')':
            if s1_done > 0: # s1 stack not empty yet
                error = True
                if s1[-1] == '(':
                    s1.pop()
                    s1_done -= 1
                    string += '1' + ' '
                    error = False
                    continue
                if error == True and len(s2) == 0:
                    print('impossible')
                    exit(0)
                elif s2[-1] == '(':
                    s2.pop()
                    string += '2' + ' '
                    error = False
                    continue
                if error == True:
                    print('impossible')
                    exit(0)
            else: # s1 stack is empty
                if len(s2) == 0:
                    print('impossible')
                    exit(0)
                item = s2.pop()
                if item != '(':
                    print('impossible')
                    exit(0)
                else:
                    string += '2' +' '
                    continue
                    
        elif get_input[i] == ']':
            if s1_done > 0: # s1 stack not empty yet
                error = True
                if s1[-1] == '[':
                    s1.pop()
                    s1_done -= 1
                    string += '1' + ' '
                    error = False
                    continue
                if error == True and len(s2) == 0:
                    print('impossible')
                    exit(0)
                elif s2[-1] == '[':
                    s2.pop()
                    string += '2' + ' '
                    error = False
                    continue
                if error == True:
                    print('impossible')
                    exit(0)
            else: # s1 stack is empty
                if len(s2) == 0:
                    print('impossible')
                    exit(0)
                item = s2.pop()
                if item != '[':
                    print('impossible')
                    exit(0)
                else:
                    string += '2' +' '
                    
    print(string)