def traverse(start, end, where_are_we):
    if start > end:
        return 0
    else:
        mid = (start + end) // 2
        time = (mid - where_are_we) * M + S
        start = mid
        where_are_we = mid
        return time + traverse(start+1, end, where_are_we)

line = input().split()
N = int(line[0])
M = int(line[1])
S = int(line[2])

time = traverse(2, N, 1)
print(time)