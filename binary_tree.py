class TreeNode:
    def __init__(self, item, height = 0, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right
        self.height = height

    def __str__(self):
        return str(self.item)

def recurse_tree(start, end, height):
    
    if end < start:
        return None

    root = prefix[recurse_tree.root_index] # get the root of the binary tree
    recurse_tree.root_index += 1        # prepare for second root 
    
    our_node = TreeNode(root, height)
    if (start == end):        # no children
        return our_node
    
    node_stopper = search(start, end, root)
    if node_stopper == None:
        return None

    our_node.left = recurse_tree (start, node_stopper-1, height+1)
    our_node.right = recurse_tree (node_stopper+1, end, height+1)

    return our_node

# no null needed
def search (start, end, value):
    for i in range (start,end+1):
        if infix[i]==value:
            return i

def traverser(tree):
    global big_list
    global max_height
    if tree == None:
        return 
    if(tree.height>max_height):
        max_height = tree.height
    if tree.height >= len(big_list):
        big_list.append(['',tree.item])
    else:
        big_list[tree.height].extend(['', tree.item])
    traverser(tree.left)
    traverser(tree.right)

def searcher (value, tree):
    global answer
    if tree == None:
        return
    if tree.item == value:
        answer = tree
    searcher(value, tree.left)
    searcher(value,tree.right)

infix = "something"
while infix != "":
    try:
        infix = input().strip()
        
    except:
        break
    if infix == "":
        break
    prefix = input().strip()

    big_list = []
    big_big_list = []
    max_height = 0

    recurse_tree.root_index = 0
    tree = (recurse_tree(0, len(infix)-1,0))


    traverser(tree)

    for j in range(len(infix)):
        list = []
        for i in range(len(infix)):
            list.append(' ')
        big_big_list.append(list)
    for i in range(len(infix)):
        head = infix[i]
        answer = 0
        searcher(head, tree)
        big_big_list[answer.height][i] = head
    for k in range(len(big_big_list)):
        row = big_big_list[k]
        list = []
        for l in range(len(infix)):
            list.append(' ')
        if row == list:
            continue
        if k != 0:
            print()
        string = ""
        for item in row:
            string+=item
        string.strip('')
        print(string, end='')
        
